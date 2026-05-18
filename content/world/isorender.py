import pygame
import pygame.surfarray
import numpy as np
import math

from world.animation import getanims



# yaw 135 -> n R + w L, pitch 30 -> top
_ISO_YAW   = math.radians(135)
_ISO_PITCH = math.radians(30)
_COS_Y = math.cos(_ISO_YAW)
_SIN_Y = math.sin(_ISO_YAW)
_COS_P = math.cos(_ISO_PITCH)
_SIN_P = math.sin(_ISO_PITCH)

_TOP_SHADE = 1.0
_F_TOP, _F_BOT, _F_NORTH, _F_SOUTH, _F_EAST, _F_WEST = range(6)


# shade p face := north=right(0.6, west=left(0.8)
_FACE_SHADE   = [_TOP_SHADE, 0.5, 0.6, 0.8, 0.6, 0.8]
_HIDDEN_FACES = {_F_BOT, _F_SOUTH, _F_EAST}


"""
def _iso_project(x, y, z):
    cx, cy, cz = x - 0.5, y - 0.5, z - 0.5
    rx = _COS_Y * cx + _SIN_Y * cz
    return (rx, -cy)
"""

def _iso_project(x, y, z):
    # R_y 135 --> R_x 30 @plane
    cx, cy, cz = x - 0.5, y - 0.5, z - 0.5
    rx = _COS_Y * cx + _SIN_Y * cz
    rz = -_SIN_Y * cx + _COS_Y * cz
    ry = _COS_P * cy - _SIN_P * rz
    return (rx, -ry)


_unit_corner = [(x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1)]
_proj_xs    = [_iso_project(x, y, z)[0] for x, y, z in _unit_corner]
_proj_ys    = [_iso_project(x, y, z)[1] for x, y, z in _unit_corner]
_PROJ_W     = max(_proj_xs) - min(_proj_xs)
_PROJ_H     = max(_proj_ys) - min(_proj_ys)
_PROJ_MIN_X = min(_proj_xs)
_PROJ_MIN_Y = min(_proj_ys)






def _iso_proj(x, y, z, s):
    sx, sy = _iso_project(x, y, z)
    pad    = 1
    usable = s - 2 * pad
    scale  = usable / max(_PROJ_W, _PROJ_H)
    px = pad + (sx - _PROJ_MIN_X) * scale + (usable - _PROJ_W * scale) * 0.5
    py = pad + (sy - _PROJ_MIN_Y) * scale + (usable - _PROJ_H * scale) * 0.5
    return (px, py)




def _render_faceuv(surf, corners_3d, uv_corners, texture, shade, s):
    p0 = _iso_proj(*corners_3d[0], s)
    p1 = _iso_proj(*corners_3d[1], s)
    p3 = _iso_proj(*corners_3d[3], s)

    ux, uy = p1[0] - p0[0], p1[1] - p0[1]
    vx, vy = p3[0] - p0[0], p3[1] - p0[1]

    det = ux * vy - vx * uy
    if abs(det) < 0.001:
        return

    inv_det = 1.0 / det
    tw, th  = texture.get_width(), texture.get_height()
    

    p2        = _iso_proj(*corners_3d[2], s)
    corners_x = [p0[0], p1[0], p2[0], p3[0]]
    corners_y = [p0[1], p1[1], p2[1], p3[1]]
    min_x = max(0,     int(math.floor(min(corners_x))))
    max_x = min(s - 1, int(math.ceil( max(corners_x))))
    min_y = max(0,     int(math.floor(min(corners_y))))
    max_y = min(s - 1, int(math.ceil( max(corners_y))))
    #print(min_x, max_x, min_y, max_y)

    if min_x > max_x or min_y > max_y:
        return
        
        
        

    px_range = np.arange(min_x, max_x + 1, dtype=np.float32)
    py_range = np.arange(min_y, max_y + 1, dtype=np.float32)
    gx, gy   = np.meshgrid(px_range, py_range)

    dx = gx - p0[0]
    dy = gy - p0[1]

    #u/v = bilinear coords face quad [0,1]^2
    u = (vy * dx - vx * dy) * inv_det
    v = (ux * dy - uy * dx) * inv_det

    mask = (u >= 0.0) & (u <= 1.0) & (v >= 0.0) & (v <= 1.0)
    if not mask.any():
        return
        
        
        
        

    u0s, v0s = uv_corners[0]
    u1s, v1s = uv_corners[1]
    u3s, v3s = uv_corners[3]

    tu = u0s + u * (u1s - u0s) + v * (u3s - u0s)
    tv = v0s + u * (v1s - v0s) + v * (v3s - v0s)

    tx = np.clip((tu * tw).astype(np.int32), 0, tw - 1)
    ty = np.clip((tv * th).astype(np.int32), 0, th - 1)

    tex_arr   = pygame.surfarray.pixels3d(texture)
    tex_alpha = pygame.surfarray.pixels_alpha(texture)

    sr = tex_arr[tx, ty, 0].astype(np.float32)
    sg = tex_arr[tx, ty, 1].astype(np.float32)
    sb = tex_arr[tx, ty, 2].astype(np.float32)
    sa = tex_alpha[tx, ty]
    

    mask = mask & (sa > 0)
    if not mask.any():
        return
        
        
        
        

    sr = np.clip(sr * shade, 0, 255).astype(np.uint8)
    sg = np.clip(sg * shade, 0, 255).astype(np.uint8)
    sb = np.clip(sb * shade, 0, 255).astype(np.uint8)

    surf_rgb = pygame.surfarray.pixels3d(surf)
    surf_a   = pygame.surfarray.pixels_alpha(surf)

    ys, xs  = np.where(mask)
    sxs     = xs + min_x
    sys_    = ys + min_y

    surf_rgb[sxs, sys_, 0] = sr[ys, xs]
    surf_rgb[sxs, sys_, 1] = sg[ys, xs]
    surf_rgb[sxs, sys_, 2] = sb[ys, xs]
    surf_a[sxs, sys_]      = sa[ys, xs]

    del surf_rgb, surf_a, tex_arr, tex_alpha
    
    
    
    
    
    
    


"""
def _render_faceuv(surf, corners_3d, uv_corners, texture, shade, s):
    pts = [_iso_proj(*c, s) for c in corners_3d]
    pygame.draw.polygon(surf, (200, 200, 200), pts)
"""

_tex_tile_cache = {}










def get_text(i, atlas_surface):
    if i in _tex_tile_cache:
        return _tex_tile_cache[i]
        
    from world.blocks import TEXTURES
    
    uv = TEXTURES.get(i)
    if not uv:
        return None
        
        
    col, row = uv
    aw, ah   = atlas_surface.get_width(), atlas_surface.get_height()
    px, py   = col * 16, row * 16
    if px + 16 > aw or py + 16 > ah:
        return None
        
        
    tile = pygame.Surface((16, 16), pygame.SRCALPHA)
    tile.blit(atlas_surface, (0, 0), pygame.Rect(px, py, 16, 16))
    _tex_tile_cache[i] = tile
    
    return tile








def get_alltexts(blockId, atlas_surface):
    from world.blocks import BLOCK_FACES
    faces = BLOCK_FACES.get(blockId)
    if not faces: return None
    
    if isinstance(faces, str):
        tex = get_text(faces, atlas_surface)
        return [tex] * 6
        
    return [get_text(faces[i], atlas_surface) for i in range(6)]







def get_atlastextAt(atlas_surface, u_start, v_start):
    ck = (u_start, v_start)
    if ck in _tex_tile_cache:
        return _tex_tile_cache[ck]
        
        
    from world.blocks import UV_W, UV_H
    
    aw, ah = atlas_surface.get_width(), atlas_surface.get_height()
    px = round(u_start * aw)
    py = round((1.0 - v_start - UV_H) * ah)
    px = max(0, min(px, aw - 16))
    py = max(0, min(py, ah - 16))
    tile = pygame.Surface((16, 16), pygame.SRCALPHA)
    tile.blit(atlas_surface, (0, 0), pygame.Rect(px, py, 16, 16))
    _tex_tile_cache[ck] = tile
    
    return tile





def render3d_ok(blockId):
    from world.blocks import BLOCK_FACES
    if blockId not in BLOCK_FACES:
        return False

    from world.renderers.registry import CUSTOM_BLOCKS, MODE_FLAT, MODE_INVISIBLE

    if blockId not in CUSTOM_BLOCKS:
        return True

    mode, elements, *_ = CUSTOM_BLOCKS[blockId]
    if mode in (MODE_FLAT, MODE_INVISIBLE):
        return False

    from world import blocks as B
    _FLAT_BLOCKS = {
        B.SAPLING_OAK, B.SAPLING_SPRUCE, B.SAPLING_BIRCH, B.SAPLING_JUNGLE,
        B.SAPLING_ACACIA, B.SAPLING_DARK_OAK,
        B.DANDELION, B.POPPY, B.BLUE_ORCHID, B.ALLIUM, B.AZURE_BLUET,
        B.RED_TULIP, B.ORANGE_TULIP, B.WHITE_TULIP, B.PINK_TULIP, B.OXEYE_DAISY,
        B.BROWN_MUSHROOM, B.RED_MUSHROOM, B.DEAD_BUSH, B.FERN,
        B.SUNFLOWER, B.LILAC, B.DOUBLE_TALLGRASS, B.LARGE_FERN, B.ROSE_BUSH, B.PEONY,
        B.COBWEB, B.VINE, B.LILY_PAD, B.TALLGRASS,
        B.RAIL, B.POWERED_RAIL, B.POWERED_RAIL_ON, B.DETECTOR_RAIL, B.ACTIVATOR_RAIL,
        B.TORCH, B.REDSTONE_TORCH_OFF, B.REDSTONE_TORCH_ON,
        B.LEVER, B.TRIPWIRE_HOOK,
    }
    return blockId not in _FLAT_BLOCKS




def _face_uv_from_verts(fi, v0, v1, v2, v3):
    if   fi == _F_TOP:   return [(v0[0],     v0[2]), (v1[0],     v1[2]), (v2[0],     v2[2]), (v3[0],     v3[2])]
    elif fi == _F_BOT:   return [(v0[0],   1-v0[2]), (v1[0],   1-v1[2]), (v2[0],   1-v2[2]), (v3[0],   1-v3[2])]
    elif fi == _F_NORTH: return [(1-v0[0], 1-v0[1]), (1-v1[0], 1-v1[1]), (1-v2[0], 1-v2[1]), (1-v3[0], 1-v3[1])]
    elif fi == _F_SOUTH: return [(v0[0],   1-v0[1]), (v1[0],   1-v1[1]), (v2[0],   1-v2[1]), (v3[0],   1-v3[1])]
    elif fi == _F_EAST:  return [(1-v0[2], 1-v0[1]), (1-v1[2], 1-v1[1]), (1-v2[2], 1-v2[1]), (1-v3[2], 1-v3[1])]
    else:                return [(v0[2],   1-v0[1]), (v1[2],   1-v1[1]), (v2[2],   1-v2[1]), (v3[2],   1-v3[1])]




def _get_prismarine_ids():
    from world import blocks as B
    return {B.PRISMARINE, B.PRISMARINE_BRICKS, B.PRISMARINE_DARK}


_iso_cache   = {}
_FOLIAGE_CLR = (72, 181, 24)






def _tintsurf(surf, color):
    tinted  = surf.copy().convert_alpha()
    overlay = pygame.Surface(tinted.get_size(), pygame.SRCALPHA)
    overlay.fill((*color, 255))
    tinted.blit(overlay, (0, 0), special_flags=pygame.BLEND_RGB_MULT)
    return tinted





def renderiso(blockId, atlas_surface, size=16, foliage_tint=False, anim_frame=None):
    cbl = anim_frame is None
    key = (blockId, foliage_tint, size)
    if cbl and key in _iso_cache:
        return _iso_cache[key]

    base_tex = get_alltexts(blockId, atlas_surface)
    if not base_tex or not any(base_tex):
        return None

    if foliage_tint:
        from world.blocks import BLOCK_FACES
        faces_def = BLOCK_FACES.get(blockId)
        # grass type:= tuple with diff textures -> tint top only
        top_only = (
            isinstance(faces_def, (list, tuple)) 
            and len(faces_def) >= 4
            and faces_def[0] != faces_def[3]
        )
        
        base_tex = list(base_tex)
        if top_only:
            if base_tex[_F_TOP]:
                base_tex[_F_TOP] = _tintsurf(base_tex[_F_TOP], _FOLIAGE_CLR)
                
        else:
            for i in range(6):
                if base_tex[i]:
                    base_tex[i] = _tintsurf(base_tex[i], _FOLIAGE_CLR)

    
    
    
    
    
    if anim_frame is not None: base_tex = [anim_frame] * 6

    from world.renderers.registry import CUSTOM_BLOCKS, CUBE_ELEMS, BLOCK_DATA

    if blockId in CUSTOM_BLOCKS:
        _, elements, *_ = CUSTOM_BLOCKS[blockId]
    else:
        elements = CUBE_ELEMS

    mc_ftex  = BLOCK_DATA.get(blockId)
    surf     = pygame.Surface((size, size), pygame.SRCALPHA)
    flist    = []
    _fcount  = 0
    #print(blockId, size)
    
    
    

    for ei, elem in enumerate(elements):
        for fi in range(6):
            fverts = elem[fi]
            
            if abs(fverts.sum()) < 1e-6:
                continue
                
            if fi in _HIDDEN_FACES:
                continue
                

            v0 = fverts[0].tolist()
            v1 = fverts[1].tolist()
            v2 = fverts[2].tolist()
            v3 = fverts[5].tolist()
            

            cx = (v0[0] + v1[0] + v2[0] + v3[0]) * 0.25
            cy = (v0[1] + v1[1] + v2[1] + v3[1]) * 0.25
            cz = (v0[2] + v1[2] + v2[2] + v3[2]) * 0.25
            depth = _COS_P * (-_SIN_Y * cx + _COS_Y * cz) + _SIN_P * cy

            tex = None
            if mc_ftex and ei < len(mc_ftex) and mc_ftex[ei] is not None:
                ftx              = mc_ftex[ei]
                u_start, v_start = ftx[fi]
                if u_start >= 0 and v_start >= 0:
                    tex = get_atlastextAt(atlas_surface, u_start, v_start)
                    
                    
            if tex is None:
                tex = base_tex[fi]
                
            if tex is None:
                continue

            uvs   = _face_uv_from_verts(fi, v0, v1, v2, v3)
            shade = _FACE_SHADE[fi]
            flist.append((depth, fi, [v0, v1, v2, v3], uvs, tex, shade))
            
            

    flist.sort(key=lambda f: f[0])

    #flist.sort(key=lambda f: -f[0])

    for _, _, quad, uvs, tex, shade in flist:
        _render_faceuv(surf, quad, uvs, tex, shade, size)

    if cbl:
        _iso_cache[key] = surf
        
    return surf









def get_itemicon_anim(item_def, atlas_surface, items_atlas_surface, size=16):
    if not item_def:
        s = pygame.Surface((size, size), pygame.SRCALPHA)
        s.fill((255, 0, 255))
        return s

    foliage = item_def.foliage_tint
    anims    = getanims()
    n   = anims.blockanimtext(item_def.itemId) if item_def.is_block else None
    #print(item_def.itemId, foliage)
    

    # only prismarine
    _3D_ANIM = _get_prismarine_ids()
    if n and item_def.itemId not in _3D_ANIM:
        animated = anims.spritesurf(n, size)
        if animated:
            
            if foliage: animated = _tintsurf(animated, _FOLIAGE_CLR)
            return animated

    if item_def.is_block and render3d_ok(item_def.itemId):
        anim_frame = None
        if n and item_def.itemId in _3D_ANIM:
            anim_frame = anims.spritesurf(n, 16)
        iso = renderiso(
            item_def.itemId, atlas_surface, size,
            foliage_tint=foliage, anim_frame=anim_frame
        )
        
        if iso:
            return iso





    if n:
        animated = anims.spritesurf(n, size)
        if animated:
            if foliage: animated = _tintsurf(animated, _FOLIAGE_CLR)
            return animated
            
            

    col, row = item_def.texture_uv
    atlas    = item_def.atlas
    source   = atlas_surface if atlas == 'blocks' else items_atlas_surface
    

    if not source:
        s = pygame.Surface((size, size), pygame.SRCALPHA)
        s.fill((255, 0, 255))
        return s

    px, py = col * 16, row * 16
    aw, ah = source.get_width(), source.get_height()

    if px + 16 > aw or py + 16 > ah:
        s = pygame.Surface((size, size), pygame.SRCALPHA)
        s.fill((255, 0, 255))
        return s



    icon = source.subsurface(pygame.Rect(px, py, 16, 16))
    if foliage: icon = _tintsurf(icon, _FOLIAGE_CLR)
    if size != 16: return pygame.transform.scale(icon, (size, size))
    return icon.copy()


















