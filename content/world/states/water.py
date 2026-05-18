# level state 0-15
# 0    = full
# 1-7  = flowing : 1-7
# 8-15 = falling : 0-7 (verical)
# render height = (8 - min(level,7)) / 8

from world.blocks import WATER, WATER_FLOWING
from world.blockstate import BlockStateHandler, regstatehandler


_LEVEL_MASK = 0x0F


def getlvl(state):      return state & _LEVEL_MASK
def setlvl(state, lvl): return (state & ~_LEVEL_MASK) | (lvl & _LEVEL_MASK)
def issource(state):    return getlvl(state) == 0
def isfalling(state):   return getlvl(state) >= 8

def flowdep(state):
    lvl = getlvl(state)
    return lvl - 8 if lvl >= 8 else lvl





def hrender(state):
    lvl = getlvl(state)
    # return (8 - lvl) / 8.0
    if lvl == 0: return 0.875
    fl = lvl if lvl < 8 else lvl - 8
    return (8 - fl) / 9.0

def renderoff(state): return 1.0 - hrender(state)






class WaterStateHandler(BlockStateHandler):
    properties = {'level': (0, 15)}
    _default   = 0

    def getlvl(self, state):              return getlvl(state)
    def setlvl(self, state, lvl):         return setlvl(state, lvl)
    def issource(self, state):            return issource(state)
    def isfalling(self, state):           return isfalling(state)
    def flowdep(self, state):             return flowdep(state)
    def hrender(self, state):             return hrender(state)
    def renderoff(self, state):           return renderoff(state)

    def getprop(self, state, prop_name):
        if prop_name == 'level': return getlvl(state)
        return None

    def setprop(self, state, prop_name, value):
        if prop_name == 'level': return setlvl(state, value)
        return state




# shorthands used by terrain/renderer code
def get_waterlvl(state):   return getlvl(state)
def get_waterH(state):     return hrender(state)
def is_watersource(state): return issource(state)
def make_watrstate(level): return setlvl(0, level)


regstatehandler(WATER,         WaterStateHandler)
regstatehandler(WATER_FLOWING, WaterStateHandler)
