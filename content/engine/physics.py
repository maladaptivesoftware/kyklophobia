import numpy as np
import math
from config import (
    P_W, P_H, P_EYE_H, P_EYE_F,
    GRAVITY, TERM_V, JUMP_V,
    MAX_GSPEED, MAX_FSPEED, MP_SPRINT,
    FL_SPEED, FL_SPEED_MP,
    SURF_FRIC, AIR_RES, SURF_ACCEL, AIR_ACCEL,
    FL_ACCEL, FL_FRIC
)


class AABB:
    def __init__(self, mn, mx):
        self.min = np.array(mn, dtype='f4')
        self.max = np.array(mx, dtype='f4')

    def intersects(self, other):
        return (
            self.min[0] <= other.max[0] and self.max[0] >= other.min[0] and
            self.min[1] <= other.max[1] and self.max[1] >= other.min[1] and
            self.min[2] <= other.max[2] and self.max[2] >= other.min[2]
        )

    def expand(self, amt):
        off = np.array([amt, amt, amt], dtype='f4')
        return AABB(self.min - off, self.max + off)





class PhysicsEngine:
    def __init__(self, world):
        self.world = world
        self.eye_h = P_EYE_H
        self.eye_f = P_EYE_F
        self.pw    = P_W
        self.ph    = P_H

    def playeraabb(self, pos):
        hw = self.pw / 2
        return AABB(
            [pos[0] - hw, pos[1], pos[2] - hw],
            [pos[0] + hw, pos[1] + self.ph, pos[2] + hw]
        )
        
        
        
        

    def isblocksolid(self, x, y, z):
        return self.world.issolid(int(math.floor(x)), int(math.floor(y)), int(math.floor(z)))
        
        

    def collidingblocks(self, aabb, result=[]):
        result = []
        x0 = int(math.floor(aabb.min[0])); x1 = int(math.ceil(aabb.max[0]))
        y0 = int(math.floor(aabb.min[1])); y1 = int(math.ceil(aabb.max[1]))
        z0 = int(math.floor(aabb.min[2])); z1 = int(math.ceil(aabb.max[2]))
        for x in range(x0, x1):
            for y in range(y0, y1):
                for z in range(z0, z1):
                    if self.isblocksolid(x, y, z):
                        ba = AABB([x, y, z], [x+1, y+1, z+1])
                        if aabb.intersects(ba):
                            result.append((x, y, z, ba))
                            
        return result
        
        
        
        



    def check_coll(self, pos, mv):
        #solve y -> solve x, z (axis separated)

        fp       = pos.copy()
        am       = np.array([0.0, 0.0, 0.0], dtype='f4')
        on_gnd   = False
        hit_ceil = False
        _steps   = 0
        

        if mv[1] != 0:
            tp = fp.copy(); tp[1] += mv[1]
            if self.is_validpos(tp):
                fp[1]  = tp[1]
                am[1] = mv[1]
                
                
            else:
                # fast->bisect, else step
                precise = abs(mv[1]) > 0.6
                
                if mv[1] < 0:
                    on_gnd = True
                    if precise:
                        lo, hi = tp[1], fp[1]
                        for _ in range(6):
                            mid = 0.5 * (lo + hi)
                            probe = fp.copy(); probe[1] = mid
                            if self.is_validpos(probe): hi = mid
                            else: lo = mid
                        fp[1] = hi
                        
                        
                    else:
                        ty    = math.floor(fp[1])
                        found = False
                        for _ in range(10):
                            probe = fp.copy(); probe[1] = ty
                            if self.is_validpos(probe):
                                found = True; fp[1] = ty; break
                            ty += 0.05
                            
                            
                        if not found:
                            fp[1] = math.ceil(tp[1]) + 0.001
                            
                            
                            
                            
                else:
                    hit_ceil = True
                    if precise:
                        lo, hi = fp[1], tp[1]
                        for _ in range(6):
                            mid = 0.5 * (lo + hi)
                            probe = fp.copy(); probe[1] = mid
                            if self.is_validpos(probe): lo = mid
                            else: hi = mid
                        fp[1] = lo
                        
                    else:
                        fp[1] = math.floor(tp[1] + self.ph) - self.ph - 0.01
                        
                        
                        
                        

        if mv[0] != 0:
            tp = fp.copy(); tp[0] += mv[0]
            if self.is_validpos(tp): fp[0] = tp[0]; am[0] = mv[0]

        if mv[2] != 0:
            tp = fp.copy(); tp[2] += mv[2]
            if self.is_validpos(tp): fp[2] = tp[2]; am[2] = mv[2]

        #print(fp, am, on_gnd)
        return fp, am, on_gnd, hit_ceil
        
        
        
        
        

    def is_validpos(self, pos):
        hw = self.pw / 2
        px, py, pz = pos[0], pos[1], pos[2]
        mnx, mxx   = px - hw,       px + hw
        mny, mxy   = py,             py + self.ph
        mnz, mxz   = pz - hw, pz + hw

        is_solid = self.world.issolid  # cache for loop
        flr, cl  = math.floor, math.ceil
        m  = 0.001
        sx = int(flr(mnx - m)); ex = int(cl(mxx + m))
        sy = int(flr(mny - m)); ey = int(cl(mxy + m))
        sz = int(flr(mnz - m)); ez = int(cl(mxz + m))
        #print(sx, ex, sy, ey, sz, ez)

        for x in range(sx, ex):
            for y in range(sy, ey):
                for z in range(sz, ez):
                    if is_solid(x, y, z):
                        if (mnx < x+1 and mxx > x and
                            mny < y+1 and mxy > y and
                            mnz < z+1 and mxz > z):
                            return False
        return True

    def grounded(self, pos):
        tp = pos.copy(); tp[1] -= 0.02
        if not self.is_validpos(tp): return True
        tp[1] = pos[1] - 0.001
        return not self.is_validpos(tp)
        
        
        

    def apply_physics(self, pos, vel, on_ground, fly, dt):
        #print(on_ground, fly)
        if fly: on_ground = False
        else:
            on_ground = self.grounded(pos)
            if on_ground:
                if vel[1] < 0: vel[1] = 0
                
            else:
                vel[1] += GRAVITY * dt
                if vel[1] < TERM_V: vel[1] = TERM_V
                
        return vel, on_ground
        
        
        
        

    """
    def apply_movinput(self, vel, move_dir, on_ground, fly, sprint, dt):
        spd = FL_SPEED if fly else MAX_GSPEED * (MP_SPRINT if sprint else 1.0)
        n = np.linalg.norm(move_dir)
        if n > 0:
            d = move_dir / n
            vel[0] = d[0] * spd
            vel[2] = d[2] * spd
            if fly: vel[1] = d[1] * spd
        else:
            vel[0] = 0; vel[2] = 0
        return vel
    """

    def apply_movinput(self, vel, move_dir, on_ground, fly, sprint, dt):
        if fly:
            tspd = FL_SPEED * (FL_SPEED_MP if sprint else 1.0)
            n    = np.linalg.norm(move_dir)
            if n > 0:
                d   = move_dir / n
                lf  = 10.0 * dt
                vel = vel * (1 - lf) + d * tspd * lf
            else:
                vel *= 0.8
        else:
            wspd = MAX_GSPEED * (MP_SPRINT if sprint else 1.0)
            n    = np.linalg.norm(move_dir)
            if n > 0:
                d      = move_dir / n
                vel[0] = d[0] * wspd
                vel[2] = d[2] * wspd
            else:
                vel[0] = 0
                vel[2] = 0
                if not on_ground:
                    vel[0] *= 0.95
                    vel[2] *= 0.95
        return vel
        
        

    def apply_jump(self, vel, on_ground):
        if on_ground: vel[1] = JUMP_V
        return vel


"""
def check_coll(self, pos, mv):
    fp     = pos.copy()
    on_gnd = False
    tp = fp.copy(); tp[1] += mv[1]
    if self.is_validpos(tp): fp[1] = tp[1]
    else:
        on_gnd = mv[1] < 0
        fp[1]  = math.floor(fp[1]) if mv[1] < 0 else fp[1]
    tp = fp.copy(); tp[0] += mv[0]
    if self.is_validpos(tp): fp[0] = tp[0]
    tp = fp.copy(); tp[2] += mv[2]
    if self.is_validpos(tp): fp[2] = tp[2]
    return fp, on_gnd
"""
