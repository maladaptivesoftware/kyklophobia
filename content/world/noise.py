import numpy as np
from numba import njit


@njit(cache=True, fastmath=True)
def fade(t): return t * t * t * (t * (t * 6.0 - 15.0) + 10.0)

@njit(cache=True, fastmath=True)
def lerp(t, a, b): return a + t * (b - a)




@njit(cache=True, fastmath=True)
def grad(hash_val, x, y, z):
    h = hash_val & 15
    u = x if h < 8 else y
    v = y if h < 4 else (x if h == 12 or h == 14 else z)
    return (u if (h & 1) == 0 else -u) + (v if (h & 2) == 0 else -v)




@njit(cache=True, fastmath=True)
def noise3d(x, y, z, p):
    xi = int(np.floor(x)) & 255
    yi = int(np.floor(y)) & 255
    zi = int(np.floor(z)) & 255
    
    xf = x - np.floor(x)
    yf = y - np.floor(y)
    zf = z - np.floor(z)
    
    u = fade(xf)
    v = fade(yf)
    w = fade(zf)
    
    
    aaa = p[p[p[xi] + yi] + zi]
    aab = p[p[p[xi] + yi] + zi + 1]
    aba = p[p[p[xi] + yi + 1] + zi]
    abb = p[p[p[xi] + yi + 1] + zi + 1]
    baa = p[p[p[xi + 1] + yi] + zi]
    bab = p[p[p[xi + 1] + yi] + zi + 1]
    bba = p[p[p[xi + 1] + yi + 1] + zi]
    bbb = p[p[p[xi + 1] + yi + 1] + zi + 1]
    
    x1 = lerp(u, grad(aaa, xf, yf, zf), grad(baa, xf - 1.0, yf, zf))
    x2 = lerp(u, grad(aba, xf, yf - 1.0, zf), grad(bba, xf - 1.0, yf - 1.0, zf))
    y1 = lerp(v, x1, x2)
    # larp
    
    x1 = lerp(u, grad(aab, xf, yf, zf - 1.0), grad(bab, xf - 1.0, yf, zf - 1.0))
    x2 = lerp(u, grad(abb, xf, yf - 1.0, zf - 1.0), grad(bbb, xf - 1.0, yf - 1.0, zf - 1.0))
    y2 = lerp(v, x1, x2)
    
    return lerp(w, y1, y2)








@njit(cache=True, fastmath=True)
def fractal3d(
        x, y, z, 
        p, octav, 
        presist, lacunarity, 
        scale_x, scale_y, scale_z
    ):

    t = 0.0
    freq = 1.0
    ampl = 1.0
    _max = 0.0
    
    for _ in range(octav):
        t += noise3d(
            x * scale_x * freq, 
            y * scale_y * freq, 
            z * scale_z * freq, 
            p
        ) * ampl



        _max += ampl
        ampl *= presist
        freq *= lacunarity
    
    return t






# bids
BIOME_PLAINS   = 0
BIOME_DESERT   = 1
BIOME_SNOWY    = 2
BIOME_JUNGLE   = 3
BIOME_BADLANDS = 4
BIOME_FOREST   = 5

BIOME_NAMES = (
    "Plains", 
    "Desert", 
    "Snowy", 
    "Jungle", 
    "Badlands", 
    "Forest"
)




@njit(cache=True, fastmath=True)
def get_climate(wx, wz, p):

    t = fractal3d(
        wx + 15000.0, 0.0, wz + 15000.0, p,
        octav=4, presist=0.5, lacunarity=2.0,
        scale_x=0.00120, scale_y=0.0, scale_z=0.00120
    ) * 0.5 + 0.5
    
    h = fractal3d(
        wx - 15000.0, 0.0, wz - 15000.0, p,
        octav=4, presist=0.5, lacunarity=2.0,
        scale_x=0.00150, scale_y=0.0, scale_z=0.00150
    ) * 0.5 + 0.5

    
    return t, h










@njit(cache=True, fastmath=True)
def climate_tobiome(temp, humid):
    if temp < 0.27:        return 2   # snowy
    
    elif temp > 0.72:
        if humid < 0.30:   return 1   # desert
        elif humid > 0.65: return 3   # jngle
        else:              return 4   # badlands
        
    else:
        if humid > 0.55:   return 5   # forest
        else:              return 0   # plains


@njit(cache=True, fastmath=True)
def get_biome(wx, wz, p):
    temp, humid = get_climate(wx, wz, p)
    j = noise3d(wx * 0.06, 0.0, wz * 0.06, p) * 0.045
    return climate_tobiome(temp + j, humid + j * 0.7)











@njit(cache=True, fastmath=True, inline='always')
def _hb_plains(wy):
    if wy > 80.0:   return -0.22
    elif wy > 70.0: return -0.06
    else: return 0.01


@njit(cache=True, fastmath=True, inline='always')
def _hb_desert(wy):
    return -0.45






@njit(cache=True, fastmath=True, inline='always')
def _hb_snowy(wy):
    if wy > 74.0: return -0.14
    else: return 0.02

@njit(cache=True, fastmath=True, inline='always')
def _hb_jungle(wy):
    if wy > 82.0:   return 0.20
    elif wy > 68.0: return 0.13
    else: return 0.03

@njit(cache=True, fastmath=True, inline='always')
def _hb_badlands(wy):
    if wy > 95.0:   return -0.20
    elif wy > 79.0: return  0.90
    elif wy > 67.0: return  0.45
    else:           return  0.12







@njit(cache=True, fastmath=True, inline='always')
def _hf_badlands(wy):
    hf = (wy - 60.0) / 38.0
    if wy > 110.0:
        d = (wy - 110.0) / 20.0
        hf += d * d * d
    return hf


@njit(cache=True, fastmath=True, inline='always')
def _hb_forest(wy):
    if wy > 78.0: return -0.03
    else: return 0.08


@njit(cache=True, fastmath=True)
def _ss(x, lo, hi):
    t = (x - lo) / (hi - lo)
    if t < 0.0: t = 0.0
    if t > 1.0: t = 1.0
    return t * t * (3.0 - 2.0 * t)












@njit(cache=True, fastmath=True)
def smooth_bonus(temp, humid, wy):
    B = 0.08


    w_snow = 1.0 - _ss(temp, 0.27 - B, 0.27)
    w_hot  =       _ss(temp, 0.72, 0.72 + B)

    w_temp = 1.0 - w_snow - w_hot
    if w_temp < 0.0: w_temp = 0.0

    # hot sub wgts
    w_des = 1.0 - _ss(humid, 0.30 - B, 0.30)
    w_jun =       _ss(humid, 0.65, 0.65 + B)

    w_bad = 1.0 - w_des - w_jun
    if w_bad < 0.0: w_bad = 0.0
    hs = w_des + w_bad + w_jun


    if hs > 0.0:
        inv = 1.0 / hs
        w_des *= inv; w_bad *= inv; w_jun *= inv

    # mid sub weights
    w_for = _ss(humid, 0.55, 0.55 + B)
    w_pla = 1.0 - w_for

    b_hot  = w_des * _hb_desert(wy) + w_bad * _hb_badlands(wy) + w_jun * _hb_jungle(wy)
    b_temp = w_for * _hb_forest(wy) + w_pla * _hb_plains(wy)

    return  w_snow * _hb_snowy(wy)  + w_hot * b_hot + w_temp * b_temp









@njit(cache=True, fastmath=True, inline='always')
def _badlands_band(y_adj):
    mod = int(y_adj) % 32
    
    if   mod < 2:  return 136   # orange
    elif mod < 4:  return 136   # orange
    elif mod < 6:  return 89    # terracotta (tan)
    elif mod < 8:  return 89    # terracotta
    elif mod < 10: return 149   # red
    elif mod < 11: return 149   # red
    elif mod < 13: return 136   # orange
    elif mod < 15: return 136   # orange
    elif mod < 17: return 139   # yellow
    elif mod < 19: return 135   # white
    elif mod < 21: return 143   # gray
    elif mod < 22: return 135   # white
    elif mod < 24: return 136   # orange
    elif mod < 26: return 89    # terracotta
    elif mod < 27: return 147   # brown
    elif mod < 28: return 149   # red
    elif mod < 29: return 149   # red
    elif mod < 30: return 135   # white
    elif mod < 31: return 143   # silver
    else:          return 136   # orange (end)







@njit(cache=True, fastmath=True, inline='always')
def _badland_bonus(fm, fm2, wy):
    fm_eff = fm + fm2 * 0.12

    # 5 plateau tiers 
    # cumulative smoothsteps
    h = -0.55
    h += 0.50 * _ss(fm_eff, -0.22, -0.18)
    h += 0.45 * _ss(fm_eff, -0.09, -0.05)
    h += 0.40 * _ss(fm_eff,  0.05,  0.09)
    h += 0.60 * _ss(fm_eff,  0.20,  0.24)

    # hoodoo spires
    if fm2 > 0.25 and wy > 79.0:
        spire = (fm2 - 0.25) * 2.0
        if spire > 0.55:
            spire = 0.55
        h += spire

    # height decay
    # rm floating islands
    if wy > 92.0:  h -= (wy - 92.0) * 0.012

    return h






@njit(cache=True, fastmath=True)
def locate_biome(
        px, pz, 
        target, p, 
        max_radius=3200, 
        step=32
    ):
        
    r = step
    while r <= max_radius:
        dx = -r
        while dx <= r:
            if get_biome(float(px + dx), float(pz + r), p) == target:
                return float(px + dx), float(pz + r)
            dx += step
        dx = -r
        
        
        while dx <= r:
            if get_biome(float(px + dx), float(pz - r), p) == target:
                return float(px + dx), float(pz - r)
            dx += step
        dz = -r + step
        
        
        while dz <= r - step:
            if get_biome(float(px + r), float(pz + dz), p) == target:
                return float(px + r), float(pz + dz)
            dz += step
        dz = -r + step
        
        
        while dz <= r - step:
            if get_biome(float(px - r), float(pz + dz), p) == target:
                return float(px - r), float(pz + dz)
            dz += step
        r += step
        
        
    return -1.0, -1.0




"""
def locate_biome(px, pz, target, p, max_radius=3200, step=64):
    for r in range(step, max_radius + step, step):
        for angle in range(0, 360, 10):
            rad = math.radians(angle)
            x = px + math.cos(rad) * r
            z = pz + math.sin(rad) * r
            if get_biome(float(x), float(z), p) == target:
                return float(x), float(z)
    return -1.0, -1.0
"""





