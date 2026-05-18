BLOCKENTY_TYPES = {}
ITEM_BLOCK_ACTION = {}


def regblockent(bid):
    def decor(cls):
        BLOCKENTY_TYPES[bid] = cls
        return cls
    return decor


def blockenttype(bid):   return BLOCKENTY_TYPES.get(bid)
def itemblock(iid, bid): return ITEM_BLOCK_ACTION.get((iid, bid))
def regitemblock(iid, bid, handler):  
    ITEM_BLOCK_ACTION[(iid, bid)] = handler

