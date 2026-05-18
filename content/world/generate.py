import numpy as np
from numba import njit, prange
from config import (
    CHUNK_SZ, CHUNK_H, SEA_LEVEL, WATER_OFF,
    TERRAIN_SCL_X, TERRAIN_SCL_Z, TERRAIN_SCL_Y
)
from world.noise import (
    noise3d, fractal3d, get_climate, climate_tobiome,
    smooth_bonus, _hf_badlands, _badland_bonus, _badlands_band
)


# the big one
# 
@njit(cache=True, fastmath=True, parallel=True, nogil=True)
def _generate(voxels, off_x, off_z, p, biomes):
    _field   = np.zeros((5, 17, 5), dtype=np.float32)
    coarse_b = np.zeros((5, 5),     dtype=np.int8)
    coarse_t = np.zeros((5, 5),     dtype=np.float32)
    coarse_h = np.zeros((5, 5),     dtype=np.float32)

    scale_x, scale_z, scale_y = TERRAIN_SCL_X, TERRAIN_SCL_Z, TERRAIN_SCL_Y

    h_factors = np.zeros(17, dtype=np.float32)
    for y in range(17):
        wy = float(y * 8)
        h_val = (wy - 64.0) / 48.0
        if wy > 75.0:  h_val += ((wy - 75.0)  / 20.0) ** 2.0
        if wy > 80.0:  h_val += ((wy - 80.0)  / 20.0) ** 3.5
        if wy > 100.0: h_val -= ((wy - 100.0) / 20.0) ** 5.0
        h_factors[y] = h_val
        
        
        

    # pass 1a
    # climate && biome @ coarse grid
    for x in prange(5):
        for z in range(5):
            wx_c = off_x + x * 4.0
            wz_c = off_z + z * 4.0
            t_c, h_c = get_climate(wx_c, wz_c, p)
            coarse_t[x, z] = t_c
            coarse_h[x, z] = h_c
            coarse_b[x, z] = climate_tobiome(t_c, h_c)
            
            
            
            

    # pass 1b
    # noise field && badlands bound blend
    for x in prange(5):
        for z in range(5):
            wx_c = off_x + x * 4.0
            wz_c = off_z + z * 4.0
            t_c  = coarse_t[x, z]
            h_c  = coarse_h[x, z]
            bc   = coarse_b[x, z]

            fm  = 0.0
            fm2 = 0.0
            bw  = 0.0
            if bc == 4:
                
                fm  = noise3d(wx_c * 0.008, 200.0, wz_c * 0.008, p)
                fm2 = noise3d(wx_c * 0.025, 400.0, wz_c * 0.025, p)

                # blend weight
                # 3x3 neighbor count 
                # (badlands neighbros)
                n_bad = 0
                n_tot = 0
                for dx in range(-1, 2):
                    for dz in range(-1, 2):
                        nx = x + dx
                        nz = z + dz
                        n_tot += 1
                        if 0 <= nx < 5 and 0 <= nz < 5:
                            if coarse_b[nx, nz] == 4:
                                n_bad += 1
                                
                        else: n_bad += 1
                bw = float(n_bad) / float(n_tot)
                

            for y in range(17):
                wy        = float(y * 8)
                noisev = fractal3d(
                    wx_c, wy, wz_c, p,
                    octav=6, presist=0.5, lacunarity=2.0,
                    scale_x=scale_x, scale_y=scale_y, scale_z=scale_z
                )


                noisev *= 1.3
                shaped = noisev * noisev * noisev * 4.0

                if bc == 4:
                    hf_bad = _hf_badlands(wy)
                    hf_def = h_factors[y]
                    hf     = hf_bad * bw + hf_def * (1.0 - bw)

                    hb_bad = _badland_bonus(fm, fm2, wy)
                    hb_def = smooth_bonus(t_c, h_c, wy)
                    h_bonus = hb_bad * bw + hb_def * (1.0 - bw)
                    
                    
                else:
                    hf = h_factors[y]
                    h_bonus = smooth_bonus(t_c, h_c, wy)

                _field[x, y, z] = shaped - hf + h_bonus
    
    
    
    
    
    
    
    
    
    # pass 2
    # trilinear interpol to voxels
    
    for x in prange(4):
        for z in range(4):
            for y in range(16):
                d000 = _field[x, y, z]
                d100 = _field[x + 1, y, z]
                d010 = _field[x, y + 1, z]
                d110 = _field[x + 1, y + 1, z]
                d001 = _field[x, y, z + 1]
                d101 = _field[x + 1, y, z + 1]
                d011 = _field[x, y + 1, z + 1]
                d111 = _field[x + 1, y + 1, z + 1]
                # pretty ^^

                for i_y in range(8):
                    ty  = i_y / 8.0
                    d00 = d000 + (d010 - d000) * ty
                    d10 = d100 + (d110 - d100) * ty
                    d01 = d001 + (d011 - d001) * ty
                    d11 = d101 + (d111 - d101) * ty

                    for i_x in range(4):
                        tx = i_x / 4.0
                        d0 = d00 + (d10 - d00) * tx
                        d1 = d01 + (d11 - d01) * tx


                        for i_z in range(4):
                            dens = d0 + (d1 - d0) * (i_z / 4.0)

                            bx = x * 4 + i_x
                            by = y * 8 + i_y
                            bz = z * 4 + i_z

                            if dens > 0.0:
                                if by <= 5: voxels[bx, by, bz] = 4   # bedrock
                                else:
                                    wx_b = off_x + bx
                                    wy_b = float(by)
                                    wz_b = off_z + bz
                                    if noise3d(
                                            wx_b * 0.1, 
                                            wy_b * 0.1, 
                                            wz_b * 0.1, 
                                            p
                                        ) > 0.2:
                                        voxels[bx, by, bz] = 12 
                                        # gravel vein
                                        # gravel veiny
                                        # veiny ahh gravel
                                        # veiny ahh dih
                                        # im funny
                                        
                                    else:
                                        hh = int(wx_b) * 428761 ^ int(wy_b) * 912876 ^ int(wz_b) * 312987
                                        voxels[bx, by, bz] = 15 if (hh & 63) == 0 else 3



                            elif by < (SEA_LEVEL - WATER_OFF):
                                voxels[bx, by, bz] = 5

    
    
    
    
    
    
    
    
    
    
    # pass 2b
    # cave carving
    # water repelled
    sea_wl = SEA_LEVEL - WATER_OFF
    CAVE_WATER_R1 = 5
    CAVE_WATER_R2 = 25.0

    # precomp percolumn water presence
    _haswater = np.zeros((CHUNK_SZ, CHUNK_SZ), dtype=np.int8)
    for cx_w in range(CHUNK_SZ):
        for cz_w in range(CHUNK_SZ):
            for cy_w in range(CHUNK_H):
                if voxels[cx_w, cy_w, cz_w] == 5:
                    _haswater[cx_w, cz_w] = 1
                    break

    # precomp 2d min ^2 distance to nearest water column within R
    min2d_w = np.full((CHUNK_SZ, CHUNK_SZ), CAVE_WATER_R2 + 1.0, dtype=np.float32)
    for cx_w in range(CHUNK_SZ):

        for cz_w in range(CHUNK_SZ):
            mind2 = CAVE_WATER_R2 + 1.0

            for ddx in range(-CAVE_WATER_R1, CAVE_WATER_R1 + 1):
                nnx = cx_w + ddx

                if 0 <= nnx < CHUNK_SZ:
                    for ddz in range(-CAVE_WATER_R1, CAVE_WATER_R1 + 1):
                        nnz = cz_w + ddz

                        if 0 <= nnz < CHUNK_SZ and _haswater[nnx, nnz] == 1:
                            d2 = float(ddx * ddx + ddz * ddz)

                            if d2 < mind2:
                                mind2 = d2
                                
                                
            min2d_w[cx_w, cz_w] = mind2




    for x in prange(CHUNK_SZ):
        for z in range(CHUNK_SZ):
            wx = off_x + float(x)
            wz = off_z + float(z)
            mind2 = min2d_w[x, z]
            
            
            for y in range(6, 95):
                
                bv = voxels[x, y, z]
                if bv == 0 or bv == 4 or bv == 5: continue
                wy = float(y)

                cave_t = 0.12 if y < 35 else 0.10
                if y >= 52:
                    if y < 68:   cave_t *= 1.0 - (wy - 52.0) / 16.0
                    elif y < 95: cave_t = 0.10 * 0.4 * (1.0 - (wy - 68.0) / 27.0)
                    else:        cave_t = 0.0
                    
                    

                # water avoid <- distance field
                if cave_t > 0.0 and y < sea_wl + CAVE_WATER_R1:
                    if mind2 <= CAVE_WATER_R2:
                        cave_t *= mind2 ** 0.5 / float(CAVE_WATER_R1)

                if cave_t > 0.0:
                    cn1 = noise3d(
                        (wx + 50000.0) * 0.015, wy * 0.040,
                        (wz + 50000.0) * 0.015, p
                    )

                    cn2 = noise3d(
                        wz * 0.040, 
                        (wy + 50000.0) * 0.015,
                        wx * 0.040, p
                    )
                    
                    if cn1 * cn1 + cn2 * cn2 < cave_t * cave_t:
                        voxels[x, y, z] = 0

    
    
    
    
    
    
    
    
    
    # pass3 
    # surface blocks 
    # w bilinear climate enterpol
    for x in range(CHUNK_SZ):
        for z in range(CHUNK_SZ):
            cx  = x >> 2
            cz  = z >> 2
            fx  = float(x & 3) * 0.25
            fz  = float(z & 3) * 0.25
            cx1 = cx + 1
            cz1 = cz + 1

            t_bl = (coarse_t[cx, cz ] * (1.0-fx) + coarse_t[cx1, cz ] * fx) * (1.0-fz) \
                 + (coarse_t[cx, cz1] * (1.0-fx) + coarse_t[cx1, cz1] * fx) * fz
            h_bl = (coarse_h[cx, cz ] * (1.0-fx) + coarse_h[cx1, cz ] * fx) * (1.0-fz) \
                 + (coarse_h[cx, cz1] * (1.0-fx) + coarse_h[cx1, cz1] * fx) * fz

            j = noise3d((off_x + x) * 0.06, 0.0, (off_z + z) * 0.06, p) * 0.045
            biome = climate_tobiome(t_bl + j, h_bl + j * 0.7)
            biomes[x, z] = biome

            col_wx = off_x + x
            col_wz = off_z + z



            top = -1
            for y in range(CHUNK_H - 1, -1, -1):
                bv = voxels[x, y, z]
                if bv != 0 and bv != 5:
                    top = y
                    break
            
            if top == -1: continue

            beach = (top >= SEA_LEVEL - 6) and (top <= SEA_LEVEL - 2) and biome != 4
            tb    = voxels[x, top, z]
            
            
            if tb != 3 and tb != 12 and tb != 15: continue

            if top >= SEA_LEVEL - 5:
                if beach:
                    voxels[x, top, z] = 6
                    if noise3d(col_wx * 0.1, float(top) * 0.1, col_wz * 0.1, p) > 0.2:
                        voxels[x, top, z] = 14
                        
                        
                elif biome == 1: voxels[x, top, z] = 6    # desert:1  -> sand
                elif biome == 2: voxels[x, top, z] = 335  # snowy:2   -> snow
                elif biome == 4: voxels[x, top, z] = 85   # badlands:4 -> red_sand
                else:            voxels[x, top, z] = 1    
                
                
                
                
                
                for d in range(1, 4):
                    
                    sub_y = top - d
                    if sub_y < 0: break
                    bb = voxels[x, sub_y, z]
                    if bb != 3 and bb != 12 and bb != 15: break
                    
                    
                    if beach:
                        voxels[x, sub_y, z] = 6
                        if noise3d(col_wx * 0.1, float(sub_y) * 0.1, col_wz * 0.1, p) > 0.2:
                            voxels[x, sub_y, z] = 14
                            
                            
                    elif biome == 1: voxels[x, sub_y, z] = 6 if d <= 2 else 14  # desert
                    elif biome == 4: voxels[x, sub_y, z] = 89                   # badlands, overrideen
                        
                    else:
                        voxels[x, sub_y, z] = 2
                        hh = int(col_wx) * 73856093 ^ int(sub_y) * 19349663 ^ int(col_wz) * 83492791
                        if (hh & 31) == 0:
                            voxels[x, sub_y, z] = 13
                            
                            
            else:
                voxels[x, top, z] = 2

    
    
    
    
    
    
    # post processing passes --
    # biome specific decors and such
    
    # terracotta band
    for x in range(CHUNK_SZ):
        for z in range(CHUNK_SZ):
            if biomes[x, z] != 4:
                continue

            surf_y = -1
            for sy in range(CHUNK_H - 1, -1, -1):
                bv = voxels[x, sy, z]
                if bv != 0 and bv != 5:
                    surf_y = sy
                    break
                    
                    

            col_wx_f = float(off_x + x)
            col_wz_f = float(off_z + z)
            y_off = int(
                noise3d(col_wx_f * 0.04, 0.0, col_wz_f * 0.04, p) * 7.0
            )

            for y in range(surf_y - 1, 3, -1):
                bv = voxels[x, y, z]
                if bv == 0 or bv == 5  or bv == 4: continue
                if (
                    bv == 3 or bv == 12 or 
                    bv == 15 or bv == 2 or 
                    bv == 89 or bv == 85 or 
                    bv == 86
                ):
                    
                    voxels[x, y, z] = _badlands_band(y + y_off)
                    
                    

    # frozen surface water
    for x in range(CHUNK_SZ):
        for z in range(CHUNK_SZ):
            
            if biomes[x, z] != 2: continue
            
            
            for y in range(CHUNK_H - 1, 0, -1):
                bv = voxels[x, y, z]
                if bv == 5:
                    if y + 1 >= CHUNK_H or voxels[x, y + 1, z] == 0:
                        voxels[x, y, z] = 48
                        break
                        
                        
                        
                elif bv != 0: break













