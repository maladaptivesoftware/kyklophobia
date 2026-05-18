import numpy as np
import json
import os
import math
import _respath

from world.blocks import TEXTURES, UV_W, UV_H


MODELS_DIR = os.path.join(os.path.dirname(__file__), "models")
JSONS_DIR  = None
MAX_ELEMS  = 48
MAX_CUSTOM = 512
FACE_MAP   = {"up": 0, "down": 1, "north": 2, "south": 3, "east": 4, "west": 5}


def atlasuv(n):
    nm = n.replace("blocks/", "")
    if nm in TEXTURES:
        col, row = TEXTURES[nm]
        u0 = col * UV_W
        v0 = 1.0 - (row + 1) * UV_H
        return (u0, v0)
    return None


def resolvtex(ref, textures):
    visited = set()
    while ref.startswith("#"):
        key = ref[1:]
        if key in visited or key not in textures:
            return ""
        visited.add(key)
        ref = textures[key]
    return ref


def faceuv8(nu1, nv1, nu2, nv2, rot=0):
    if rot == 90:    return [nu1, 1-nv1, nu1, 1-nv2, nu2, 1-nv2, nu2, 1-nv1]
    elif rot == 180: return [nu2, 1-nv1, nu1, 1-nv1, nu1, 1-nv2, nu2, 1-nv2]
    elif rot == 270: return [nu2, 1-nv2, nu2, 1-nv1, nu1, 1-nv1, nu1, 1-nv2]
    else:            return [nu1, 1-nv2, nu2, 1-nv2, nu2, 1-nv1, nu1, 1-nv1]


def rotelem(faces, origin, axis, adeg, rescale=False):
    # rescale=True: expand rotated axes by 1/cos to fill full extent (cross/flower models)
    angle = math.radians(adeg)
    ca = math.cos(angle)
    sa = math.sin(angle)
    scale = (1.0 / abs(ca)) if (rescale and abs(ca) > 1e-6) else 1.0
    ox, oy, oz = origin[0]/16.0, origin[1]/16.0, origin[2]/16.0
    for fi in range(6):
        for vi in range(6):
            dx = faces[fi, vi, 0] - ox
            dy = faces[fi, vi, 1] - oy
            dz = faces[fi, vi, 2] - oz
            if axis == "x":
                ndy = (dy * ca - dz * sa) * scale
                ndz = (dy * sa + dz * ca) * scale
                faces[fi, vi, 1] = oy + ndy
                faces[fi, vi, 2] = oz + ndz
            elif axis == "y":
                ndx = (dx * ca + dz * sa) * scale
                ndz = (-dx * sa + dz * ca) * scale
                faces[fi, vi, 0] = ox + ndx
                faces[fi, vi, 2] = oz + ndz
            elif axis == "z":
                ndx = (dx * ca - dy * sa) * scale
                ndy = (dx * sa + dy * ca) * scale
                faces[fi, vi, 0] = ox + ndx
                faces[fi, vi, 1] = oy + ndy


def modelsdir():
    global JSONS_DIR
    if JSONS_DIR is None:
        JSONS_DIR = _respath.dir_model()
    return JSONS_DIR


def load_json(modelname):
    path = os.path.join(modelsdir(), f"{modelname}.json")
    if not os.path.exists(path):
        return None
    with open(path, "r") as f:
        data = json.load(f)
    if "parent" in data:
        pname  = data["parent"].replace("block/", "")
        parent = load_json(pname)
        if parent:
            merged = dict(parent.get("textures", {}))
            merged.update(data.get("textures", {}))
            data["textures"] = merged
            if "elements" not in data:
                data["elements"] = parent.get("elements", [])
    return data


def elemfaces(fc, tc):
    x0, y0, z0 = fc[0] / 16.0, fc[1] / 16.0, fc[2] / 16.0
    x1, y1, z1 = tc[0] / 16.0, tc[1] / 16.0, tc[2] / 16.0

    faces = np.array([
        [[x0, y1, z1], [x1, y1, z1], [x1, y1, z0], [x0, y1, z1], [x1, y1, z0], [x0, y1, z0]],
        [[x0, y0, z0], [x1, y0, z0], [x1, y0, z1], [x0, y0, z0], [x1, y0, z1], [x0, y0, z1]],
        [[x1, y0, z0], [x0, y0, z0], [x0, y1, z0], [x1, y0, z0], [x0, y1, z0], [x1, y1, z0]],
        [[x0, y0, z1], [x1, y0, z1], [x1, y1, z1], [x0, y0, z1], [x1, y1, z1], [x0, y1, z1]],
        [[x1, y0, z1], [x1, y0, z0], [x1, y1, z0], [x1, y0, z1], [x1, y1, z0], [x1, y1, z1]],
        [[x0, y0, z0], [x0, y0, z1], [x0, y1, z1], [x0, y0, z0], [x0, y1, z1], [x0, y1, z0]],
    ], dtype=np.float32)

    return faces


def modeljson(modelname, etx=None):
    data = load_json(modelname)
    if not data:
        return None
    textures = data.get("textures", {})
    if etx:
        textures.update(etx)

    elm = []
    fuvs     = []
    ftex     = []

    for i in data.get("elements", []):
        fc    = i["from"]
        tc    = i["to"]
        faces = elemfaces(fc, tc)

        rot = i.get("rotation")
        if rot:
            rotelem(
                faces, 
                rot["origin"], rot["axis"], rot["angle"], 
                rot.get("rescale", False)
            )

        efuvs  = np.zeros((6, 8), dtype=np.float32)
        facetex  = np.full((6, 2), -1.0, dtype=np.float32)
        dfaces = set()
        
        

        for fn, j in i.get("faces", {}).items():
            fi = FACE_MAP.get(fn, -1)
            if fi < 0:
                continue
                
                
            dfaces.add(fi)

            uv   = j.get("uv", [0, 0, 16, 16])
            rot2 = j.get("rotation", 0)
            nu1, nv1, nu2, nv2 = uv[0]/16.0, uv[1]/16.0, uv[2]/16.0, uv[3]/16.0
            efuvs[fi] = faceuv8(nu1, nv1, nu2, nv2, rot2)

            tref = j.get("texture", "")
            if tref:
                n = resolvtex(tref, textures)
                if n:
                    atlas = atlasuv(n)
                    if atlas:
                        facetex[fi] = atlas
                        
                        

        for fi in range(6):
            if fi not in dfaces:
                faces[fi, :, :] = 0.0

        elm.append(faces)
        fuvs.append(efuvs)
        ftex.append(facetex)

    return elm, fuvs, ftex


def load_model(nm):
    path = os.path.join(MODELS_DIR, f"{nm}.json")
    if not os.path.exists(path):
        return [elemfaces([0, 0, 0], [16, 16, 16])], UV_MODE_POS, False, None
        
        

    with open(path, "r") as f:
        data = json.load(f)

    uvm = UV_MODE_IDX if data.get("uv_mode") == "index" else UV_MODE_POS
    ctb = data.get("cull_topbot", False)
    

    if data.get("format") == "vertices":
        ford  = ["top", "bottom", "north", "south", "east", "west"]
        faces = np.zeros((6, 6, 3), dtype=np.float32)
        for i, fn in enumerate(ford):
            if fn in data.get("faces", {}):
                verts = data["faces"][fn]
                for j, v in enumerate(verts):
                    faces[i, j, 0] = v[0]
                    faces[i, j, 1] = v[1]
                    faces[i, j, 2] = v[2]
                    
                    
        return [faces], uvm, ctb, None
        
        

    relms  = data.get("elements", [])
    ismfmt = any("faces" in i for i in relms)

    elm = []
    fuvs     = []

    for i in relms:
        fc    = i["from"]
        tc    = i["to"]
        faces = elemfaces(fc, tc)

        if ismfmt and "faces" in i:
            efuvs  = np.zeros((6, 8), dtype=np.float32)
            dfaces = set()

            for fn, j in i["faces"].items():
                fi = FACE_MAP.get(fn, -1)
                if fi < 0:
                    continue
                dfaces.add(fi)
                uv = j.get("uv", [0, 0, 16, 16])
                nu1, nv1, nu2, nv2 = uv[0]/16.0, uv[1]/16.0, uv[2]/16.0, uv[3]/16.0
                efuvs[fi] = faceuv8(nu1, nv1, nu2, nv2)
                
                

            for fi in range(6):
                if fi not in dfaces:
                    faces[fi, :, :] = 0.0

            fuvs.append(efuvs)
            
            
        else:
            fuvs.append(None)

        elm.append(faces)
        
        
        
        
        
        

    if not elm:
        return [elemfaces([0, 0, 0], [16, 16, 16])], uvm, ctb, None

    hf = data.get("hide_faces", [])
    
    
    if hf:
        for i in elm:
            for fi in hf:
                if 0 <= fi < 6:
                    i[fi, :, :] = 0.0
                    

    if ismfmt:
        uvm = UV_MODE_MODEL
        return elm, uvm, ctb, fuvs
        
        

    return elm, uvm, ctb, None








def flattenelems(elm):
    n      = len(elm)
    result = np.zeros((MAX_ELEMS, 6, 6, 3), dtype=np.float32)
    for i, elem in enumerate(elm[:MAX_ELEMS]):
        result[i] = elem
        
        
    return n, result






def extrflat(n, depth=0.0625):
    
    import pygame

    atlas = pygame.image.load(_respath.atlas_block())

    if n not in TEXTURES:
        return [elemfaces([0, 0, 0], [16, 1, 16])]

    col, row = TEXTURES[n]
    px, py   = col * 16, row * 16
    atw      = atlas.get_width()  // 16
    ath      = atlas.get_height() // 16

    u0 = col / atw;             u1 = (col + 1) / atw
    v0 = 1.0 - (row + 1) / ath; v1 = 1.0 - row / ath

    d   = depth
    pix = 1.0 / 16.0
    
    

    def is_opaque(tx, ty):
        if tx < 0 or tx >= 16 or ty < 0 or ty >= 16:
            return False
            
        c = atlas.get_at((px + tx, py + ty))
        return c[3] > 128 if len(c) > 3 else True
        
        
        

    verts = []

    verts.extend([   # top
        [0.0, d, 0.0], [1.0, d, 0.0], [1.0, d, 1.0],
        [0.0, d, 0.0], [1.0, d, 1.0], [0.0, d, 1.0]
    ])
    verts.extend([   # bot
        [1.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 1.0],
        [1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 1.0]
    ])
    
    

    # tx=0 := left (x=0), ty=0 := img top (z=0)
    for ty in range(16):
        for tx in range(16):
            if not is_opaque(tx, ty):
                continue
            x0 = tx * pix;  x1 = x0 + pix
            z0 = ty * pix;  z1 = z0 + pix

            if not is_opaque(tx + 1, ty): verts.extend([[x1,0.0,z0],[x1,0.0,z1],[x1,d,z1],[x1,0.0,z0],[x1,d,z1],[x1,d,z0]])
            if not is_opaque(tx - 1, ty): verts.extend([[x0,0.0,z1],[x0,0.0,z0],[x0,d,z0],[x0,0.0,z1],[x0,d,z0],[x0,d,z1]])
            if not is_opaque(tx, ty + 1): verts.extend([[x0,0.0,z1],[x1,0.0,z1],[x1,d,z1],[x0,0.0,z1],[x1,d,z1],[x0,d,z1]])
            if not is_opaque(tx, ty - 1): verts.extend([[x1,0.0,z0],[x0,0.0,z0],[x0,d,z0],[x1,0.0,z0],[x0,d,z0],[x1,d,z0]])

    if not verts:
        return [elemfaces([0, 0, 0], [16, 1, 16])]

    elm = []
    nv = len(verts)
    for s in range(0, nv, 36):
        e     = min(s + 36, nv)
        faces = np.zeros((6, 6, 3), dtype=np.float32)
        vi    = 0
        for v in range(s, e):
            fi = vi // 6;  li = vi % 6
            if fi < 6:
                faces[fi, li] = verts[v]
            vi += 1
        elm.append(faces)

    return elm if elm else [elemfaces([0, 0, 0], [16, 1, 16])]




UV_MODE_POS = 0
UV_MODE_IDX = 1
UV_MODE_MODEL = 2
