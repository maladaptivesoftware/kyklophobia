from world import blocks
from items import textures
from items.registry import REGISTRY, blockuv
from items.registry import BUILDING, DECORATION, NATURE, TOOLS, COMBAT, FOOD, MATERIALS, MISC


def regblocks():
    R = REGISTRY

    building = [
        (blocks.STONE, "Stone"),
        (blocks.COBBLESTONE, "Cobblestone"),
        (blocks.COBBLESTONE_MOSSY, "Mossy Cobblestone"),
        (blocks.STONEBRICK, "Stone Bricks"),
        (blocks.STONEBRICK_MOSSY, "Mossy Stone Bricks"),
        (blocks.STONEBRICK_CRACKED, "Cracked Stone Bricks"),
        (blocks.STONEBRICK_CARVED, "Chiseled Stone Bricks"),
        (blocks.BRICK, "Bricks"),
        (blocks.NETHER_BRICK, "Nether Bricks"),
        (blocks.OAK_PLANKS, "Oak Planks"),
        (blocks.SPRUCE_PLANKS, "Spruce Planks"),
        (blocks.BIRCH_PLANKS, "Birch Planks"),
        (blocks.JUNGLE_PLANKS, "Jungle Planks"),
        (blocks.ACACIA_PLANKS, "Acacia Planks"),
        (blocks.DARK_OAK_PLANKS, "Dark Oak Planks"),
        (blocks.SANDSTONE, "Sandstone"),
        (blocks.SANDSTONE_CARVED, "Chiseled Sandstone"),
        (blocks.SANDSTONE_SMOOTH, "Smooth Sandstone"),
        (blocks.RED_SANDSTONE, "Red Sandstone"),
        (blocks.RED_SANDSTONE_CARVED, "Chiseled Red Sandstone"),
        (blocks.RED_SANDSTONE_SMOOTH, "Smooth Red Sandstone"),
        (blocks.QUARTZ_BLOCK, "Quartz Block"),
        (blocks.QUARTZ_CHISELED, "Chiseled Quartz"),
        (blocks.QUARTZ_PILLAR, "Quartz Pillar"),
        (blocks.OBSIDIAN, "Obsidian"),
        (blocks.PRISMARINE, "Prismarine"),
        (blocks.PRISMARINE_BRICKS, "Prismarine Bricks"),
        (blocks.PRISMARINE_DARK, "Dark Prismarine"),
        (blocks.END_STONE, "End Stone"),
        (blocks.HARDENED_CLAY, "Hardened Clay"),
    ]

    for bid, nm in building:
        R.register(
            bid, nm, category=BUILDING, is_block=True,
            texture_uv=blockuv(bid), atlas="blocks"
        )

    nature = [
        (blocks.GRASS, "Grass Block", True),
        (blocks.DIRT, "Dirt", False),
        (blocks.COARSE_DIRT, "Coarse Dirt", False),
        (blocks.PODZOL, "Podzol", False),
        (blocks.MYCELIUM, "Mycelium", False),
        (blocks.SAND, "Sand", False),
        (blocks.RED_SAND, "Red Sand", False),
        (blocks.GRAVEL, "Gravel", False),
        (blocks.CLAY, "Clay", False),
        (blocks.SNOW, "Snow", False),
        (blocks.SNOW_BLOCK, "Snow Block", False),
        (blocks.ICE, "Ice", False),
        (blocks.ICE_PACKED, "Packed Ice", False),
        (blocks.OAK_LOG, "Oak Log", False),
        (blocks.SPRUCE_LOG, "Spruce Log", False),
        (blocks.BIRCH_LOG, "Birch Log", False),
        (blocks.JUNGLE_LOG, "Jungle Log", False),
        (blocks.ACACIA_LOG, "Acacia Log", False),
        (blocks.DARK_OAK_LOG, "Dark Oak Log", False),
        (blocks.OAK_LEAVES, "Oak Leaves", True),
        (blocks.SPRUCE_LEAVES, "Spruce Leaves", True),
        (blocks.BIRCH_LEAVES, "Birch Leaves", True),
        (blocks.JUNGLE_LEAVES, "Jungle Leaves", True),
        (blocks.ACACIA_LEAVES, "Acacia Leaves", True),
        (blocks.DARK_OAK_LEAVES, "Dark Oak Leaves", True),
        (blocks.TALLGRASS, "Tall Grass", True),
        (blocks.CACTUS, "Cactus", False),
        (blocks.MELON, "Melon", False),
        (blocks.PUMPKIN, "Pumpkin", False),
    ]

    for i in nature:
        bid, nm = i[0], i[1]
        foliage = i[2] if len(i) > 2 else False
        R.register(
            bid, nm, category=NATURE, is_block=True,
            texture_uv=blockuv(bid), atlas="blocks", foliage_tint=foliage
        )

    ores = [
        (blocks.COAL_ORE, "Coal Ore"),
        (blocks.IRON_ORE, "Iron Ore"),
        (blocks.GOLD_ORE, "Gold Ore"),
        (blocks.DIAMOND_ORE, "Diamond Ore"),
        (blocks.EMERALD_ORE, "Emerald Ore"),
        (blocks.REDSTONE_ORE, "Redstone Ore"),
        (blocks.LAPIS_ORE, "Lapis Ore"),
    ]

    for bid, nm in ores:
        R.register(
            bid, nm, category=MATERIALS, is_block=True,
            texture_uv=blockuv(bid), atlas="blocks"
        )

    minerals = [
        (blocks.COAL_BLOCK, "Coal Block"),
        (blocks.IRON_BLOCK, "Iron Block"),
        (blocks.GOLD_BLOCK, "Gold Block"),
        (blocks.DIAMOND_BLOCK, "Diamond Block"),
        (blocks.EMERALD_BLOCK, "Emerald Block"),
        (blocks.REDSTONE_BLOCK, "Redstone Block"),
        (blocks.LAPIS_BLOCK, "Lapis Block"),
        (blocks.GLOWSTONE, "Glowstone"),
        (blocks.SEA_LANTERN, "Sea Lantern"),
    ]

    for bid, nm in minerals:
        R.register(
            bid, nm, category=BUILDING, is_block=True,
            texture_uv=blockuv(bid), atlas="blocks"
        )

    decoration = [
        (blocks.GLASS, "Glass"),
        (blocks.BOOKSHELF, "Bookshelf"),
        (blocks.CRAFTING_TABLE, "Crafting Table"),
        (blocks.FURNACE, "Furnace"),
        (blocks.NOTEBLOCK, "Note Block"),
        (blocks.JUKEBOX, "Jukebox"),
        (blocks.JACK_O_LANTERN, "Jack o'Lantern"),
        (blocks.HAY_BLOCK, "Hay Bale"),
        (blocks.SPONGE, "Sponge"),
        (blocks.SPONGE_WET, "Wet Sponge"),
        (blocks.SLIME, "Slime Block"),
        (blocks.REDSTONE_LAMP, "Redstone Lamp"),
        (blocks.BEACON, "Beacon"),
    ]

    for bid, nm in decoration:
        R.register(
            bid, nm, category=DECORATION, is_block=True,
            texture_uv=blockuv(bid), atlas="blocks"
        )

    special = [
        (blocks.BEDROCK, "Bedrock"),
        (blocks.TNT, "TNT"),
        (blocks.MOB_SPAWNER, "Mob Spawner"),
        (blocks.COMMAND_BLOCK, "Command Block"),
        (blocks.DRAGON_EGG, "Dragon Egg"),
        (blocks.NETHERRACK, "Netherrack"),
        (blocks.SOUL_SAND, "Soul Sand"),
    ]

    for bid, nm in special:
        R.register(
            bid, nm, category=MISC, is_block=True,
            texture_uv=blockuv(bid), atlas="blocks"
        )

    stones = [
        (blocks.ANDESITE,        "Andesite"),
        (blocks.ANDESITE_SMOOTH, "Polished Andesite"),
        (blocks.DIORITE,         "Diorite"),
        (blocks.DIORITE_SMOOTH,  "Polished Diorite"),
        (blocks.GRANITE,         "Granite"),
        (blocks.GRANITE_SMOOTH,  "Polished Granite"),
    ]

    for bid, nm in stones:
        R.register(
            bid, nm, category=BUILDING, is_block=True,
            texture_uv=blockuv(bid), atlas="blocks"
        )

    wool = [
        (blocks.WOOL_WHITE,      "White Wool"),
        (blocks.WOOL_ORANGE,     "Orange Wool"),
        (blocks.WOOL_MAGENTA,    "Magenta Wool"),
        (blocks.WOOL_LIGHT_BLUE, "Light Blue Wool"),
        (blocks.WOOL_YELLOW,     "Yellow Wool"),
        (blocks.WOOL_LIME,       "Lime Wool"),
        (blocks.WOOL_PINK,       "Pink Wool"),
        (blocks.WOOL_GRAY,       "Gray Wool"),
        (blocks.WOOL_SILVER,     "Light Gray Wool"),
        (blocks.WOOL_CYAN,       "Cyan Wool"),
        (blocks.WOOL_PURPLE,     "Purple Wool"),
        (blocks.WOOL_BLUE,       "Blue Wool"),
        (blocks.WOOL_BROWN,      "Brown Wool"),
        (blocks.WOOL_GREEN,      "Green Wool"),
        (blocks.WOOL_RED,        "Red Wool"),
        (blocks.WOOL_BLACK,      "Black Wool"),
    ]

    for bid, nm in wool:
        R.register(
            bid, nm, category=DECORATION, is_block=True,
            texture_uv=blockuv(bid), atlas="blocks"
        )

    glass = [
        (blocks.GLASS_WHITE,      "White Glass"),
        (blocks.GLASS_ORANGE,     "Orange Glass"),
        (blocks.GLASS_MAGENTA,    "Magenta Glass"),
        (blocks.GLASS_LIGHT_BLUE, "Light Blue Glass"),
        (blocks.GLASS_YELLOW, "Yellow Glass"),
        (blocks.GLASS_LIME,   "Lime Glass"),
        (blocks.GLASS_PINK,   "Pink Glass"),
        (blocks.GLASS_GRAY,   "Gray Glass"),
        (blocks.GLASS_SILVER, "Light Gray Glass"),
        (blocks.GLASS_CYAN,   "Cyan Glass"),
        (blocks.GLASS_PURPLE, "Purple Glass"),
        (blocks.GLASS_BLUE,   "Blue Glass"),
        (blocks.GLASS_BROWN,  "Brown Glass"),
        (blocks.GLASS_GREEN,  "Green Glass"),
        (blocks.GLASS_RED,    "Red Glass"),
        (blocks.GLASS_BLACK,  "Black Glass"),
    ]

    for bid, nm in glass:
        R.register(
            bid, nm, category=DECORATION, is_block=True,
            texture_uv=blockuv(bid), atlas="blocks"
        )

    clay = [
        (blocks.CLAY_WHITE,   "White Terracotta"),
        (blocks.CLAY_ORANGE,  "Orange Terracotta"),
        (blocks.CLAY_MAGENTA, "Magenta Terracotta"),
        (blocks.CLAY_LIGHT_BLUE, "Light Blue Terracotta"),
        (blocks.CLAY_YELLOW, "Yellow Terracotta"),
        (blocks.CLAY_LIME,   "Lime Terracotta"),
        (blocks.CLAY_PINK,   "Pink Terracotta"),
        (blocks.CLAY_GRAY,   "Gray Terracotta"),
        (blocks.CLAY_SILVER, "Light Gray Terracotta"),
        (blocks.CLAY_CYAN,   "Cyan Terracotta"),
        (blocks.CLAY_BLUE,   "Blue Terracotta"),
        (blocks.CLAY_BROWN,  "Brown Terracotta"),
        (blocks.CLAY_GREEN,  "Green Terracotta"),
        (blocks.CLAY_RED,    "Red Terracotta"),
        (blocks.CLAY_BLACK,  "Black Terracotta"),
    ]

    for bid, nm in clay:
        R.register(
            bid, nm, category=BUILDING, is_block=True,
            texture_uv=blockuv(bid), atlas="blocks"
        )

    R.register(
        blocks.WATER, "Water", category=MISC, is_block=True,
        texture_uv=blocks.TEXTURES.get("water_still", (17, 16)), atlas="blocks"
    )

    # stairs
    stairs = [
        (blocks.OAK_STAIRS,    "Oak Stairs"),
        (blocks.SPRUCE_STAIRS, "Spruce Stairs"),
        (blocks.BIRCH_STAIRS,  "Birch Stairs"),
        (blocks.JUNGLE_STAIRS, "Jungle Stairs"),
        (blocks.ACACIA_STAIRS, "Acacia Stairs"),
        (blocks.DARK_OAK_STAIRS,     "Dark Oak Stairs"),
        (blocks.STONE_STAIRS,        "Stone Stairs"),
        (blocks.COBBLESTONE_STAIRS,  "Cobblestone Stairs"),
        (blocks.BRICK_STAIRS,        "Brick Stairs"),
        (blocks.STONE_BRICK_STAIRS,  "Stone Brick Stairs"),
        (blocks.NETHER_BRICK_STAIRS, "Nether Brick Stairs"),
        (blocks.SANDSTONE_STAIRS,     "Sandstone Stairs"),
        (blocks.QUARTZ_STAIRS,        "Quartz Stairs"),
        (blocks.RED_SANDSTONE_STAIRS, "Red Sandstone Stairs"),
    ]

    for bid, nm in stairs:
        R.register(
            bid, nm, category=BUILDING, is_block=True,
            texture_uv=blockuv(bid), atlas="blocks"
        )

    # slabs
    slabs = [
        (blocks.STONE_SLAB,        "Stone Slab"),
        (blocks.SANDSTONE_SLAB,    "Sandstone Slab"),
        (blocks.COBBLESTONE_SLAB,  "Cobblestone Slab"),
        (blocks.BRICK_SLAB,        "Brick Slab"),
        (blocks.STONE_BRICK_SLAB,  "Stone Brick Slab"),
        (blocks.NETHER_BRICK_SLAB, "Nether Brick Slab"),
        (blocks.QUARTZ_SLAB, "Quartz Slab"),
        (blocks.OAK_SLAB,    "Oak Slab"),
        (blocks.SPRUCE_SLAB, "Spruce Slab"),
        (blocks.BIRCH_SLAB,  "Birch Slab"),
        (blocks.JUNGLE_SLAB, "Jungle Slab"),
        (blocks.ACACIA_SLAB, "Acacia Slab"),
        (blocks.DARK_OAK_SLAB,      "Dark Oak Slab"),
        (blocks.RED_SANDSTONE_SLAB, "Red Sandstone Slab"),
    ]

    for bid, nm in slabs:
        R.register(
            bid, nm, category=BUILDING, is_block=True,
            texture_uv=blockuv(bid), atlas="blocks"
        )

    # fences
    fences = [
        (blocks.OAK_FENCE,    "Oak Fence"),
        (blocks.SPRUCE_FENCE, "Spruce Fence"),
        (blocks.BIRCH_FENCE,  "Birch Fence"),
        (blocks.JUNGLE_FENCE, "Jungle Fence"),
        (blocks.ACACIA_FENCE, "Acacia Fence"),
        (blocks.DARK_OAK_FENCE,     "Dark Oak Fence"),
        (blocks.NETHER_BRICK_FENCE, "Nether Brick Fence"),
    ]

    for bid, nm in fences:
        R.register(
            bid, nm, category=BUILDING, is_block=True,
            texture_uv=blockuv(bid), atlas="blocks"
        )

    # gates
    fence_gates = [
        (blocks.OAK_FENCE_GATE,    "Oak Fence Gate"),
        (blocks.SPRUCE_FENCE_GATE, "Spruce Fence Gate"),
        (blocks.BIRCH_FENCE_GATE,  "Birch Fence Gate"),
        (blocks.JUNGLE_FENCE_GATE, "Jungle Fence Gate"),
        (blocks.ACACIA_FENCE_GATE, "Acacia Fence Gate"),
        (blocks.DARK_OAK_FENCE_GATE, "Dark Oak Fence Gate"),
    ]

    for bid, nm in fence_gates:
        R.register(
            bid, nm, category=BUILDING, is_block=True,
            texture_uv=blockuv(bid), atlas="blocks"
        )

    # walls
    walls = [
        (blocks.COBBLESTONE_WALL, "Cobblestone Wall"),
        (blocks.MOSSY_COBBLESTONE_WALL, "Mossy Cobblestone Wall"),
    ]

    for bid, nm in walls:
        R.register(
            bid, nm, category=BUILDING, is_block=True,
            texture_uv=blockuv(bid), atlas="blocks"
        )

    # carpet
    carpet = [
        (blocks.CARPET_WHITE,  "White Carpet"),
        (blocks.CARPET_ORANGE, "Orange Carpet"),
        (blocks.CARPET_MAGENTA,    "Magenta Carpet"),
        (blocks.CARPET_LIGHT_BLUE, "Light Blue Carpet"),
        (blocks.CARPET_YELLOW, "Yellow Carpet"),
        (blocks.CARPET_LIME,   "Lime Carpet"),
        (blocks.CARPET_PINK,   "Pink Carpet"),
        (blocks.CARPET_GRAY,   "Gray Carpet"),
        (blocks.CARPET_SILVER, "Light Gray Carpet"),
        (blocks.CARPET_CYAN,   "Cyan Carpet"),
        (blocks.CARPET_PURPLE, "Purple Carpet"),
        (blocks.CARPET_BLUE,   "Blue Carpet"),
        (blocks.CARPET_BROWN,  "Brown Carpet"),
        (blocks.CARPET_GREEN,  "Green Carpet"),
        (blocks.CARPET_RED,    "Red Carpet"),
        (blocks.CARPET_BLACK,  "Black Carpet"),
    ]

    for bid, nm in carpet:
        R.register(
            bid, nm, category=DECORATION, is_block=True,
            texture_uv=blockuv(bid), atlas="blocks"
        )

    # saplings
    saplings = [
        (blocks.SAPLING_OAK,      "Oak Sapling"),
        (blocks.SAPLING_SPRUCE,   "Spruce Sapling"),
        (blocks.SAPLING_BIRCH,    "Birch Sapling"),
        (blocks.SAPLING_JUNGLE,   "Jungle Sapling"),
        (blocks.SAPLING_ACACIA,   "Acacia Sapling"),
        (blocks.SAPLING_DARK_OAK, "Dark Oak Sapling"),
    ]

    for bid, nm in saplings:
        R.register(
            bid, nm, category=NATURE, is_block=True,
            texture_uv=blockuv(bid), atlas="blocks", foliage_tint=True
        )

    # flowers
    flowers = [
        (blocks.DANDELION,    "Dandelion"),
        (blocks.POPPY,        "Poppy"),
        (blocks.BLUE_ORCHID,  "Blue Orchid"),
        (blocks.ALLIUM,       "Allium"),
        (blocks.AZURE_BLUET,  "Azure Bluet"),
        (blocks.RED_TULIP,    "Red Tulip"),
        (blocks.ORANGE_TULIP, "Orange Tulip"),
        (blocks.WHITE_TULIP,  "White Tulip"),
        (blocks.PINK_TULIP,   "Pink Tulip"),
        (blocks.OXEYE_DAISY,  "Oxeye Daisy"),
        (blocks.BROWN_MUSHROOM, "Brown Mushroom"),
        (blocks.RED_MUSHROOM,   "Red Mushroom"),
        (blocks.DEAD_BUSH,      "Dead Bush"),
        (blocks.FERN, "Fern"),
    ]

    for bid, nm in flowers:
        foliage = bid in (blocks.FERN,)
        R.register(
            bid, nm, category=NATURE, is_block=True,
            texture_uv=blockuv(bid), atlas="blocks", foliage_tint=foliage
        )

    # double plants
    double_plants = [
        (blocks.SUNFLOWER, "Sunflower"),
        (blocks.LILAC,     "Lilac"),
        (blocks.DOUBLE_TALLGRASS, "Double Tallgrass"),
        (blocks.LARGE_FERN, "Large Fern"),
        (blocks.ROSE_BUSH,  "Rose Bush"),
        (blocks.PEONY,      "Peony"),
    ]

    for bid, nm in double_plants:
        foliage = bid in (blocks.DOUBLE_TALLGRASS, blocks.LARGE_FERN)
        R.register(
            bid, nm, category=NATURE, is_block=True,
            texture_uv=blockuv(bid), atlas="blocks", foliage_tint=foliage
        )

    # rails
    rails = [
        (blocks.RAIL, "Rail"),
        (blocks.POWERED_RAIL,   "Powered Rail"),
        (blocks.DETECTOR_RAIL,  "Detector Rail"),
        (blocks.ACTIVATOR_RAIL, "Activator Rail"),
    ]

    for bid, nm in rails:
        R.register(
            bid, nm, category=DECORATION, is_block=True,
            texture_uv=blockuv(bid), atlas="blocks"
        )

    # torches
    torches = [
        (blocks.TORCH, "Torch"),
        (blocks.REDSTONE_TORCH_ON, "Redstone Torch"),
    ]

    for bid, nm in torches:
        R.register(
            bid, nm, category=DECORATION, is_block=True,
            texture_uv=blockuv(bid), atlas="blocks"
        )

    # doors
    doors = [
        (blocks.OAK_DOOR_BOTTOM,    "Oak Door"),
        (blocks.IRON_DOOR_BOTTOM,   "Iron Door"),
        (blocks.SPRUCE_DOOR_BOTTOM, "Spruce Door"),
        (blocks.BIRCH_DOOR_BOTTOM,  "Birch Door"),
        (blocks.JUNGLE_DOOR_BOTTOM, "Jungle Door"),
        (blocks.ACACIA_DOOR_BOTTOM, "Acacia Door"),
        (blocks.DARK_OAK_DOOR_BOTTOM, "Dark Oak Door"),
    ]

    for bid, nm in doors:
        R.register(
            bid, nm, category=BUILDING, is_block=True,
            texture_uv=blockuv(bid), atlas="blocks"
        )

    # trapdoors
    trapdoors = [
        (blocks.OAK_TRAPDOOR,  "Trapdoor"),
        (blocks.IRON_TRAPDOOR, "Iron Trapdoor"),
    ]

    for bid, nm in trapdoors:
        R.register(
            bid, nm, category=BUILDING, is_block=True,
            texture_uv=blockuv(bid), atlas="blocks"
        )

    # buttons && plates
    input_blocks = [
        (blocks.STONE_BUTTON,  "Stone Button"),
        (blocks.WOODEN_BUTTON, "Wooden Button"),
        (blocks.STONE_PRESSURE_PLATE,  "Stone Pressure Plate"),
        (blocks.WOODEN_PRESSURE_PLATE, "Wooden Pressure Plate"),
        (blocks.LIGHT_WEIGHTED_PRESSURE_PLATE, "Light Weighted Pressure Plate"),
        (blocks.HEAVY_WEIGHTED_PRESSURE_PLATE, "Heavy Weighted Pressure Plate"),
    ]

    for bid, nm in input_blocks:
        R.register(
            bid, nm, category=DECORATION, is_block=True,
            texture_uv=blockuv(bid), atlas="blocks"
        )

    # ladder
    R.register(
        blocks.LADDER, "Ladder", category=BUILDING, is_block=True,
        texture_uv=blocks.blockuvs(blocks.LADDER)[0], atlas="blocks"
    )

    # tech stuff
    tech_blocks = [
        (blocks.LEVER, "Lever"),
        (blocks.TRIPWIRE_HOOK,     "Tripwire Hook"),
        (blocks.DAYLIGHT_DETECTOR, "Daylight Detector"),
        (blocks.COBWEB,   "Cobweb"),
        (blocks.VINE,     "Vines"),
        (blocks.LILY_PAD, "Lily Pad"),
    ]

    for bid, nm in tech_blocks:
        foliage = bid in (blocks.VINE, blocks.LILY_PAD)
        R.register(
            bid, nm, category=DECORATION, is_block=True,
            texture_uv=blockuv(bid), atlas="blocks", foliage_tint=foliage
        )

    # mushroom
    mushroom_blocks = [
        (blocks.BROWN_MUSHROOM_BLOCK, "Brown Mushroom Block"),
        (blocks.RED_MUSHROOM_BLOCK,   "Red Mushroom Block"),
    ]

    for bid, nm in mushroom_blocks:
        R.register(
            bid, nm, category=BUILDING, is_block=True,
            texture_uv=blockuv(bid), atlas="blocks"
        )

    # bars && panes
    panes = [
        (blocks.IRON_BARS,  "Iron Bars"),
        (blocks.GLASS_PANE, "Glass Pane"),
    ]

    for bid, nm in panes:
        R.register(
            bid, nm, category=BUILDING, is_block=True,
            texture_uv=blockuv(bid), atlas="blocks"
        )

    # stained panes
    glass_panes = [
        (blocks.GLASS_PANE_WHITE,      "White Glass Pane"),
        (blocks.GLASS_PANE_ORANGE,     "Orange Glass Pane"),
        (blocks.GLASS_PANE_MAGENTA,    "Magenta Glass Pane"),
        (blocks.GLASS_PANE_LIGHT_BLUE, "Light Blue Glass Pane"),
        (blocks.GLASS_PANE_YELLOW,     "Yellow Glass Pane"),
        (blocks.GLASS_PANE_LIME,       "Lime Glass Pane"),
        (blocks.GLASS_PANE_PINK,       "Pink Glass Pane"),
        (blocks.GLASS_PANE_GRAY,       "Gray Glass Pane"),
        (blocks.GLASS_PANE_SILVER,     "Light Gray Glass Pane"),
        (blocks.GLASS_PANE_CYAN,       "Cyan Glass Pane"),
        (blocks.GLASS_PANE_PURPLE,     "Purple Glass Pane"),
        (blocks.GLASS_PANE_BLUE,       "Blue Glass Pane"),
        (blocks.GLASS_PANE_BROWN,      "Brown Glass Pane"),
        (blocks.GLASS_PANE_GREEN,      "Green Glass Pane"),
        (blocks.GLASS_PANE_RED,        "Red Glass Pane"),
        (blocks.GLASS_PANE_BLACK,      "Black Glass Pane"),
    ]

    for bid, nm in glass_panes:
        R.register(
            bid, nm, category=DECORATION, is_block=True,
            texture_uv=blockuv(bid), atlas="blocks"
        )

    # pistons
    pistons = [
        (blocks.PISTON, "Piston"),
        (blocks.STICKY_PISTON, "Sticky Piston"),
    ]

    for bid, nm in pistons:
        R.register(
            bid, nm, category=DECORATION, is_block=True,
            texture_uv=blockuv(bid), atlas="blocks"
        )

    # dispensers & droppers
    dispensers = [
        (blocks.DISPENSER, "Dispenser"),
        (blocks.DROPPER, "Dropper"),
    ]

    for bid, nm in dispensers:
        R.register(
            bid, nm, category=DECORATION, is_block=True,
            texture_uv=blockuv(bid), atlas="blocks"
        )

    # chests
    chests = [
        (blocks.CHEST, "Chest"),
        (blocks.TRAPPED_CHEST, "Trapped Chest"),
        (blocks.ENDER_CHEST, "Ender Chest"),
    ]

    for bid, nm in chests:
        R.register(
            bid, nm, category=DECORATION, is_block=True,
            texture_uv=blockuv(bid), atlas="blocks"
        )

    # misc special
    special_blocks = [
        (blocks.ENCHANTING_TABLE, "Enchanting Table"),
        (blocks.ANVIL, "Anvil"),
        (blocks.END_PORTAL_FRAME, "End Portal Frame"),
    ]

    for bid, nm in special_blocks:
        R.register(
            bid, nm, category=DECORATION, is_block=True,
            texture_uv=blockuv(bid), atlas="blocks"
        )

    
    
    
    R.register(
        blocks.FARMLAND_DRY, "Farmland", category=NATURE, is_block=True,
        texture_uv=blocks.blockuvs(blocks.FARMLAND_DRY)[0], atlas="blocks"
    )

    
    R.register(
        blocks.SUGAR_CANE, "Sugar Cane (Block)", category=NATURE, is_block=True,
        texture_uv=blocks.blockuvs(blocks.SUGAR_CANE)[0], atlas="blocks", foliage_tint=True
    )

    
    R.register(
        blocks.BED_FOOT, "Bed", category=DECORATION, is_block=True,
        texture_uv=blocks.blockuvs(blocks.BED_FOOT)[0], atlas="blocks"
    )

    
    R.register(
        blocks.SIGN_STANDING, "Sign (Block)", category=DECORATION, is_block=True,
        texture_uv=blocks.blockuvs(blocks.SIGN_STANDING)[0], atlas="blocks"
    )

    # animated
    animated_blocks = [
        (blocks.LAVA, "Lava"),
        (blocks.FIRE, "Fire"),
        (blocks.FURNACE_ON, "Lit Furnace"),
        (blocks.WATER_FLOWING, "Flowing Water"),
        (blocks.LAVA_FLOWING, "Flowing Lava"),
    ]

    for bid, nm in animated_blocks:
        R.register(
            bid, nm, category=MISC, is_block=True,
            texture_uv=blockuv(bid), atlas="blocks"
        )


def regitems():
    R = REGISTRY
    T = textures

    food = [
        (T.APPLE, "Apple"),
        (T.GOLDEN_APPLE, "Golden Apple"),
        (T.BREAD, "Bread"),
        (T.COOKED_BEEF, "Steak"),
        (T.RAW_BEEF, "Raw Beef"),
        (T.COOKED_CHICKEN, "Cooked Chicken"),
        (T.RAW_CHICKEN, "Raw Chicken"),
        (T.COOKED_PORKCHOP, "Cooked Porkchop"),
        (T.RAW_PORKCHOP, "Raw Porkchop"),
        (T.COOKIE, "Cookie"),
        (T.MELON_SLICE, "Melon Slice"),
        (T.CARROT, "Carrot"),
        (T.GOLDEN_CARROT, "Golden Carrot"),
        (T.POTATO, "Potato"),
        (T.BAKED_POTATO, "Baked Potato"),
        (T.PUMPKIN_PIE, "Pumpkin Pie"),
        (T.ROTTEN_FLESH, "Rotten Flesh"),
        (T.COOKED_FISH, "Cooked Fish"),
        (T.RAW_FISH, "Raw Fish"),
    ]

    for iid, nm in food:
        R.register(
            iid, nm, category=FOOD, is_block=False,
            texture_uv=T.getuv(iid), atlas="items"
        )

    R.register(
        T.CAKE, "Cake", category=FOOD, is_block=False,
        max_stack=1, texture_uv=T.getuv(T.CAKE), atlas="items",
        places_block=blocks.CAKE
    )

    materials = [
        (T.DIAMOND, "Diamond"),
        (T.EMERALD, "Emerald"),
        (T.GOLD_INGOT, "Gold Ingot"),
        (T.GOLD_NUGGET, "Gold Nugget"),
        (T.IRON_INGOT, "Iron Ingot"),
        (T.COAL, "Coal"),
        (T.CHARCOAL, "Charcoal"),
        # (T.REDSTONE, "Redstone"),
        (T.QUARTZ, "Nether Quartz"),
        (T.STICK, "Stick"),
        (T.STRING, "String"),
        (T.LEATHER, "Leather"),
        (T.FEATHER, "Feather"),
        (T.BONE, "Bone"),
        (T.FLINT, "Flint"),
        (T.PAPER, "Paper"),
        (T.SLIMEBALL, "Slimeball"),
        (T.GUNPOWDER, "Gunpowder"),
        (T.GLOWSTONE_DUST, "Glowstone Dust"),
        (T.SUGAR, "Sugar"),
        (T.BLAZE_ROD, "Blaze Rod"),
        (T.BLAZE_POWDER, "Blaze Powder"),
        (T.GHAST_TEAR, "Ghast Tear"),
        (T.MAGMA_CREAM, "Magma Cream"),
        (T.ENDER_PEARL, "Ender Pearl"),
        (T.ENDER_EYE, "Eye of Ender"),
        (T.NETHER_STAR, "Nether Star"),
        (T.PRISMARINE_SHARD, "Prismarine Shard"),
        (T.PRISMARINE_CRYSTALS, "Prismarine Crystals"),
        (T.BRICK, "Brick"),
        (T.CLAY_BALL, "Clay Ball"),
        (T.NETHER_WART, "Nether Wart"),
        (T.SUGAR_CANE, "Sugar Cane"),
        (T.SPIDER_EYE, "Spider Eye"),
    ]

    for iid, nm in materials:
        stack = 16 if iid == T.ENDER_PEARL else 64
        R.register(
            iid, nm, category=MATERIALS, is_block=False,
            max_stack=stack, texture_uv=T.getuv(iid), atlas="items"
        )

    tools = [
        (T.DIAMOND_PICKAXE, "Diamond Pickaxe", "pickaxe"),
        (T.DIAMOND_AXE, "Diamond Axe", "axe"),
        (T.DIAMOND_SHOVEL, "Diamond Shovel", "shovel"),
        (T.DIAMOND_HOE, "Diamond Hoe", "hoe"),
        (T.IRON_PICKAXE, "Iron Pickaxe", "pickaxe"),
        (T.IRON_AXE, "Iron Axe", "axe"),
        (T.IRON_SHOVEL, "Iron Shovel", "shovel"),
        (T.IRON_HOE, "Iron Hoe", "hoe"),
        (T.GOLD_PICKAXE, "Golden Pickaxe", "pickaxe"),
        (T.GOLD_AXE, "Golden Axe", "axe"),
        (T.GOLD_SHOVEL, "Golden Shovel", "shovel"),
        (T.GOLD_HOE, "Golden Hoe", "hoe"),
        (T.STONE_PICKAXE, "Stone Pickaxe", "pickaxe"),
        (T.STONE_AXE, "Stone Axe", "axe"),
        (T.STONE_SHOVEL, "Stone Shovel", "shovel"),
        (T.STONE_HOE, "Stone Hoe", "hoe"),
        (T.WOOD_PICKAXE, "Wooden Pickaxe", "pickaxe"),
        (T.WOOD_AXE, "Wooden Axe", "axe"),
        (T.WOOD_SHOVEL, "Wooden Shovel", "shovel"),
        (T.WOOD_HOE, "Wooden Hoe", "hoe"),
    ]

    for iid, nm, tool in tools:
        R.register(
            iid, nm, category=TOOLS, is_block=False,
            max_stack=1, tool_type=tool, texture_uv=T.getuv(iid), atlas="items"
        )

    combat = [
        (T.DIAMOND_SWORD, "Diamond Sword", 7),
        (T.IRON_SWORD, "Iron Sword", 6),
        (T.GOLD_SWORD, "Golden Sword", 4),
        (T.STONE_SWORD, "Stone Sword", 5),
        (T.WOOD_SWORD, "Wooden Sword", 4),
        (T.BOW, "Bow", 0),
        (T.ARROW, "Arrow", 0),
    ]

    for iid, nm, dmg in combat:
        stack = 64 if iid == T.ARROW else 1
        R.register(
            iid, nm, category=COMBAT, is_block=False,
            max_stack=stack, damage=dmg, texture_uv=T.getuv(iid), atlas="items"
        )

    armor = [
        (T.DIAMOND_HELMET, "Diamond Helmet"),
        (T.DIAMOND_CHESTPLATE, "Diamond Chestplate"),
        (T.DIAMOND_LEGGINGS, "Diamond Leggings"),
        (T.DIAMOND_BOOTS, "Diamond Boots"),
        (T.GOLD_HELMET, "Golden Helmet"),
        (T.GOLD_CHESTPLATE, "Golden Chestplate"),
        (T.GOLD_LEGGINGS, "Golden Leggings"),
        (T.GOLD_BOOTS, "Golden Boots"),
        (T.IRON_HELMET, "Iron Helmet"),
        (T.IRON_CHESTPLATE, "Iron Chestplate"),
        (T.IRON_LEGGINGS, "Iron Leggings"),
        (T.IRON_BOOTS, "Iron Boots"),
    ]

    for iid, nm in armor:
        R.register(
            iid, nm, category=COMBAT, is_block=False,
            max_stack=1, texture_uv=T.getuv(iid), atlas="items"
        )

    armor_more = [
        (T.CHAINMAIL_HELMET, "Chainmail Helmet"),
        (T.CHAINMAIL_CHESTPLATE, "Chainmail Chestplate"),
        (T.CHAINMAIL_LEGGINGS, "Chainmail Leggings"),
        (T.CHAINMAIL_BOOTS, "Chainmail Boots"),
        (T.LEATHER_HELMET, "Leather Cap"),
        (T.LEATHER_CHESTPLATE, "Leather Tunic"),
        (T.LEATHER_LEGGINGS, "Leather Pants"),
        (T.LEATHER_BOOTS, "Leather Boots"),
    ]

    for iid, nm in armor_more:
        R.register(
            iid, nm, category=COMBAT, is_block=False,
            max_stack=1, texture_uv=T.getuv(iid), atlas="items"
        )

    misc_tools = [
        (T.FISHING_ROD, "Fishing Rod", 1),
        (T.FLINT_AND_STEEL, "Flint and Steel", 1),
        (T.SHEARS, "Shears", 1),
        (T.COMPASS, "Compass", 64),
        (T.CLOCK, "Clock", 64),
        (T.BUCKET, "Bucket", 16),
        (T.MILK_BUCKET, "Milk Bucket", 1),
        (T.NAME_TAG, "Name Tag", 64),
        (T.LEAD, "Lead", 64),
        (T.CARROT_ON_A_STICK, "Carrot on a Stick", 1),
    ]

    for iid, nm, stack in misc_tools:
        R.register(
            iid, nm, category=TOOLS, is_block=False,
            max_stack=stack, texture_uv=T.getuv(iid), atlas="items"
        )

    R.register(
        T.WATER_BUCKET, "Water Bucket", category=TOOLS, is_block=False,
        max_stack=1, texture_uv=T.getuv(T.WATER_BUCKET), atlas="items",
        places_block=blocks.WATER
    )
    R.register(
        T.LAVA_BUCKET, "Lava Bucket", category=TOOLS, is_block=False,
        max_stack=1, texture_uv=T.getuv(T.LAVA_BUCKET), atlas="items",
        places_block=blocks.LAVA
    )

    misc = [
        (T.EGG, "Egg", 16),
        (T.SNOWBALL, "Snowball", 16),
        (T.BOOK, "Book", 64),
        (T.BOWL, "Bowl", 64),
        (T.WHEAT, "Wheat", 64),
        (T.WHEAT_SEEDS, "Wheat Seeds", 64),
        (T.MELON_SEEDS, "Melon Seeds", 64),
        (T.PUMPKIN_SEEDS, "Pumpkin Seeds", 64),
        (T.SADDLE, "Saddle", 1),
        (T.BOAT, "Boat", 1),
        (T.SIGN, "Sign", 16),
        (T.BED, "Bed", 1),
        (T.EXPERIENCE_BOTTLE, "Bottle o' Enchanting", 64),
    ]

    for iid, nm, stack in misc:
        R.register(
            iid, nm, category=MISC, is_block=False,
            max_stack=stack, texture_uv=T.getuv(iid), atlas="items"
        )
        
    # this is getting annoying...

    # dyes
    dyes = [
        (T.DYE_BLACK, "Ink Sac"), 
        (T.DYE_RED, "Rose Red"), 
        (T.DYE_GREEN, "Cactus Green"),
        (T.DYE_BROWN, "Cocoa Beans"), 
        (T.DYE_BLUE, "Lapis Lazuli"), 
        (T.DYE_PURPLE, "Purple Dye"),
        (T.DYE_CYAN, "Cyan Dye"), 
        (T.DYE_LIGHT_BLUE, "Light Blue Dye"), 
        (T.DYE_GRAY, "Gray Dye"),
        (T.DYE_PINK, "Pink Dye"), 
        (T.DYE_LIME, "Lime Dye"), 
        (T.DYE_YELLOW, "Dandelion Yellow"),
        (T.DYE_LIGHT_BLUE, "Light Blue Dye"), 
        (T.DYE_MAGENTA, "Magenta Dye"), 
        (T.DYE_ORANGE, "Orange Dye"),
        (T.DYE_SILVER, "Light Gray Dye"), 
        (T.DYE_WHITE, "Bone Meal")
    ]
    for iid, nm in dyes:
        if not R.exists(iid):
            R.register(
                iid, nm, category=MATERIALS, is_block=False, 
                texture_uv=T.getuv(iid), atlas="items"
            )

    # records
    records = [
        (T.RECORD_13, "13"), 
        (T.RECORD_CAT, "Cat"), 
        (T.RECORD_BLOCKS, "Blocks"), 
        (T.RECORD_CHIRP, "Chirp"),
        (T.RECORD_FAR, "Far"), 
        (T.RECORD_MALL, "Mall"), 
        (T.RECORD_MELLOHI, "Mellohi"), 
        (T.RECORD_STAL, "Stal"),
        (T.RECORD_STRAD, "Strad"), 
        (T.RECORD_WARD, "Ward"), 
        (T.RECORD_11, "11"), 
        (T.RECORD_WAIT, "Wait")
    ]
    for iid, nm in records:
        R.register(
            iid, f"Disc {nm}", category=MISC, is_block=False, 
            max_stack=1, texture_uv=T.getuv(iid), atlas="items"
        )

    # minecarts
    minecarts = [
        (T.MINECART, "Minecart"), 
        (T.MINECART_CHEST, "Minecart with Chest"), 
        (T.MINECART_FURNACE, "Minecart with Furnace"),
        (T.MINECART_TNT, "Minecart with TNT"), 
        (T.MINECART_HOPPER, "Minecart with Hopper"), 
        (T.MINECART_COMMAND_BLOCK, "Minecart with Command Block")
    ]
    for iid, nm in minecarts:
        R.register(
            iid, nm, category=MISC, is_block=False, 
            max_stack=1, texture_uv=T.getuv(iid), atlas="items"
        )

    # extra food
    food_more = [
        (T.MUTTON_RAW, "Raw Mutton"), 
        (T.MUTTON_COOKED, "Cooked Mutton"),
        (T.RABBIT_RAW, "Raw Rabbit"), 
        (T.RABBIT_COOKED, "Cooked Rabbit"), 
        (T.RABBIT_STEW, "Rabbit Stew"),
        (T.PUFFERFISH, "Pufferfish"), 
        (T.MELON_SPECKLED, "Glistering Melon"), 
        (T.POISONOUS_POTATO, "Poisonous Potato"),
        (T.MUSHROOM_STEW, "Mushroom Stew")
    ]
    for iid, nm in food_more:
        stack = 1 if "Stew" in nm else 64
        R.register(
            iid, nm, category=FOOD, is_block=False, 
            max_stack=stack, texture_uv=T.getuv(iid), atlas="items"
        )

    # extra misc
    misc_extra = [
        (T.POTION_DRINKABLE, "Potion"), 
        (T.POTION_SPLASH, "Splash Potion"), 
        (T.POTION_EMPTY, "Glass Bottle"),
        (T.FIREBALL, "Fire Charge"), 
        (T.FIREWORKS, "Firework Rocket"), 
        (T.FIREWORKS_CHARGE, "Firework Star"),
        (T.SPAWN_EGG, "Spawn Egg"), 
        # (T.ITEM_FRAME, "Item Frame"),
        (T.FLOWER_POT, "Flower Pot"),
        (T.NETHERBRICK_ITEM, "Nether Brick"), 
        (T.FERMENTED_SPIDER_EYE, "Fermented Spider Eye"),
        (T.ENCHANTED_BOOK, "Enchanted Book"), 
        (T.WRITTEN_BOOK, "Written Book"), 
        (T.WRITABLE_BOOK, "Book and Quill"),
        (T.DOOR_WOOD, "Oak Door"), 
        (T.DOOR_IRON, "Iron Door"), 
        (T.HORSE_ARMOR_DIAMOND, "Diamond Horse Armor"),
        (T.HORSE_ARMOR_GOLD, "Gold Horse Armor"), 
        (T.HORSE_ARMOR_IRON, "Iron Horse Armor")
    ]
    for iid, nm in misc_extra:
        stack = 1 if "Door" in nm or "Potion" in nm or "Book" in nm or "Horse Armor" in nm else 64
        R.register(
            iid, nm, category=MISC, is_block=False, 
            max_stack=stack, texture_uv=T.getuv(iid), atlas="items"
        )

    # last
    missing_items = [
        (T.RABBIT_HIDE, "Rabbit Hide"),
        (T.MAP_EMPTY, "Empty Map"), 
        (T.PAINTING, "Painting"),
        (T.DOOR_SPRUCE, "Spruce Door"), 
        (T.DOOR_BIRCH, "Birch Door"), 
        (T.DOOR_JUNGLE, "Jungle Door"),
        (T.DOOR_ACACIA, "Acacia Door"), 
        (T.DOOR_DARK_OAK, "Dark Oak Door")
    ]
    for iid, nm in missing_items:
        stack = 1 if "Door" in nm else 64
        R.register(
            iid, nm, category=MISC, is_block=False, 
            max_stack=stack, texture_uv=T.getuv(iid), atlas="items"
        )

    R.register(
        T.BREWING_STAND, "Brewing Stand", category=DECORATION, is_block=False,
        max_stack=64, texture_uv=T.getuv(T.BREWING_STAND), atlas="items",
        places_block=blocks.BREWING_STAND_BLOCK
    )
    R.register(
        T.HOPPER, "Hopper", category=DECORATION, is_block=False,
        max_stack=64, texture_uv=T.getuv(T.HOPPER), atlas="items",
        places_block=blocks.HOPPER
    )
    R.register(
        T.CAULDRON, "Cauldron", category=DECORATION, is_block=False,
        max_stack=64, texture_uv=T.getuv(T.CAULDRON), atlas="items",
        places_block=blocks.CAULDRON
    )
    R.register(
        T.REPEATER, "Redstone Repeater", category=DECORATION, is_block=False,
        max_stack=64, texture_uv=T.getuv(T.REPEATER), atlas="items",
        places_block=blocks.REPEATER
    )
    R.register(
        T.COMPARATOR, "Redstone Comparator", category=DECORATION, is_block=False,
        max_stack=64, texture_uv=T.getuv(T.COMPARATOR), atlas="items",
        places_block=blocks.COMPARATOR
    )
    R.register(
        T.BARRIER, "Barrier", category=MISC, is_block=False,
        max_stack=64, texture_uv=T.getuv(T.BARRIER), atlas="items",
        places_block=blocks.BARRIER
    )

    R.register(
        T.REDSTONE, "Redstone Dust", category=MATERIALS, is_block=False,
        max_stack=64, texture_uv=T.getuv(T.REDSTONE), atlas="items",
        places_block=blocks.REDSTONE_WIRE
    )

    R.register(
        T.ITEM_FRAME, "Item Frame", category=DECORATION, is_block=False,
        max_stack=64, texture_uv=T.getuv(T.ITEM_FRAME), atlas="items",
        places_block=blocks.ITEM_FRAME_BLOCK
    )


regblocks()
regitems()
