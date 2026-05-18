import numpy as np
import moderngl
import pygame
import os
import shaders
import _respath

from world.blocks import TEXTURES, REDSTONE_WIRE


class ExtrudedRenderer:
    def __init__(self, ctx):
        self.ctx   = ctx
        self.bpos  = {}   # btype -> list (x, y, z)
        self.bvaos = {}   # btype -> {vbo, uvvbo, nvbo, vcount, tint, vao, ivbo}
        self.tex   = None
        self.dirty = {}

        self.loadshader()
        self.loadatlas()
        self.buildbase()

    def loadshader(self):
        self.prog = shaders.prog(self.ctx, "extruded.vert", "extruded.frag")
        
        

    def loadatlas(self):
        img      = pygame.image.load(_respath.atlas_block())
        imgd     = pygame.image.tostring(img, 'RGBA', True)
        self.tex = self.ctx.texture(img.get_size(), 4, imgd)
        self.tex.filter = (moderngl.NEAREST, moderngl.NEAREST)
        self.atlas = img
        self.atw   = img.get_width()  // 16
        self.ath   = img.get_height() // 16
        
        

    def extrudedgeom(self, n, depth=0.0625):
        if n not in TEXTURES:
            return None

        col, row = TEXTURES[n]
        px, py   = col * 16, row * 16

        eps  = 0.0001
        u0   = col / self.atw + eps;       u1 = (col + 1) / self.atw - eps
        v0   = 1.0 - (row + 1) / self.ath + eps; v1 = 1.0 - row / self.ath - eps

        j    = depth
        pix  = 1.0 / 16.0
        pu   = (u1 - u0) / 16.0
        pv   = (v1 - v0) / 16.0

        def is_opaque(tx, ty):
            if tx < 0 or tx >= 16 or ty < 0 or ty >= 16:
                return False
                
            c = self.atlas.get_at((px + tx, py + ty))
            return c[3] > 128 if len(c) > 3 else True
            
            

        verts = []; uvs = []; norms = []

        # top
        verts.extend([[0.0,j,0.0],[0.0,j,1.0],[1.0,j,1.0],[0.0,j,0.0],[1.0,j,1.0],[1.0,j,0.0]])
        uvs.extend([[u0,v1],[u0,v0],[u1,v0],[u0,v1],[u1,v0],[u1,v1]])
        norms.extend([[0,1,0]]*6)

        # bot
        verts.extend([[0.0,0.0,0.0],[1.0,0.0,0.0],[1.0,0.0,1.0],[0.0,0.0,0.0],[1.0,0.0,1.0],[0.0,0.0,1.0]])
        uvs.extend([[u0,v1],[u1,v1],[u1,v0],[u0,v1],[u1,v0],[u0,v0]])
        norms.extend([[0,-1,0]]*6)
        
        

        for ty in range(16):
            for tx in range(16):
                if not is_opaque(tx, ty):
                    continue

                ovlp = 0.001
                x0 = max(0, tx * pix - ovlp);      x1 = min(1, (tx+1) * pix + ovlp)
                z0 = max(0, ty * pix - ovlp);      z1 = min(1, (ty+1) * pix + ovlp)
                puc = u0 + (tx + 0.5) * pu
                pvc = v1 - (ty + 0.5) * pv  # v decrease top->bottom
                
                

                if not is_opaque(tx+1, ty):
                    verts.extend([[x1,0.0,z0],[x1,0.0,z1],[x1,j,z1],[x1,0.0,z0],[x1,j,z1],[x1,j,z0]])
                    uvs.extend([[puc,pvc]]*6); norms.extend([[1,0,0]]*6)
                if not is_opaque(tx-1, ty):
                    verts.extend([[x0,0.0,z1],[x0,0.0,z0],[x0,j,z0],[x0,0.0,z1],[x0,j,z0],[x0,j,z1]])
                    uvs.extend([[puc,pvc]]*6); norms.extend([[-1,0,0]]*6)
                if not is_opaque(tx, ty+1):
                    verts.extend([[x0,0.0,z1],[x1,0.0,z1],[x1,j,z1],[x0,0.0,z1],[x1,j,z1],[x0,j,z1]])
                    uvs.extend([[puc,pvc]]*6); norms.extend([[0,0,1]]*6)
                if not is_opaque(tx, ty-1):
                    verts.extend([[x1,0.0,z0],[x0,0.0,z0],[x0,j,z0],[x1,0.0,z0],[x0,j,z0],[x1,j,z0]])
                    uvs.extend([[puc,pvc]]*6); norms.extend([[0,0,-1]]*6)

        if not verts:
            return None
            

        vbo   = self.ctx.buffer(np.array(verts, dtype='f4').tobytes())
        uvvbo = self.ctx.buffer(np.array(uvs,   dtype='f4').tobytes())
        nvbo  = self.ctx.buffer(np.array(norms, dtype='f4').tobytes())
        return vbo, uvvbo, nvbo, len(verts)

    def flatgeom(self, n, height=0.01):
        if n not in TEXTURES: return None
        

        col, row = TEXTURES[n]
        eps  = 0.0001
        u0   = col / self.atw + eps;            u1 = (col + 1) / self.atw - eps
        v0   = 1.0 - (row + 1) / self.ath + eps; v1 = 1.0 - row / self.ath - eps

        h     = height
        verts = [[0.0,h,0.0],[0.0,h,1.0],[1.0,h,1.0],[0.0,h,0.0],[1.0,h,1.0],[1.0,h,0.0]]
        uvs   = [[u0,v1],[u0,v0],[u1,v0],[u0,v1],[u1,v0],[u1,v1]]
        norms = [[0,1,0]] * 6

        vbo   = self.ctx.buffer(np.array(verts, dtype='f4').tobytes())
        uvvbo = self.ctx.buffer(np.array(uvs,   dtype='f4').tobytes())
        nvbo  = self.ctx.buffer(np.array(norms, dtype='f4').tobytes())
        return vbo, uvvbo, nvbo, len(verts)
        
        
        
        
        

    def buildbase(self):
        ecfgs = {}
        fcfgs = {}

        for i, (n, tint) in ecfgs.items():
            result = self.extrudedgeom(n)
            if result:
                vbo, uvvbo, nvbo, vc = result
                self.bvaos[i] = {
                    'vbo': vbo, 'uvvbo': uvvbo, 'nvbo': nvbo,
                    'vcount': vc, 'tint': tint, 'vao': None, 'ivbo': None
                }
                self.bpos[i]  = []
                self.dirty[i] = True

        for i, (n, tint) in fcfgs.items():
            result = self.flatgeom(n)
            if result:
                vbo, uvvbo, nvbo, vc = result
                self.bvaos[i] = {
                    'vbo': vbo, 'uvvbo': uvvbo, 'nvbo': nvbo,
                    'vcount': vc, 'tint': tint, 'vao': None, 'ivbo': None
                }
                self.bpos[i]  = []
                self.dirty[i] = True
                
                
                

    def rebuildibuf(self, btype):
        if btype not in self.bvaos:
            return

        data = self.bvaos[btype]
        pos  = self.bpos.get(btype, [])

        if data['vao']:  data['vao'].release();  data['vao']  = None
        if data['ivbo']: data['ivbo'].release(); data['ivbo'] = None

        if not pos:
            return

        idata        = np.array(pos, dtype='f4')
        data['ivbo'] = self.ctx.buffer(idata.tobytes())
        data['vao']  = self.ctx.vertex_array(self.prog, [
            (data['vbo'],   '3f',   'in_pos'),
            (data['uvvbo'], '2f',   'in_uv'),
            (data['nvbo'],  '3f',   'in_norm'),
            (data['ivbo'],  '3f/i', 'instance_pos'),
        ])
        self.dirty[btype] = False



    def add_block(self, x, y, z, btype):
        if btype not in self.bpos:
            return
        p = (float(x), float(y), float(z))
        if p not in self.bpos[btype]:
            self.bpos[btype].append(p)
            self.dirty[btype] = True



    def rm_block(self, x, y, z):
        p = (float(x), float(y), float(z))
        for i in self.bpos:
            if p in self.bpos[i]:
                self.bpos[i].remove(p)
                self.dirty[i] = True
                break



    def clear_chunk(self, chunk_x, chunk_z):
        ox, oz = chunk_x * 16, chunk_z * 16
        for i in self.bpos:
            old = self.bpos[i]
            new = [(x,y,z) for x,y,z in old if not (ox <= x < ox+16 and oz <= z < oz+16)]
            if len(new) != len(old):
                self.bpos[i]  = new
                self.dirty[i] = True





    def render(self, mvp, ambient=0.3):
        if not self.bvaos:
            return

        for i in self.dirty:
            if self.dirty[i]:
                self.rebuildibuf(i)

        if not any(len(self.bpos.get(i, [])) > 0 for i in self.bvaos):
            return

        self.ctx.disable(moderngl.CULL_FACE)
        self.tex.use(0)
        self.prog['tex']     = 0
        self.prog['ambient'] = ambient
        self.prog['mvp'].write(mvp.astype('f4').tobytes())

        for i, j in self.bvaos.items():
            if not j['vao']:
                continue
            n = len(self.bpos.get(i, []))
            if n == 0:
                continue
            self.prog['tint'] = j['tint']
            j['vao'].render(moderngl.TRIANGLES, instances=n)

        self.ctx.enable(moderngl.CULL_FACE)

    def cleanup(self):
        for j in self.bvaos.values():
            if j['vao']:  j['vao'].release()
            if j['ivbo']: j['ivbo'].release()
            j['vbo'].release()
            j['uvvbo'].release()
            j['nvbo'].release()
        if self.tex:
            self.tex.release()
