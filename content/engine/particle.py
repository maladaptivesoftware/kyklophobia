import numpy as np
import moderngl
import random
import math
import shaders
from config import (
    PART_MAXCOUNT, PART_PERBLOCK, PART_LF_MIN, PART_LF_MAX,
    PART_SZ_MIN, PART_SZ_MAX, PART_SPEED, PART_G
)




class Particle:
    def __init__(self):
        self.active  = False
        self.pos     = np.zeros(3, dtype='f4')
        self.vel     = np.zeros(3, dtype='f4')
        self.life    = 0.0
        self.maxlife = 1.0
        self.size    = 0.1
        self.uvoff   = (0.0, 0.0)
        self.gravity = -9.8
        self.tint    = (1.0, 1.0, 1.0)


class ParticleManager:
    BLOCK_UV_MAP = {
        1:  (0, 0), 2:  (2, 0), 3:  (3, 0), 4:  (1, 1), 5:  (0, 0),
        6:  (0, 1), 7:  (3, 1), 8:  (0, 2), 9:  (1, 2), 10: (2, 2),
        11: (3, 2), 12: (4, 0), 13: (4, 1), 14: (4, 2), 20: (2, 1),
    }

    ATLAS_COLS       = 10
    ATLAS_ROWS       = 10
    TILE_SIZE        = 16
    ATLAS_SIZE       = 160
    PARTICLE_SUBTILE  = 4
    SUBTILES_PER_TILE = 4

    TINT_MAP = {
        1:  (0.47, 0.75, 0.35),   # grass
        2:  (0.55, 0.38, 0.28),   # dirt
        3:  (0.60, 0.60, 0.60),   # stone
        4:  (0.30, 0.30, 0.30),   # bedrock
        5:  (0.20, 0.40, 0.80),   # water
        6:  (0.86, 0.78, 0.50),   # sand
        7:  (0.40, 0.30, 0.20),   # log
        8:  (0.28, 0.70, 0.09),   # oak leaves
        9:  (0.38, 0.60, 0.38),   # spruce leaves
        10: (0.47, 0.75, 0.35),   # tall grass
        11: (0.65, 0.65, 0.70),   # andesite
        12: (0.50, 0.50, 0.50),   # cobblestone
        13: (0.45, 0.35, 0.30),   # coarse dirt
        14: (0.86, 0.75, 0.55),   # sandstone
        20: (0.90, 0.95, 1.00),   # glass
    }
    # TODO use get(block) -> texture

    def __init__(self, ctx, maxp=PART_MAXCOUNT, texture=None):
        self.ctx     = ctx
        self.maxp    = maxp
        self.texture = texture

        self.particles = [Particle() for _ in range(maxp)]
        self.acount    = 0
        self.pidx      = 0

        self.prog = shaders.prog(ctx, "particle.vert", "particle.frag")

        vsz      = 12
        vprt     = 6
        buf_size = maxp * vprt * vsz

        self.vsz      = vsz
        self.vprt     = vprt
        self.vertdata = np.zeros(buf_size, dtype='f4')
        self.vbo      = ctx.buffer(reserve=buf_size * 4)
        self.vao      = ctx.vertex_array(
            self.prog,
            [(
                self.vbo, 
                '3f 2f 2f 1f 1f 3f', 
                'in_pos',  'in_offset', 
                'in_uv',   'in_alpha', 
                'in_size', 'in_tint'
            )]
        )
        
        

        self.quadoffs = np.array([
            [-0.5, -0.5], [0.5, -0.5], [0.5,  0.5],
            [-0.5, -0.5], [0.5,  0.5], [-0.5, 0.5],
        ], dtype='f4')
        
        

        uv_sz = self.PARTICLE_SUBTILE / self.ATLAS_SIZE
        self.quaduvs = np.array([
            [0.0,   uv_sz], [uv_sz, uv_sz], [uv_sz, 0.0],
            [0.0,   uv_sz], [uv_sz, 0.0],   [0.0,   0.0],
        ], dtype='f4')

        self.worldup  = np.array([0.0, 1.0, 0.0], dtype='f4')
        self._last_count = 0
        
        
        
        
        
        
        

    def spawn(self, x, y, z, btype):
        btype = btype & 0x3FF   # strip state bits

        if btype == 0 or btype >= 512:   # skip air && item ids
            return

        subuv = self.PARTICLE_SUBTILE / self.ATLAS_SIZE
        tint  = self.TINT_MAP.get(btype, (0.6, 0.6, 0.6))

        for _ in range(PART_PERBLOCK):
            p = self.particles[self.pidx]

            if not p.active: self.acount += 1
            #print(self.acount, self.pidx)

            p.active  = True
            p.pos[0]  = x + 0.5 + (random.random() - 0.5) * 0.8
            p.pos[1]  = y + 0.5 + (random.random() - 0.5) * 0.8
            p.pos[2]  = z + 0.5 + (random.random() - 0.5) * 0.8
            
            

            angle = random.random() * math.pi * 2
            pitch = random.random() * math.pi * 0.5
            spd   = PART_SPEED * (0.5 + random.random() * 0.5)

            p.vel[0]  = math.cos(angle) * math.cos(pitch) * spd
            p.vel[1]  = math.sin(pitch) * spd + 2.0
            p.vel[2]  = math.sin(angle) * math.cos(pitch) * spd

            p.life    = random.uniform(PART_LF_MIN, PART_LF_MAX)
            p.maxlife = p.life
            p.size    = random.uniform(PART_SZ_MIN, PART_SZ_MAX)
            
            

            shade  = random.uniform(0.85, 1.0)
            p.tint = (tint[0] * shade, tint[1] * shade, tint[2] * shade)

            sx     = random.randint(0, self.SUBTILES_PER_TILE - 1)
            sy     = random.randint(0, self.SUBTILES_PER_TILE - 1)
            p.uvoff   = (sx * subuv, sy * subuv)
            p.gravity = PART_G

            self.pidx = (self.pidx + 1) % self.maxp  # ring buffer
            
            
            
            
            

    def update(self, dt):
        for i in self.particles:
            if not i.active: continue
            i.vel[1] += i.gravity * dt
            i.pos    += i.vel * dt
            i.life   -= dt
            if i.life <= 0:
                i.active = False
                self.acount = max(0, self.acount - 1)
                
                
                
                
                

    def render(self, mvp, cam_front, cam_pos):
        if self.acount == 0: return

        # billboard basis -> right = front * up, up = right * front
        cam_r = np.cross(cam_front, self.worldup)
        cam_r /= np.linalg.norm(cam_r)
        cam_u  = np.cross(cam_r, cam_front)
        cam_u /= np.linalg.norm(cam_u)

        vi = 0
        for i in self.particles:
            if not i.active: continue
            alpha = max(0.0, min(1.0, i.life / i.maxlife))
            for j in range(self.vprt):
                b = vi * self.vsz
                self.vertdata[b:b+3]   = i.pos
                self.vertdata[b+3:b+5] = self.quadoffs[j]
                self.vertdata[b+5]     = i.uvoff[0] + self.quaduvs[j, 0]
                self.vertdata[b+6]     = i.uvoff[1] + self.quaduvs[j, 1]
                self.vertdata[b+7]     = alpha
                self.vertdata[b+8]     = i.size
                self.vertdata[b+9:b+12] = i.tint
                vi += 1
                
                
                

        self.vbo.write(self.vertdata[:vi * self.vsz].tobytes())

        self.prog['mvp'].write(mvp.astype('f4').tobytes())
        self.prog['cam_r'].write(cam_r.astype('f4').tobytes())
        self.prog['cam_u'].write(cam_u.astype('f4').tobytes())
        

        if self.texture:
            self.texture.use(0)
            self.prog['texture0'].value = 0
            
            

        self.ctx.enable(moderngl.BLEND)
        self.ctx.blend_func  = moderngl.SRC_ALPHA, moderngl.ONE_MINUS_SRC_ALPHA
        self.ctx.depth_mask  = False

        self.vao.render(moderngl.TRIANGLES, vertices=vi)

        self.ctx.depth_mask = True
        self.ctx.disable(moderngl.BLEND)
        
        
        
        
        
        

    """
    def update(self, dt):
        for i in self.particles:
            if not i.active: continue
            i.vel[1] += PART_G * dt
            i.pos    += i.vel * dt
            i.life   -= dt
            if i.life <= 0: i.active = False
    """

    def clear(self):
        for i in self.particles: i.active = False
        self.acount = 0

    def release(self):
        self.vbo.release()
        self.vao.release()
        self.prog.release()
