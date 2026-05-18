
import numpy as np
import pygame
from pygame.locals import *
import math
from pyrr import Matrix44

from config import (
    FOV, N_PLANE, F_PLANE, SENSIVITY, MOUS_SMOOTH,
    WIN_W, WIN_H
)


class Camera:
    def __init__(self, pos=None):
        self.pos   = pos if pos is not None else np.array([0.0, 80.0, 0.0], dtype='f4')
        self.front = np.array([0.0, 0.0, -1.0], dtype='f4')
        self.up    = np.array([0.0, 1.0,  0.0], dtype='f4')

        self.yaw   = -90.0
        self.pitch = -20.0

        self.target_yaw   = self.yaw
        self.target_pitch = self.pitch

        self._proj = None

        self.updatevecs()
        
        

    def updatevecs(self):
        front = np.array([
            math.cos(math.radians(self.yaw)) * math.cos(math.radians(self.pitch)),
            math.sin(math.radians(self.pitch)),
            math.sin(math.radians(self.yaw)) * math.cos(math.radians(self.pitch))
        ], dtype='f4')
        self.front = front / np.linalg.norm(front)
        
        

    def mvpmat(self, inverted=False):
        # inverted=True : flip view dir
        target = self.pos - self.front if inverted else self.pos + self.front
        view   = Matrix44.look_at(self.pos, target, self.up)

        if self._proj is None:
            self._proj = Matrix44.perspective_projection(
                FOV, WIN_W / WIN_H, N_PLANE, F_PLANE
            )

        return self._proj * view
        
        
        
        
        

    def invalidproj(self):
        self._proj = None

    def oninput(self, dt):
        keys  = pygame.key.get_pressed()
        spd   = 25.0 * dt
        right = np.cross(self.front, self.up)
        right = right / np.linalg.norm(right)

        if keys[K_LSHIFT] and keys[K_w]: spd *= 3.0

        if keys[K_w]:     self.pos += self.front * spd
        if keys[K_s]:     self.pos -= self.front * spd
        if keys[K_a]:     self.pos -= right * spd
        if keys[K_d]:     self.pos += right * spd
        if keys[K_SPACE]: self.pos[1] += spd
        if keys[K_LCTRL]: self.pos[1] -= spd
        
        


    def onmouse(self):
        dx, dy = pygame.mouse.get_rel()

        self.target_yaw   +=  dx * SENSIVITY
        self.target_pitch  = max(-89.0, min(89.0, self.target_pitch - dy * SENSIVITY))

        sf = 1.0 - MOUS_SMOOTH
        self.yaw   += (self.target_yaw   - self.yaw)   * sf
        self.pitch += (self.target_pitch - self.pitch) * sf

        self.updatevecs()

    def chunkpos(self, chunk_sz):
        return (
            int(self.pos[0] // chunk_sz), 
            int(self.pos[2] // chunk_sz)
        )

















