import pygame
import pygame.surfarray
import json
import os
import math
import numpy as np
import _respath


ANIM_TEXT = {
    "fire_layer_0": 16,
    "fire_layer_1": 16,
    "lava_flow": 32,
    "lava_still": 16,
    "prismarine_rough": 16,
    "sea_lantern": 16,
    "water_flow": 32,
    "water_still": 16,
}


META_FILES = {
    "fire_layer_0": "fire_layer_0.png.json",
    "fire_layer_1": "fire_layer_1.png.json",
    "lava_flow":    "lava_flow.png.json",
    "lava_still":   "lava_still.png.json",
    "prismarine_rough": "prismarine_rough.png.json",
    "sea_lantern":  "sea_lantern.png.json",
    "water_flow":   "water_flow.png.json",
    "water_still":  "water_still.png.json",
}


class AnimSettings:
    def __init__(self, frametime=1, interpolate=False, frames=None):
        self.frametime   = frametime
        self.interpolate = interpolate
        self.frames      = frames








class AnimManager:
    TPS     = 20
    TILE_SZ = 16

    def __init__(self, meta_dir=None):
        if meta_dir is None:
            meta_dir = _respath.dir_anims()
        self.meta_dir   = meta_dir
        self.settings   = {}
        self.textures   = {}
        self.fcounts    = {}
        self.tsizes     = {}
        self.fstates    = {}
        self.tick_acc   = 0.0
        self.id_to_anim = {}

        self.atlas  = None
        self.atw    = 0
        self.ath    = 0
        self.layout = {}

        self.loadsetting()
        self.loadtext()
        self.bakeatlas()
        self.initfstates()
        self.init_blockmapping()
        
        
        
        
        

    def init_blockmapping(self):
        from world import blocks
        self.id_to_anim = {
            blocks.PRISMARINE:  "prismarine_rough",
            blocks.SEA_LANTERN: "sea_lantern",
            blocks.WATER:       "water_still",
        }
        
        
        self.id_to_anim[blocks.LAVA]          = "lava_still"
        self.id_to_anim[blocks.FIRE]          = "fire_layer_0"
        self.id_to_anim[blocks.WATER_FLOWING] = "water_flow"
        self.id_to_anim[blocks.LAVA_FLOWING]  = "lava_flow"

    def loadsetting(self):
        for i, j in META_FILES.items():
            path = os.path.join(self.meta_dir, j)
            if os.path.exists(path):
                with open(path, 'r') as f:
                    data = json.load(f)
                    anim = data.get("animation", {})
                    self.settings[i] = AnimSettings(
                        frametime   = anim.get("frametime", 1),
                        interpolate = anim.get("interpolate", False),
                        frames      = anim.get("frames")
                    )

            # self.settings[i] = AnimSettings(frametime=ANIM_TEXT[i] // 4)

            else:
                self.settings[i] = AnimSettings()
                
                
                

    def loadtext(self):
        for i, tile_sz in ANIM_TEXT.items():
            png_path = os.path.join(self.meta_dir, f"{i}.png")
            if os.path.exists(png_path):
                img = pygame.image.load(png_path).convert_alpha()
                self.textures[i] = img
                self.tsizes[i]   = tile_sz
                self.fcounts[i]  = img.get_height() // tile_sz
                
            else:
                self.textures[i] = None
                self.tsizes[i]   = tile_sz
                self.fcounts[i]  = 1




    def bakeatlas(self):
        maxf = max(self.fcounts.values()) if self.fcounts else 1

        colasgn = {}
        curcol  = 0
        for i in ANIM_TEXT:
            tile_sz = self.tsizes.get(i, 16)
            ncols   = tile_sz // self.TILE_SZ  # 32px textures := 2 cols
            colasgn[i] = (curcol, ncols)
            curcol += ncols
            

        self.atw = curcol * self.TILE_SZ
        self.ath = maxf * self.TILE_SZ
        # print(self.atw, self.ath)

        self.atlas = pygame.Surface((self.atw, self.ath), pygame.SRCALPHA)
        self.atlas.fill((0, 0, 0, 0))
        

        for i, (j, k) in colasgn.items():
            img = self.textures.get(i)
            if not img:
                continue

            tile_sz = self.tsizes.get(i, 16)
            fcount  = self.fcounts.get(i, 1)

            self.layout[i] = (j, 0, fcount)

            for fi in range(fcount):
                src_y = fi * tile_sz
                sr = pygame.Rect(0, src_y, tile_sz, tile_sz)

                if src_y + tile_sz <= img.get_height():
                    fsurf = img.subsurface(sr)
                    dw    = k * self.TILE_SZ
                    dh    = self.TILE_SZ

                    if tile_sz != self.TILE_SZ:
                        fsurf = pygame.transform.scale(fsurf, (dw, dh))

                    self.atlas.blit(fsurf, (j * self.TILE_SZ, fi * self.TILE_SZ))
                    
                    

    def initfstates(self):
        for i in ANIM_TEXT:
            self.fstates[i] = {'frame': 0, 'tick_counter': 0}

    """
    def update(self, dt):
        ticks = int(dt * self.TPS)
        for _ in range(ticks):
            self.nexttick()
    """

    def update(self, dt):
        # dt -> discrete ticks
        self.tick_acc += dt * self.TPS
        # print(self.tick_acc)
        while self.tick_acc >= 1.0:
            self.tick_acc -= 1.0
            self.nexttick()
            

    def nexttick(self):
        _ntick = 0
        for i, j in self.fstates.items():
            # print(i, j['frame'])
            settings = self.settings.get(i, AnimSettings())
            j['tick_counter'] += 1
            if j['tick_counter'] >= settings.frametime:
                j['tick_counter'] = 0
                fcount = self.fcounts.get(i, 1)
                if settings.frames:
                    j['frame'] = (j['frame'] + 1) % len(settings.frames)
                else:
                    j['frame'] = (j['frame'] + 1) % fcount
                    
                    
                    

    def getframe(self, i):
        if i not in self.fstates: return 0
        j        = self.fstates[i]
        settings = self.settings.get(i, AnimSettings())
        if settings.frames: return settings.frames[j['frame']]
        return j['frame']

    # def getframe(self, i):
    #     if i not in self.fstates: return 0.0
    #     return self.fstates[i]['frame'] / max(1, self.fcounts.get(i, 1))
        
        

    def atlaslayout(self, i): return self.layout.get(i, (0, 0, 1))
    def framecount(self, i):  return self.fcounts.get(i, 1)
    def surfaceatlas(self):   return self.atlas
    def szatlas(self):        return (self.atw, self.ath)
    
    

    def spritesurf(self, i, size=16):
        if not self.atlas or i not in self.layout: return None

        frame = self.getframe(i)
        j, _, fcount = self.layout[i]

        tile_sz   = self.tsizes.get(i, 16)
        cols_used = tile_sz // self.TILE_SZ

        if frame >= fcount: frame = 0

        px = j * self.TILE_SZ
        py = frame * self.TILE_SZ
        pw = cols_used * self.TILE_SZ
        ph = self.TILE_SZ

        if px + pw > self.atw or py + ph > self.ath: return None

        sprite = self.atlas.subsurface(pygame.Rect(px, py, pw, ph))

        if size != self.TILE_SZ:
            return pygame.transform.scale(sprite, (size, size))
            
        return sprite.copy()
        
        
        
        
        
        

    def blockanimtext(self, blockId): return self.id_to_anim.get(blockId)
    def isanimblock(self, blockId):   return blockId in self.id_to_anim
    def isanimated(self, i):          return i in ANIM_TEXT






_anims = None


def getanims():
    global _anims
    if _anims is None:
        _anims = AnimManager()
    return _anims
