import numpy as np


# build extruded geometry from img
def bake_extrudedgeom(image, col, row, tsz=16, depth=0.0625):
    px, py   = col * tsz, row * tsz
    acols    = image.get_width()  // tsz
    arows    = image.get_height() // tsz

    u0 = col / acols
    u1 = (col + 1) / acols
    v0 = 1.0 - (row + 1) / arows
    v1 = 1.0 - row / arows

    
    h    = 0.5
    d    = depth / 2.0
    yoff = d
    pix  = 1.0 / tsz
    pu   = (u1 - u0) / tsz
    pv   = (v1 - v0) / tsz

    verts = []
    uvs   = []
    norms = []
    
    
    

    # top
    verts.extend([
        [-h, yoff + d, -h], [h, yoff + d, -h], [h, yoff + d, h],
        [-h, yoff + d, -h], [h, yoff + d, h], [-h, yoff + d, h]
    ])
    uvs.extend([
        [u0, v0], [u1, v0], [u1, v1],
        [u0, v0], [u1, v1], [u0, v1]
    ])
    norms.extend([[0, 1, 0]] * 6)

    # bot
    verts.extend([
        [h, yoff - d, -h], [-h, yoff - d, -h], [-h, yoff - d, h],
        [h, yoff - d, -h], [-h, yoff - d, h], [h, yoff - d, h]
    ])
    uvs.extend([
        [u1, v0], [u0, v0], [u0, v1],
        [u1, v0], [u0, v1], [u1, v1]
    ])
    norms.extend([[0, -1, 0]] * 6)
    
    
    
    
    

    def is_opaque(tx, ty):
        if tx < 0 or tx >= tsz or ty < 0 or ty >= tsz:
            return False
        c = image.get_at((px + tx, py + ty))
        return c[3] > 128

    for ty in range(tsz):
        for tx in range(tsz):
            if not is_opaque(tx, ty):
                continue

            # tx=0 := left (-h), ty=0 := img top (-Z in model)
            x0 = -h + tx * pix;  x1 = x0 + pix
            z0 = -h + ty * pix;  z1 = z0 + pix

            pu0 = u0 + tx * pu;      pu1 = pu0 + pu
            pv0 = v1 - (ty + 1) * pv; pv1 = pv0 + pv

            if not is_opaque(tx + 1, ty):  # +x r
                verts.extend([
                    [x1, yoff - d, z0], [x1, yoff - d, z1], [x1, yoff + d, z1],
                    [x1, yoff - d, z0], [x1, yoff + d, z1], [x1, yoff + d, z0]
                ])
                uvs.extend([[pu1, pv0], [pu1, pv0], [pu1, pv1], [pu1, pv0], [pu1, pv1], [pu1, pv1]])
                norms.extend([[1, 0, 0]] * 6)

            if not is_opaque(tx - 1, ty):  # -x l
                verts.extend([
                    [x0, yoff - d, z1], [x0, yoff - d, z0], [x0, yoff + d, z0],
                    [x0, yoff - d, z1], [x0, yoff + d, z0], [x0, yoff + d, z1]
                ])
                uvs.extend([[pu0, pv0], [pu0, pv0], [pu0, pv1], [pu0, pv0], [pu0, pv1], [pu0, pv1]])
                norms.extend([[-1, 0, 0]] * 6)

            if not is_opaque(tx, ty + 1):  # +z s
                verts.extend([
                    [x0, yoff - d, z1], [x1, yoff - d, z1], [x1, yoff + d, z1],
                    [x0, yoff - d, z1], [x1, yoff + d, z1], [x0, yoff + d, z1]
                ])
                uvs.extend([[pu0, pv0], [pu1, pv0], [pu1, pv1], [pu0, pv0], [pu1, pv1], [pu0, pv1]])
                norms.extend([[0, 0, 1]] * 6)

            if not is_opaque(tx, ty - 1):  # -z n
                verts.extend([
                    [x1, yoff - d, z0], [x0, yoff - d, z0], [x0, yoff + d, z0],
                    [x1, yoff - d, z0], [x0, yoff + d, z0], [x1, yoff + d, z0]
                ])
                uvs.extend([[pu1, pv0], [pu0, pv0], [pu0, pv1], [pu1, pv0], [pu0, pv1], [pu1, pv1]])
                norms.extend([[0, 0, -1]] * 6)

    if not verts:
        return None

    return (
        np.array(verts, dtype=np.float32),
        np.array(uvs,   dtype=np.float32),
        np.array(norms, dtype=np.float32)
    )





# build flat extruded faces
def bake_extrudedflat(depth=0.0625):
    # tpnsew
    h     = 0.5
    d     = depth / 2.0
    ybase = d

    faces = np.zeros((6, 6, 3), dtype=np.float32)

    faces[0] = [  # +y top
        [-h+0.5, ybase+d, -h+0.5], [h+0.5, ybase+d, -h+0.5], [h+0.5, ybase+d, h+0.5],
        [-h+0.5, ybase+d, -h+0.5], [h+0.5, ybase+d, h+0.5],  [-h+0.5, ybase+d, h+0.5]
    ]
    faces[1] = [  # -y bot
        [h+0.5, ybase-d, -h+0.5], [-h+0.5, ybase-d, -h+0.5], [-h+0.5, ybase-d, h+0.5],
        [h+0.5, ybase-d, -h+0.5], [-h+0.5, ybase-d, h+0.5],  [h+0.5, ybase-d, h+0.5]
    ]
    faces[2] = [  # -z n
        [h+0.5, ybase-d, -h+0.5], [-h+0.5, ybase-d, -h+0.5], [-h+0.5, ybase+d, -h+0.5],
        [h+0.5, ybase-d, -h+0.5], [-h+0.5, ybase+d, -h+0.5], [h+0.5, ybase+d, -h+0.5]
    ]
    faces[3] = [  # +z s
        [-h+0.5, ybase-d, h+0.5], [h+0.5, ybase-d, h+0.5], [h+0.5, ybase+d, h+0.5],
        [-h+0.5, ybase-d, h+0.5], [h+0.5, ybase+d, h+0.5],  [-h+0.5, ybase+d, h+0.5]
    ]
    faces[4] = [  # +x e
        [h+0.5, ybase-d, h+0.5], [h+0.5, ybase-d, -h+0.5], [h+0.5, ybase+d, -h+0.5],
        [h+0.5, ybase-d, h+0.5], [h+0.5, ybase+d, -h+0.5], [h+0.5, ybase+d, h+0.5]
    ]
    faces[5] = [  # -x w
        [-h+0.5, ybase-d, -h+0.5], [-h+0.5, ybase-d, h+0.5], [-h+0.5, ybase+d, h+0.5],
        [-h+0.5, ybase-d, -h+0.5], [-h+0.5, ybase+d, h+0.5], [-h+0.5, ybase+d, -h+0.5]
    ]

    return [faces]
