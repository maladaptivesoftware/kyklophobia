# state bit layout: [PSSS SSBB] [BBBB BBBB]
#   b 0-9:   block id (1024 max)
#   b 10-14: block-specific state
#   b 15:    player-placed flag

from world.blocks import WATER, WATER_FLOWING

STATE_BITS       = 5
BLOCK_ID_BITS    = 10
BLOCK_ID_MASK    = (1 << BLOCK_ID_BITS) - 1   # 0x3FF
STATE_MASK       = ((1 << STATE_BITS) - 1) << BLOCK_ID_BITS  # 0x7C00
STATE_SHIFT      = BLOCK_ID_BITS
PLAYER_PLACED_FLAG = 0x8000


def packBlock(blockId, state=0): return (blockId & BLOCK_ID_MASK) | ((state & 0x1F) << STATE_SHIFT)
def unpackBlock(value):          return value & BLOCK_ID_MASK, (value >> STATE_SHIFT) & 0x1F
def getId(value):                return value & BLOCK_ID_MASK
def getState(value):             return (value >> STATE_SHIFT) & 0x1F
def setState(value, state):      return (value & BLOCK_ID_MASK) | ((state & 0x1F) << STATE_SHIFT)


_state_handlers = {}


def regstatehandler(blockId, handler_class): _state_handlers[blockId] = handler_class

def statehandler(blockId): return _state_handlers.get(blockId)
def hasStates(blockId):    return blockId in _state_handlers


class BlockStateHandler:
    properties    = {}
    default_state = 0

    @classmethod
    def getprop(cls, state, prop_name):
        raise NotImplementedError

    @classmethod
    def setprop(cls, state, prop_name, value):
        raise NotImplementedError

    @classmethod
    def renderoff(cls, state): return 0.0

    @classmethod
    def textvrngt(cls, state): return 0





STATEFUL_BLOCKS = set()


def init_blockStates():
    global STATEFUL_BLOCKS
    STATEFUL_BLOCKS = set(_state_handlers.keys())


def load_statehandlers():
    from world.states import water
    init_blockStates()
    
    
    
    
    
