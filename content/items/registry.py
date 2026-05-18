from world import blocks


class ItemDef:
    def __init__(
        self, itemId, nm, category="misc", is_block=False,
        max_stack=64, texture_uv=(0, 0), atlas="blocks",
        foliage_tint=False, tool_type=None, damage=0,
        places_block=None
    ):
        
        self.itemId = itemId
        self.nm = nm
        self.category = category
        self.is_block = is_block
        self.max_stack = max_stack
        self.texture_uv = texture_uv
        self.atlas = atlas
        self.foliage_tint = foliage_tint
        self.tool_type = tool_type
        self.damage = damage
        self.places_block = places_block

    def __repr__(self):
        return f"ItemDef({self.itemId}: {self.nm})"


class ItemStack:
    def __init__(self, idef, count=1):
        self.item = idef
        self.count = min(count, idef.max_stack)

    def add(self, amount):
        space = self.item.max_stack - self.count
        ta = min(amount, space)
        self.count += ta
        return amount - ta

    def isfull(self):
        return self.count >= self.item.max_stack

    def copy(self):
        return ItemStack(self.item, self.count)

    def __repr__(self):
        return f"{self.count}x {self.item.nm}"


BUILDING   = "building"
DECORATION = "decoration"
NATURE     = "nature"
TOOLS      = "tools"
COMBAT     = "combat"
FOOD       = "food"
MATERIALS  = "materials"
MISC       = "misc"


class ItemRegistry:
    def __init__(self):
        self._items = {}
        self._by_category = {}
        self._sorted_ids = []

    def register(self, itemId, nm, **kwargs):
        item = ItemDef(itemId, nm, **kwargs)
        self._items[itemId] = item

        cat = item.category
        if cat not in self._by_category:
            self._by_category[cat] = []
        self._by_category[cat].append(item)

        self._sorted_ids = sorted(self._items.keys())
        return item
        
        
        

    def get(self, itemId):     return self._items.get(itemId)
    def exists(self, itemId):  return itemId in self._items
    def getall(self):          return [self._items[i] for i in self._sorted_ids]
    def bycat(self, category): return self._by_category.get(category, [])
    
    

    def search(self, query):
        query = query.lower().strip()
        if not query: return self.getall()
        
        

        res = []
        for i in self._items.values():
            if query in i.nm.lower():
                res.append(i)

        return sorted(res, key=lambda x: x.itemId)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self.getall())


REGISTRY = ItemRegistry()


def blockuv(bid):
    if bid in blocks.BLOCK_FACES:
        faces = blocks.BLOCK_FACES[bid]
        tname = faces if isinstance(faces, str) else faces[0]
        if tname in blocks.TEXTURES:
            return blocks.TEXTURES[tname]
    return (0, 0)
