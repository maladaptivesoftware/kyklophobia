import numpy as np
import _respath

from world.blocks import (
    TEXTURES, UV_W, UV_H,
    WATER, WATER_FLOWING, CACTUS, BARRIER, HOPPER, CAULDRON,
    CAKE, REPEATER, COMPARATOR, REDSTONE_WIRE, ITEM_FRAME_BLOCK,
    BREWING_STAND_BLOCK,
    # doors
    OAK_DOOR_BOTTOM, OAK_DOOR_TOP, IRON_DOOR_BOTTOM, IRON_DOOR_TOP,
    SPRUCE_DOOR_BOTTOM, SPRUCE_DOOR_TOP, BIRCH_DOOR_BOTTOM, BIRCH_DOOR_TOP,
    JUNGLE_DOOR_BOTTOM, JUNGLE_DOOR_TOP, ACACIA_DOOR_BOTTOM, ACACIA_DOOR_TOP,
    DARK_OAK_DOOR_BOTTOM, DARK_OAK_DOOR_TOP,
    # beds
    BED_HEAD, BED_FOOT,
    # saplings
    SAPLING_OAK, SAPLING_SPRUCE, SAPLING_BIRCH, SAPLING_JUNGLE,
    SAPLING_ACACIA, SAPLING_DARK_OAK,
    # rails
    RAIL, POWERED_RAIL, POWERED_RAIL_ON, DETECTOR_RAIL, ACTIVATOR_RAIL,
    # torches
    TORCH, REDSTONE_TORCH_OFF, REDSTONE_TORCH_ON,
    # stairs
    OAK_STAIRS, SPRUCE_STAIRS, BIRCH_STAIRS, JUNGLE_STAIRS, ACACIA_STAIRS,
    DARK_OAK_STAIRS, STONE_STAIRS, COBBLESTONE_STAIRS, BRICK_STAIRS,
    STONE_BRICK_STAIRS, NETHER_BRICK_STAIRS, SANDSTONE_STAIRS,
    QUARTZ_STAIRS, RED_SANDSTONE_STAIRS,
    # slabs
    STONE_SLAB, SANDSTONE_SLAB, COBBLESTONE_SLAB, BRICK_SLAB,
    STONE_BRICK_SLAB, NETHER_BRICK_SLAB, QUARTZ_SLAB, OAK_SLAB,
    SPRUCE_SLAB, BIRCH_SLAB, JUNGLE_SLAB, ACACIA_SLAB,
    DARK_OAK_SLAB, RED_SANDSTONE_SLAB,
    # misc custom geometry
    COBWEB, LEVER, TRIPWIRE_HOOK, DAYLIGHT_DETECTOR, DAYLIGHT_DETECTOR_INVERTED,
    IRON_BARS, GLASS_PANE, VINE, LILY_PAD, ENCHANTING_TABLE,
    ANVIL, ANVIL_SLIGHTLY_DAMAGED, ANVIL_VERY_DAMAGED, END_PORTAL_FRAME,
    # colored glass panes
    GLASS_PANE_WHITE, GLASS_PANE_ORANGE, GLASS_PANE_MAGENTA, GLASS_PANE_LIGHT_BLUE,
    GLASS_PANE_YELLOW, GLASS_PANE_LIME, GLASS_PANE_PINK, GLASS_PANE_GRAY,
    GLASS_PANE_SILVER, GLASS_PANE_CYAN, GLASS_PANE_PURPLE, GLASS_PANE_BLUE,
    GLASS_PANE_BROWN, GLASS_PANE_GREEN, GLASS_PANE_RED, GLASS_PANE_BLACK,
    # flowers & cross plants
    DANDELION, POPPY, BLUE_ORCHID, ALLIUM, AZURE_BLUET,
    RED_TULIP, ORANGE_TULIP, WHITE_TULIP, PINK_TULIP, OXEYE_DAISY,
    BROWN_MUSHROOM, RED_MUSHROOM, DEAD_BUSH, FERN,
    SUNFLOWER, LILAC, DOUBLE_TALLGRASS, LARGE_FERN, ROSE_BUSH, PEONY,
    TALLGRASS, SUGAR_CANE,
    # custom geometry blocks
    FIRE, SNOW, DRAGON_EGG,
    OAK_FENCE, SPRUCE_FENCE, BIRCH_FENCE, JUNGLE_FENCE, ACACIA_FENCE, DARK_OAK_FENCE, NETHER_BRICK_FENCE,
    OAK_FENCE_GATE, SPRUCE_FENCE_GATE, BIRCH_FENCE_GATE, JUNGLE_FENCE_GATE, ACACIA_FENCE_GATE, DARK_OAK_FENCE_GATE,
    COBBLESTONE_WALL, MOSSY_COBBLESTONE_WALL,
    STONE_BUTTON, WOODEN_BUTTON,
    STONE_PRESSURE_PLATE, WOODEN_PRESSURE_PLATE, LIGHT_WEIGHTED_PRESSURE_PLATE, HEAVY_WEIGHTED_PRESSURE_PLATE,
    OAK_TRAPDOOR, IRON_TRAPDOOR,
    LADDER,
    CHEST, TRAPPED_CHEST, ENDER_CHEST,
    CARPET_WHITE, CARPET_ORANGE, CARPET_MAGENTA, CARPET_LIGHT_BLUE,
    CARPET_YELLOW, CARPET_LIME, CARPET_PINK, CARPET_GRAY,
    CARPET_SILVER, CARPET_CYAN, CARPET_PURPLE, CARPET_BLUE,
    CARPET_BROWN, CARPET_GREEN, CARPET_RED, CARPET_BLACK,
)

MODE_SOLID       = 0
MODE_TRANSPARENT = 1
MODE_CUSTOM      = 2
MODE_FLAT        = 3
MODE_INVISIBLE   = 4
MODE_EXTRUDED    = 5

from world.renderers.geom import (
    UV_MODE_POS, UV_MODE_IDX, UV_MODE_MODEL,
    MAX_ELEMS, MAX_CUSTOM,
    elemfaces, flattenelems, faceuv8,
    load_model, modeljson, extrflat,
    atlasuv, resolvtex, rotelem,
)



CACTUS_ELEMS, CACTUS_UV, CACTUS_CULL, CACTUS_FUVS = load_model("cactus")
CAKE_ELEMS, CAKE_UV, CAKE_CULL, CAKE_FUVS = load_model("cake")
REPEATER_ELEMS, REPEATER_UV, REPEATER_CULL, REPEATER_FUVS = load_model("repeater")
COMPARATOR_ELEMS, COMPARATOR_UV, COMPARATOR_CULL, COMPARATOR_FUVS = load_model("comparator")
HOPPER_ELEMS, HOPPER_UV, HOPPER_CULL, HOPPER_FUVS = load_model("hopper")
CAULDRON_ELEMS, CAULDRON_UV, CAULDRON_CULL, CAULDRON_FUVS = load_model("cauldron")

SLAB_ELEMS, SLAB_UV, SLAB_CULL, SLAB_FUVS = load_model("slab")
STAIR_ELEMS, STAIR_UV, STAIR_CULL, STAIR_FUVS = load_model("stair")
DOOR_ELEMS, DOOR_UV, DOOR_CULL, DOOR_FUVS = load_model("door")
BED_ELEMS, BED_UV, BED_CULL, BED_FUVS = load_model("bed")
SAPLING_ELEMS, SAPLING_UV, SAPLING_CULL, SAPLING_FUVS = load_model("sapling")
RAIL_ELEMS, RAIL_UV, RAIL_CULL, RAIL_FUVS = load_model("rail")
TORCH_ELEMS, TORCH_UV, TORCH_CULL, TORCH_FUVS = load_model("torch")
LEVER_ELEMS, LEVER_UV, LEVER_CULL, LEVER_FUVS = load_model("lever")
TRIPWIRE_HOOK_ELEMS, TRIPWIRE_HOOK_UV, TRIPWIRE_HOOK_CULL, TRIPWIRE_HOOK_FUVS = load_model("tripwire_hook")
DAYLIGHT_DETECTOR_ELEMS, DAYLIGHT_DETECTOR_UV, DAYLIGHT_DETECTOR_CULL, DAYLIGHT_DETECTOR_FUVS = load_model("daylight_detector")
IRON_BARS_ELEMS, IRON_BARS_UV, IRON_BARS_CULL, IRON_BARS_FUVS = load_model("iron_bars")
COBWEB_ELEMS, COBWEB_UV, COBWEB_CULL, COBWEB_FUVS = load_model("cobweb")
GLASS_PANE_ELEMS, GLASS_PANE_UV, GLASS_PANE_CULL, GLASS_PANE_FUVS = load_model("glass_pane")
VINE_ELEMS, VINE_UV, VINE_CULL, VINE_FUVS = load_model("vine")
LILY_PAD_ELEMS, LILY_PAD_UV, LILY_PAD_CULL, LILY_PAD_FUVS = load_model("lily_pad")
ENCHANTING_TABLE_ELEMS, ENCHANTING_TABLE_UV, ENCHANTING_TABLE_CULL, ENCHANTING_TABLE_FUVS = load_model("enchanting_table")
END_PORTAL_FRAME_ELEMS, END_PORTAL_FRAME_UV, END_PORTAL_FRAME_CULL, END_PORTAL_FRAME_FUVS = load_model("end_portal_frame")
ANVIL_ELEMS, ANVIL_UV, ANVIL_CULL, ANVIL_FUVS = load_model("anvil")
BREWING_STAND_ELEMS, BREWING_STAND_UV, BREWING_STAND_CULL, BREWING_STAND_FUVS = load_model("brewing_stand")

REDSTONE_EXTRUDED_ELEMS = extrflat("redstone_dust_dot", depth=0.0625)
CUBE_ELEMS = [elemfaces([0, 0, 0], [16, 16, 16])]

CUSTOM_BLOCKS = {
    WATER: (MODE_TRANSPARENT, CUBE_ELEMS, UV_MODE_POS, False, None),
    WATER_FLOWING: (MODE_TRANSPARENT, CUBE_ELEMS, UV_MODE_POS, False, None),
    CACTUS: (MODE_CUSTOM, CACTUS_ELEMS, CACTUS_UV, CACTUS_CULL, CACTUS_FUVS),
    BARRIER: (MODE_INVISIBLE, CUBE_ELEMS, UV_MODE_POS, False, None),
    HOPPER: (MODE_CUSTOM, HOPPER_ELEMS, HOPPER_UV, HOPPER_CULL, HOPPER_FUVS),
    CAULDRON: (MODE_CUSTOM, CAULDRON_ELEMS, CAULDRON_UV, CAULDRON_CULL, CAULDRON_FUVS),
    CAKE: (MODE_CUSTOM, CAKE_ELEMS, CAKE_UV, CAKE_CULL, CAKE_FUVS),
    REPEATER: (MODE_FLAT, REPEATER_ELEMS, REPEATER_UV, REPEATER_CULL, REPEATER_FUVS),
    COMPARATOR: (MODE_FLAT, COMPARATOR_ELEMS, COMPARATOR_UV, COMPARATOR_CULL, COMPARATOR_FUVS),
    REDSTONE_WIRE: (MODE_FLAT, [elemfaces([0, 0, 0], [16, 1, 16])], UV_MODE_MODEL, False, None),

    # doors
    OAK_DOOR_BOTTOM: (MODE_CUSTOM, DOOR_ELEMS, DOOR_UV, DOOR_CULL, DOOR_FUVS),
    OAK_DOOR_TOP: (MODE_CUSTOM, DOOR_ELEMS, DOOR_UV, DOOR_CULL, DOOR_FUVS),
    IRON_DOOR_BOTTOM: (MODE_CUSTOM, DOOR_ELEMS, DOOR_UV, DOOR_CULL, DOOR_FUVS),
    IRON_DOOR_TOP: (MODE_CUSTOM, DOOR_ELEMS, DOOR_UV, DOOR_CULL, DOOR_FUVS),
    SPRUCE_DOOR_BOTTOM: (MODE_CUSTOM, DOOR_ELEMS, DOOR_UV, DOOR_CULL, DOOR_FUVS),
    SPRUCE_DOOR_TOP: (MODE_CUSTOM, DOOR_ELEMS, DOOR_UV, DOOR_CULL, DOOR_FUVS),
    BIRCH_DOOR_BOTTOM: (MODE_CUSTOM, DOOR_ELEMS, DOOR_UV, DOOR_CULL, DOOR_FUVS),
    BIRCH_DOOR_TOP: (MODE_CUSTOM, DOOR_ELEMS, DOOR_UV, DOOR_CULL, DOOR_FUVS),
    JUNGLE_DOOR_BOTTOM: (MODE_CUSTOM, DOOR_ELEMS, DOOR_UV, DOOR_CULL, DOOR_FUVS),
    JUNGLE_DOOR_TOP: (MODE_CUSTOM, DOOR_ELEMS, DOOR_UV, DOOR_CULL, DOOR_FUVS),
    ACACIA_DOOR_BOTTOM: (MODE_CUSTOM, DOOR_ELEMS, DOOR_UV, DOOR_CULL, DOOR_FUVS),
    ACACIA_DOOR_TOP: (MODE_CUSTOM, DOOR_ELEMS, DOOR_UV, DOOR_CULL, DOOR_FUVS),
    DARK_OAK_DOOR_BOTTOM: (MODE_CUSTOM, DOOR_ELEMS, DOOR_UV, DOOR_CULL, DOOR_FUVS),
    DARK_OAK_DOOR_TOP: (MODE_CUSTOM, DOOR_ELEMS, DOOR_UV, DOOR_CULL, DOOR_FUVS),

    # beds
    BED_HEAD: (MODE_CUSTOM, BED_ELEMS, BED_UV, BED_CULL, BED_FUVS),
    BED_FOOT: (MODE_CUSTOM, BED_ELEMS, BED_UV, BED_CULL, BED_FUVS),

    # brewing stand
    BREWING_STAND_BLOCK: (MODE_CUSTOM, BREWING_STAND_ELEMS, BREWING_STAND_UV, BREWING_STAND_CULL, BREWING_STAND_FUVS),

    # saplings
    SAPLING_OAK: (MODE_CUSTOM, SAPLING_ELEMS, SAPLING_UV, SAPLING_CULL, SAPLING_FUVS),
    SAPLING_SPRUCE: (MODE_CUSTOM, SAPLING_ELEMS, SAPLING_UV, SAPLING_CULL, SAPLING_FUVS),
    SAPLING_BIRCH: (MODE_CUSTOM, SAPLING_ELEMS, SAPLING_UV, SAPLING_CULL, SAPLING_FUVS),
    SAPLING_JUNGLE: (MODE_CUSTOM, SAPLING_ELEMS, SAPLING_UV, SAPLING_CULL, SAPLING_FUVS),
    SAPLING_ACACIA: (MODE_CUSTOM, SAPLING_ELEMS, SAPLING_UV, SAPLING_CULL, SAPLING_FUVS),
    SAPLING_DARK_OAK: (MODE_CUSTOM, SAPLING_ELEMS, SAPLING_UV, SAPLING_CULL, SAPLING_FUVS),

    # rails
    RAIL: (MODE_CUSTOM, RAIL_ELEMS, RAIL_UV, RAIL_CULL, RAIL_FUVS),
    POWERED_RAIL: (MODE_CUSTOM, RAIL_ELEMS, RAIL_UV, RAIL_CULL, RAIL_FUVS),
    POWERED_RAIL_ON: (MODE_CUSTOM, RAIL_ELEMS, RAIL_UV, RAIL_CULL, RAIL_FUVS),
    DETECTOR_RAIL: (MODE_CUSTOM, RAIL_ELEMS, RAIL_UV, RAIL_CULL, RAIL_FUVS),
    ACTIVATOR_RAIL: (MODE_CUSTOM, RAIL_ELEMS, RAIL_UV, RAIL_CULL, RAIL_FUVS),

    # torches
    TORCH: (MODE_CUSTOM, TORCH_ELEMS, TORCH_UV, TORCH_CULL, TORCH_FUVS),
    REDSTONE_TORCH_OFF: (MODE_CUSTOM, TORCH_ELEMS, TORCH_UV, TORCH_CULL, TORCH_FUVS),
    REDSTONE_TORCH_ON: (MODE_CUSTOM, TORCH_ELEMS, TORCH_UV, TORCH_CULL, TORCH_FUVS),

    # stairs
    OAK_STAIRS: (MODE_CUSTOM, STAIR_ELEMS, STAIR_UV, STAIR_CULL, STAIR_FUVS),
    SPRUCE_STAIRS: (MODE_CUSTOM, STAIR_ELEMS, STAIR_UV, STAIR_CULL, STAIR_FUVS),
    BIRCH_STAIRS: (MODE_CUSTOM, STAIR_ELEMS, STAIR_UV, STAIR_CULL, STAIR_FUVS),
    JUNGLE_STAIRS: (MODE_CUSTOM, STAIR_ELEMS, STAIR_UV, STAIR_CULL, STAIR_FUVS),
    ACACIA_STAIRS: (MODE_CUSTOM, STAIR_ELEMS, STAIR_UV, STAIR_CULL, STAIR_FUVS),
    DARK_OAK_STAIRS: (MODE_CUSTOM, STAIR_ELEMS, STAIR_UV, STAIR_CULL, STAIR_FUVS),
    STONE_STAIRS: (MODE_CUSTOM, STAIR_ELEMS, STAIR_UV, STAIR_CULL, STAIR_FUVS),
    COBBLESTONE_STAIRS: (MODE_CUSTOM, STAIR_ELEMS, STAIR_UV, STAIR_CULL, STAIR_FUVS),
    BRICK_STAIRS: (MODE_CUSTOM, STAIR_ELEMS, STAIR_UV, STAIR_CULL, STAIR_FUVS),
    STONE_BRICK_STAIRS: (MODE_CUSTOM, STAIR_ELEMS, STAIR_UV, STAIR_CULL, STAIR_FUVS),
    NETHER_BRICK_STAIRS: (MODE_CUSTOM, STAIR_ELEMS, STAIR_UV, STAIR_CULL, STAIR_FUVS),
    SANDSTONE_STAIRS: (MODE_CUSTOM, STAIR_ELEMS, STAIR_UV, STAIR_CULL, STAIR_FUVS),
    QUARTZ_STAIRS: (MODE_CUSTOM, STAIR_ELEMS, STAIR_UV, STAIR_CULL, STAIR_FUVS),
    RED_SANDSTONE_STAIRS: (MODE_CUSTOM, STAIR_ELEMS, STAIR_UV, STAIR_CULL, STAIR_FUVS),

    # slabs
    STONE_SLAB: (MODE_CUSTOM, SLAB_ELEMS, SLAB_UV, SLAB_CULL, SLAB_FUVS),
    SANDSTONE_SLAB: (MODE_CUSTOM, SLAB_ELEMS, SLAB_UV, SLAB_CULL, SLAB_FUVS),
    COBBLESTONE_SLAB: (MODE_CUSTOM, SLAB_ELEMS, SLAB_UV, SLAB_CULL, SLAB_FUVS),
    BRICK_SLAB: (MODE_CUSTOM, SLAB_ELEMS, SLAB_UV, SLAB_CULL, SLAB_FUVS),
    STONE_BRICK_SLAB: (MODE_CUSTOM, SLAB_ELEMS, SLAB_UV, SLAB_CULL, SLAB_FUVS),
    NETHER_BRICK_SLAB: (MODE_CUSTOM, SLAB_ELEMS, SLAB_UV, SLAB_CULL, SLAB_FUVS),
    QUARTZ_SLAB: (MODE_CUSTOM, SLAB_ELEMS, SLAB_UV, SLAB_CULL, SLAB_FUVS),
    OAK_SLAB: (MODE_CUSTOM, SLAB_ELEMS, SLAB_UV, SLAB_CULL, SLAB_FUVS),
    SPRUCE_SLAB: (MODE_CUSTOM, SLAB_ELEMS, SLAB_UV, SLAB_CULL, SLAB_FUVS),
    BIRCH_SLAB: (MODE_CUSTOM, SLAB_ELEMS, SLAB_UV, SLAB_CULL, SLAB_FUVS),
    JUNGLE_SLAB: (MODE_CUSTOM, SLAB_ELEMS, SLAB_UV, SLAB_CULL, SLAB_FUVS),
    ACACIA_SLAB: (MODE_CUSTOM, SLAB_ELEMS, SLAB_UV, SLAB_CULL, SLAB_FUVS),
    DARK_OAK_SLAB: (MODE_CUSTOM, SLAB_ELEMS, SLAB_UV, SLAB_CULL, SLAB_FUVS),
    RED_SANDSTONE_SLAB: (MODE_CUSTOM, SLAB_ELEMS, SLAB_UV, SLAB_CULL, SLAB_FUVS),

    # lever & tripwire hook
    LEVER: (MODE_CUSTOM, LEVER_ELEMS, LEVER_UV, LEVER_CULL, LEVER_FUVS),
    TRIPWIRE_HOOK: (MODE_CUSTOM, TRIPWIRE_HOOK_ELEMS, TRIPWIRE_HOOK_UV, TRIPWIRE_HOOK_CULL, TRIPWIRE_HOOK_FUVS),

    # daylight detectors
    DAYLIGHT_DETECTOR: (MODE_CUSTOM, DAYLIGHT_DETECTOR_ELEMS, DAYLIGHT_DETECTOR_UV, DAYLIGHT_DETECTOR_CULL, DAYLIGHT_DETECTOR_FUVS),
    DAYLIGHT_DETECTOR_INVERTED: (MODE_CUSTOM, DAYLIGHT_DETECTOR_ELEMS, DAYLIGHT_DETECTOR_UV, DAYLIGHT_DETECTOR_CULL, DAYLIGHT_DETECTOR_FUVS),

    # iron bars
    IRON_BARS: (MODE_CUSTOM, IRON_BARS_ELEMS, IRON_BARS_UV, IRON_BARS_CULL, IRON_BARS_FUVS),

    # cobweb
    COBWEB: (MODE_CUSTOM, COBWEB_ELEMS, COBWEB_UV, COBWEB_CULL, COBWEB_FUVS),

    # glass panes
    GLASS_PANE: (MODE_CUSTOM, GLASS_PANE_ELEMS, GLASS_PANE_UV, GLASS_PANE_CULL, GLASS_PANE_FUVS),
    GLASS_PANE_WHITE: (MODE_CUSTOM, GLASS_PANE_ELEMS, GLASS_PANE_UV, GLASS_PANE_CULL, GLASS_PANE_FUVS),
    GLASS_PANE_ORANGE: (MODE_CUSTOM, GLASS_PANE_ELEMS, GLASS_PANE_UV, GLASS_PANE_CULL, GLASS_PANE_FUVS),
    GLASS_PANE_MAGENTA: (MODE_CUSTOM, GLASS_PANE_ELEMS, GLASS_PANE_UV, GLASS_PANE_CULL, GLASS_PANE_FUVS),
    GLASS_PANE_LIGHT_BLUE: (MODE_CUSTOM, GLASS_PANE_ELEMS, GLASS_PANE_UV, GLASS_PANE_CULL, GLASS_PANE_FUVS),
    GLASS_PANE_YELLOW: (MODE_CUSTOM, GLASS_PANE_ELEMS, GLASS_PANE_UV, GLASS_PANE_CULL, GLASS_PANE_FUVS),
    GLASS_PANE_LIME: (MODE_CUSTOM, GLASS_PANE_ELEMS, GLASS_PANE_UV, GLASS_PANE_CULL, GLASS_PANE_FUVS),
    GLASS_PANE_PINK: (MODE_CUSTOM, GLASS_PANE_ELEMS, GLASS_PANE_UV, GLASS_PANE_CULL, GLASS_PANE_FUVS),
    GLASS_PANE_GRAY: (MODE_CUSTOM, GLASS_PANE_ELEMS, GLASS_PANE_UV, GLASS_PANE_CULL, GLASS_PANE_FUVS),
    GLASS_PANE_SILVER: (MODE_CUSTOM, GLASS_PANE_ELEMS, GLASS_PANE_UV, GLASS_PANE_CULL, GLASS_PANE_FUVS),
    GLASS_PANE_CYAN: (MODE_CUSTOM, GLASS_PANE_ELEMS, GLASS_PANE_UV, GLASS_PANE_CULL, GLASS_PANE_FUVS),
    GLASS_PANE_PURPLE: (MODE_CUSTOM, GLASS_PANE_ELEMS, GLASS_PANE_UV, GLASS_PANE_CULL, GLASS_PANE_FUVS),
    GLASS_PANE_BLUE: (MODE_CUSTOM, GLASS_PANE_ELEMS, GLASS_PANE_UV, GLASS_PANE_CULL, GLASS_PANE_FUVS),
    GLASS_PANE_BROWN: (MODE_CUSTOM, GLASS_PANE_ELEMS, GLASS_PANE_UV, GLASS_PANE_CULL, GLASS_PANE_FUVS),
    GLASS_PANE_GREEN: (MODE_CUSTOM, GLASS_PANE_ELEMS, GLASS_PANE_UV, GLASS_PANE_CULL, GLASS_PANE_FUVS),
    GLASS_PANE_RED: (MODE_CUSTOM, GLASS_PANE_ELEMS, GLASS_PANE_UV, GLASS_PANE_CULL, GLASS_PANE_FUVS),
    GLASS_PANE_BLACK: (MODE_CUSTOM, GLASS_PANE_ELEMS, GLASS_PANE_UV, GLASS_PANE_CULL, GLASS_PANE_FUVS),

    # vines & lily pad
    VINE: (MODE_CUSTOM, VINE_ELEMS, VINE_UV, VINE_CULL, VINE_FUVS),
    LILY_PAD: (MODE_CUSTOM, LILY_PAD_ELEMS, LILY_PAD_UV, LILY_PAD_CULL, LILY_PAD_FUVS),

    # enchanting table
    ENCHANTING_TABLE: (MODE_CUSTOM, ENCHANTING_TABLE_ELEMS, ENCHANTING_TABLE_UV, ENCHANTING_TABLE_CULL, ENCHANTING_TABLE_FUVS),

    # end portal frame
    END_PORTAL_FRAME: (MODE_CUSTOM, END_PORTAL_FRAME_ELEMS, END_PORTAL_FRAME_UV, END_PORTAL_FRAME_CULL, END_PORTAL_FRAME_FUVS),

    # anvils
    ANVIL: (MODE_CUSTOM, ANVIL_ELEMS, ANVIL_UV, ANVIL_CULL, ANVIL_FUVS),
    ANVIL_SLIGHTLY_DAMAGED: (MODE_CUSTOM, ANVIL_ELEMS, ANVIL_UV, ANVIL_CULL, ANVIL_FUVS),
    ANVIL_VERY_DAMAGED: (MODE_CUSTOM, ANVIL_ELEMS, ANVIL_UV, ANVIL_CULL, ANVIL_FUVS),

    # flowers & cross plants
    DANDELION: (MODE_CUSTOM, SAPLING_ELEMS, SAPLING_UV, SAPLING_CULL, SAPLING_FUVS),
    POPPY: (MODE_CUSTOM, SAPLING_ELEMS, SAPLING_UV, SAPLING_CULL, SAPLING_FUVS),
    BLUE_ORCHID: (MODE_CUSTOM, SAPLING_ELEMS, SAPLING_UV, SAPLING_CULL, SAPLING_FUVS),
    ALLIUM: (MODE_CUSTOM, SAPLING_ELEMS, SAPLING_UV, SAPLING_CULL, SAPLING_FUVS),
    AZURE_BLUET: (MODE_CUSTOM, SAPLING_ELEMS, SAPLING_UV, SAPLING_CULL, SAPLING_FUVS),
    RED_TULIP: (MODE_CUSTOM, SAPLING_ELEMS, SAPLING_UV, SAPLING_CULL, SAPLING_FUVS),
    ORANGE_TULIP: (MODE_CUSTOM, SAPLING_ELEMS, SAPLING_UV, SAPLING_CULL, SAPLING_FUVS),
    WHITE_TULIP: (MODE_CUSTOM, SAPLING_ELEMS, SAPLING_UV, SAPLING_CULL, SAPLING_FUVS),
    PINK_TULIP: (MODE_CUSTOM, SAPLING_ELEMS, SAPLING_UV, SAPLING_CULL, SAPLING_FUVS),
    OXEYE_DAISY: (MODE_CUSTOM, SAPLING_ELEMS, SAPLING_UV, SAPLING_CULL, SAPLING_FUVS),
    BROWN_MUSHROOM: (MODE_CUSTOM, SAPLING_ELEMS, SAPLING_UV, SAPLING_CULL, SAPLING_FUVS),
    RED_MUSHROOM: (MODE_CUSTOM, SAPLING_ELEMS, SAPLING_UV, SAPLING_CULL, SAPLING_FUVS),
    DEAD_BUSH: (MODE_CUSTOM, SAPLING_ELEMS, SAPLING_UV, SAPLING_CULL, SAPLING_FUVS),
    FERN: (MODE_CUSTOM, SAPLING_ELEMS, SAPLING_UV, SAPLING_CULL, SAPLING_FUVS),
    SUNFLOWER: (MODE_CUSTOM, SAPLING_ELEMS, SAPLING_UV, SAPLING_CULL, SAPLING_FUVS),
    LILAC: (MODE_CUSTOM, SAPLING_ELEMS, SAPLING_UV, SAPLING_CULL, SAPLING_FUVS),
    DOUBLE_TALLGRASS: (MODE_CUSTOM, SAPLING_ELEMS, SAPLING_UV, SAPLING_CULL, SAPLING_FUVS),
    LARGE_FERN: (MODE_CUSTOM, SAPLING_ELEMS, SAPLING_UV, SAPLING_CULL, SAPLING_FUVS),
    ROSE_BUSH: (MODE_CUSTOM, SAPLING_ELEMS, SAPLING_UV, SAPLING_CULL, SAPLING_FUVS),
    PEONY: (MODE_CUSTOM, SAPLING_ELEMS, SAPLING_UV, SAPLING_CULL, SAPLING_FUVS),
}







##  == BLOCK MODELS ==


BLOCK_DATA = {}  # bid -> (elements, face_uvs_list, face_tex_list)

# anvil
for bid, top_tex in [
    (ANVIL, "anvil_top_damaged_0"),
    (ANVIL_SLIGHTLY_DAMAGED, "anvil_top_damaged_1"),
    (ANVIL_VERY_DAMAGED, "anvil_top_damaged_2")
]:
    
    m = modeljson("anvil", {"body": "blocks/anvil_base", "top": f"blocks/{top_tex}"})
    if m:
        elems, fuvs, ftex = m
        CUSTOM_BLOCKS[bid] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
        BLOCK_DATA[bid] = ftex


# lver
m = modeljson("lever", {"base": "blocks/cobblestone", "lever": "blocks/lever"})
if m:
    elems, fuvs, ftex = m
    CUSTOM_BLOCKS[LEVER] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
    BLOCK_DATA[LEVER] = ftex

m = modeljson("tripwire_hook", {"hook": "blocks/trip_wire_source", "wood": "blocks/planks_oak"})
if m:
    elems, fuvs, ftex = m
    CUSTOM_BLOCKS[TRIPWIRE_HOOK] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
    BLOCK_DATA[TRIPWIRE_HOOK] = ftex





# pane post
_ppelems = [elemfaces([7, 0, 7], [9, 16, 9])]
_pp_fuv = np.zeros((6, 8), dtype=np.float32)
_pp_fuv[0] = faceuv8(7/16, 7/16, 9/16, 9/16)   # top
_pp_fuv[1] = faceuv8(7/16, 7/16, 9/16, 9/16)   # bot
_pp_fuv[2] = faceuv8(7/16, 0/16, 9/16, 16/16)  # n
_pp_fuv[3] = faceuv8(7/16, 0/16, 9/16, 16/16)  # s
_pp_fuv[4] = faceuv8(7/16, 0/16, 9/16, 16/16)  # e
_pp_fuv[5] = faceuv8(7/16, 0/16, 9/16, 16/16)  # w
_ppfuv  = [_pp_fuv]
_ppedge = atlasuv("blocks/glass_pane_top")
_ppftex = [np.full((6, 2), -1.0, dtype=np.float32)]
if _ppedge:
    for _fi in range(6):
        _ppftex[0][_fi] = _ppedge

_pvars = [
    (GLASS_PANE,            "glass",            "glass_pane_top"),
    (GLASS_PANE_WHITE,      "glass_white",      "glass_pane_top_white"),
    (GLASS_PANE_ORANGE,     "glass_orange",     "glass_pane_top_orange"),
    (GLASS_PANE_MAGENTA,    "glass_magenta",    "glass_pane_top_magenta"),
    (GLASS_PANE_LIGHT_BLUE, "glass_light_blue", "glass_pane_top_light_blue"),
    (GLASS_PANE_YELLOW,     "glass_yellow",     "glass_pane_top_yellow"),
    (GLASS_PANE_LIME,       "glass_lime",       "glass_pane_top_lime"),
    (GLASS_PANE_PINK,       "glass_pink",       "glass_pane_top_pink"),
    (GLASS_PANE_GRAY,       "glass_gray",       "glass_pane_top_gray"),
    (GLASS_PANE_SILVER,     "glass_silver",     "glass_pane_top_silver"),
    (GLASS_PANE_CYAN,       "glass_cyan",       "glass_pane_top_cyan"),
    (GLASS_PANE_PURPLE,     "glass_purple",     "glass_pane_top_purple"),
    (GLASS_PANE_BLUE,       "glass_blue",       "glass_pane_top_blue"),
    (GLASS_PANE_BROWN,      "glass_brown",      "glass_pane_top_brown"),
    (GLASS_PANE_GREEN,      "glass_green",      "glass_pane_top_green"),
    (GLASS_PANE_RED,        "glass_red",        "glass_pane_top_red"),
    (GLASS_PANE_BLACK,      "glass_black",      "glass_pane_top_black"),
]
for _gpid, _ptx, _etx in _pvars:
    CUSTOM_BLOCKS[_gpid] = (MODE_CUSTOM, _ppelems, UV_MODE_MODEL, False, _ppfuv)
    _peatl  = atlasuv(f"blocks/{_etx}")
    _pvftex = [np.full((6, 2), -1.0, dtype=np.float32)]
    if _peatl:
        for _pfi in range(6):
            _pvftex[0][_pfi] = np.array(_peatl, dtype=np.float32)
    BLOCK_DATA[_gpid] = _pvftex




# torch
for bid, tex in [(TORCH, "blocks/torch_on"),
                 (REDSTONE_TORCH_ON, "blocks/redstone_torch_on"),
                 (REDSTONE_TORCH_OFF, "blocks/redstone_torch_off")]:
    m = modeljson("torch", etx={"torch": tex})
    if m:
        elems, fuvs, ftex = m
        CUSTOM_BLOCKS[bid] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
        BLOCK_DATA[bid] = ftex



# enchanting
m = modeljson("enchanting_table_base", {
    "bottom": "blocks/enchanting_table_bottom",
    "top": "blocks/enchanting_table_top",
    "side": "blocks/enchanting_table_side",
})
if m:
    elems, fuvs, ftex = m
    CUSTOM_BLOCKS[ENCHANTING_TABLE] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
    BLOCK_DATA[ENCHANTING_TABLE] = ftex



# portal
m = modeljson("end_portal_frame_empty", {
    "bottom": "blocks/end_stone",
    "top": "blocks/endframe_top",
    "side": "blocks/endframe_side",
})
if m:
    elems, fuvs, ftex = m
    CUSTOM_BLOCKS[END_PORTAL_FRAME] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
    BLOCK_DATA[END_PORTAL_FRAME] = ftex



# bars
_bpelems = [elemfaces([7, 0, 7], [9, 16, 9])]
_bpfuv   = [_pp_fuv.copy()]  # same proportions as pane post
_batl    = atlasuv("blocks/iron_bars")
_bpftex  = [np.full((6, 2), -1.0, dtype=np.float32)]
if _batl:
    for _fi in range(6):
        _bpftex[0][_fi] = _batl
CUSTOM_BLOCKS[IRON_BARS] = (MODE_CUSTOM, _bpelems, UV_MODE_MODEL, False, _bpfuv)
BLOCK_DATA[IRON_BARS] = _bpftex



# beds
m = modeljson("bed_foot", {
    "top": "blocks/bed_feet_top",
    "bottom": "blocks/planks_oak",
    "end": "blocks/bed_feet_end",
    "side": "blocks/bed_feet_side",
})
if m:
    elems, fuvs, ftex = m
    CUSTOM_BLOCKS[BED_FOOT] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
    BLOCK_DATA[BED_FOOT] = ftex

m = modeljson("bed_head", {
    "top": "blocks/bed_head_top",
    "bottom": "blocks/planks_oak",
    "end": "blocks/bed_head_end",
    "side": "blocks/bed_head_side",
})
if m:
    elems, fuvs, ftex = m
    CUSTOM_BLOCKS[BED_HEAD] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
    BLOCK_DATA[BED_HEAD] = ftex



# vine
m = modeljson("vine_1", {"vine": "blocks/vine"})
if m:
    elems, fuvs, ftex = m
    CUSTOM_BLOCKS[VINE] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
    BLOCK_DATA[VINE] = ftex



# brewing stand
m = modeljson("brewing_stand_empty", {
    "stand": "blocks/brewing_stand",
    "base": "blocks/brewing_stand_base",
})
if m:
    elems, fuvs, ftex = m
    CUSTOM_BLOCKS[BREWING_STAND_BLOCK] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
    BLOCK_DATA[BREWING_STAND_BLOCK] = ftex



# item frame
m = modeljson("item_frame_map", {"wood": "blocks/planks_birch", "back": "blocks/item_frame"})
if m:
    elems, fuvs, ftex = m
    CUSTOM_BLOCKS[ITEM_FRAME_BLOCK] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
    BLOCK_DATA[ITEM_FRAME_BLOCK] = ftex



# repeater
m = modeljson("repeater_1tick", {
    "slab": "blocks/stone_slab_top",
    "top": "blocks/repeater_off",
    "unlit": "blocks/redstone_torch_off",
})
if m:
    elems, fuvs, ftex = m
    CUSTOM_BLOCKS[REPEATER] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
    BLOCK_DATA[REPEATER] = ftex



# comparator
m = modeljson("comparator_unlit", {
    "slab": "blocks/stone_slab_top",
    "top": "blocks/comparator_off",
    "unlit": "blocks/redstone_torch_off",
    "lit": "blocks/redstone_torch_on",
})
if m:
    elems, fuvs, ftex = m
    CUSTOM_BLOCKS[COMPARATOR] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
    BLOCK_DATA[COMPARATOR] = ftex



# hopper
m = modeljson("hopper_down", {
    "top": "blocks/hopper_top",
    "side": "blocks/hopper_outside",
    "inside": "blocks/hopper_inside",
})
if m:
    elems, fuvs, ftex = m
    CUSTOM_BLOCKS[HOPPER] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
    BLOCK_DATA[HOPPER] = ftex



# cauldron
m = modeljson("cauldron_empty", {
    "top": "blocks/cauldron_top",
    "bottom": "blocks/cauldron_bottom",
    "side": "blocks/cauldron_side",
    "inside": "blocks/cauldron_inner",
})
if m:
    elems, fuvs, ftex = m
    CUSTOM_BLOCKS[CAULDRON] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
    BLOCK_DATA[CAULDRON] = ftex



# cake
m = modeljson("cake_uneaten", {
    "top": "blocks/cake_top",
    "bottom": "blocks/cake_bottom",
    "side": "blocks/cake_side",
})
if m:
    elems, fuvs, ftex = m
    CUSTOM_BLOCKS[CAKE] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
    BLOCK_DATA[CAKE] = ftex



# cactus
m = modeljson("cactus", {
    "top": "blocks/cactus_top",
    "bottom": "blocks/cactus_bottom",
    "side": "blocks/cactus_side",
})
if m:
    elems, fuvs, ftex = m
    CUSTOM_BLOCKS[CACTUS] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
    BLOCK_DATA[CACTUS] = ftex



# detector
m = modeljson("daylight_detector", {
    "top": "blocks/daylight_detector_top",
    "side": "blocks/daylight_detector_side",
})
if m:
    elems, fuvs, ftex = m
    CUSTOM_BLOCKS[DAYLIGHT_DETECTOR] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
    BLOCK_DATA[DAYLIGHT_DETECTOR] = ftex

m = modeljson("daylight_detector_inverted", {
    "top": "blocks/daylight_detector_inverted_top",
    "side": "blocks/daylight_detector_side",
})
if m:
    elems, fuvs, ftex = m
    CUSTOM_BLOCKS[DAYLIGHT_DETECTOR_INVERTED] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
    BLOCK_DATA[DAYLIGHT_DETECTOR_INVERTED] = ftex




# tallgrass
m = modeljson("tallgrass", {"cross": "blocks/tallgrass"})
if m:
    elems, fuvs, ftex = m
    CUSTOM_BLOCKS[TALLGRASS] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
    BLOCK_DATA[TALLGRASS] = ftex


# cane
m = modeljson("reeds", {"cross": "blocks/reeds"})
if m:
    elems, fuvs, ftex = m
    CUSTOM_BLOCKS[SUGAR_CANE] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
    BLOCK_DATA[SUGAR_CANE] = ftex



# cobweb
m = modeljson("cross", {"cross": "blocks/web"})
if m:
    elems, fuvs, ftex = m
    CUSTOM_BLOCKS[COBWEB] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
    BLOCK_DATA[COBWEB] = ftex

m = modeljson("waterlily", {"texture": "blocks/waterlily"})
if m:
    elems, fuvs, ftex = m
    CUSTOM_BLOCKS[LILY_PAD] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
    BLOCK_DATA[LILY_PAD] = ftex





"""
# cross plants
_cmc = modeljson("cross", {"cross": "blocks/tallgrass"})
if _cmc:
    _celems, _cfuvs, _ = _cmc
    for bid in [
        SAPLING_OAK, SAPLING_SPRUCE, SAPLING_BIRCH,
        SAPLING_JUNGLE, SAPLING_ACACIA, SAPLING_DARK_OAK,
        DANDELION, POPPY, BLUE_ORCHID, ALLIUM, AZURE_BLUET,
        RED_TULIP, ORANGE_TULIP, WHITE_TULIP, PINK_TULIP, OXEYE_DAISY,
        BROWN_MUSHROOM, RED_MUSHROOM, DEAD_BUSH, FERN,
        SUNFLOWER, LILAC, DOUBLE_TALLGRASS, LARGE_FERN, ROSE_BUSH, PEONY
    ]:

        old = CUSTOM_BLOCKS.get(bid)
        if old:
            CUSTOM_BLOCKS[bid] = (old[0], _celems, UV_MODE_IDX, old[3], None)
"""

for bid, modelname in [
    (SAPLING_OAK,      "oak_sapling"),
    (SAPLING_SPRUCE,   "spruce_sapling"),
    (SAPLING_BIRCH,    "birch_sapling"),
    (SAPLING_JUNGLE,   "jungle_sapling"),
    (SAPLING_ACACIA,   "acacia_sapling"),
    (SAPLING_DARK_OAK, "dark_oak_sapling"),
    (DANDELION,        "dandelion"),
    (POPPY,            "poppy"),
    (BLUE_ORCHID,      "blue_orchid"),
    (ALLIUM,           "allium"),
    (AZURE_BLUET,      "azure_bluet"),
    (RED_TULIP,        "red_tulip"),
    (ORANGE_TULIP,     "orange_tulip"),
    (WHITE_TULIP,      "white_tulip"),
    (PINK_TULIP,       "pink_tulip"),
    (OXEYE_DAISY,      "oxeye_daisy"),
    (BROWN_MUSHROOM,   "brown_mushroom"),
    (RED_MUSHROOM,     "red_mushroom"),
    (DEAD_BUSH,        "dead_bush"),
    (FERN,             "fern"),
    (SUNFLOWER,        "double_sunflower_bottom"),
    (LILAC,            "double_syringa_bottom"),
    (DOUBLE_TALLGRASS, "double_grass_bottom"),
    (LARGE_FERN,       "double_fern_bottom"),
    (ROSE_BUSH,        "double_rose_bottom"),
    (PEONY,            "double_paeonia_bottom"),
]:
    m = modeljson(modelname)
    if m:
        elems, fuvs, ftex = m
        CUSTOM_BLOCKS[bid] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
        BLOCK_DATA[bid] = ftex





# rails
for bid, tex in [
    (RAIL, "blocks/rail_normal"),
    (POWERED_RAIL, "blocks/rail_golden"),
    (POWERED_RAIL_ON, "blocks/rail_golden_powered"),
    (DETECTOR_RAIL, "blocks/rail_detector"),
    (ACTIVATOR_RAIL, "blocks/rail_activator")
]:
    m = modeljson("normal_rail_flat", {"rail": tex})
    if m:
        elems, fuvs, ftex = m
        CUSTOM_BLOCKS[bid] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
        BLOCK_DATA[bid] = ftex





# slabs
_svars = [
    (STONE_SLAB,        "half_slab_stone"),
    (SANDSTONE_SLAB,    "half_slab_sandstone"),
    (COBBLESTONE_SLAB,  "half_slab_cobblestone"),
    (BRICK_SLAB,        "half_slab_brick"),
    (STONE_BRICK_SLAB,  "half_slab_stone_brick"),
    (NETHER_BRICK_SLAB, "half_slab_nether_brick"),
    (QUARTZ_SLAB,   "half_slab_quartz"),
    (OAK_SLAB,      "half_slab_oak"),
    (SPRUCE_SLAB,   "half_slab_spruce"),
    (BIRCH_SLAB,    "half_slab_birch"),
    (JUNGLE_SLAB,   "half_slab_jungle"),
    (ACACIA_SLAB,   "half_slab_acacia"),
    (DARK_OAK_SLAB, "half_slab_dark_oak"),
    (RED_SANDSTONE_SLAB, "half_slab_red_sandstone"),
]
for bid, modelname in _svars:
    m = modeljson(modelname)
    if m:
        elems, fuvs, ftex = m
        CUSTOM_BLOCKS[bid] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
        BLOCK_DATA[bid] = ftex






# stairs
_stvars = [
    (OAK_STAIRS,      "oak_stairs"),
    (SPRUCE_STAIRS,   "spruce_stairs"),
    (BIRCH_STAIRS,    "birch_stairs"),
    (JUNGLE_STAIRS,   "jungle_stairs"),
    (ACACIA_STAIRS,   "acacia_stairs"),
    (DARK_OAK_STAIRS, "dark_oak_stairs"),
    (COBBLESTONE_STAIRS,  "stone_stairs"),
    (BRICK_STAIRS,        "brick_stairs"),
    (STONE_BRICK_STAIRS,  "stone_brick_stairs"),
    (NETHER_BRICK_STAIRS, "nether_brick_stairs"),
    (SANDSTONE_STAIRS,    "sandstone_stairs"),
    (QUARTZ_STAIRS,       "quartz_stairs"),
    (RED_SANDSTONE_STAIRS, "red_sandstone_stairs"),
]
for bid, modelname in _stvars:
    m = modeljson(modelname)
    if m:
        elems, fuvs, ftex = m
        CUSTOM_BLOCKS[bid] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
        BLOCK_DATA[bid] = ftex



m = modeljson("stone_stairs", {
        "bottom": "blocks/stone", 
        "top": "blocks/stone", 
        "side": "blocks/stone"
    }
)
if m:
    elems, fuvs, ftex = m
    CUSTOM_BLOCKS[STONE_STAIRS] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
    BLOCK_DATA[STONE_STAIRS] = ftex

# doors
_dvars = [
    (OAK_DOOR_BOTTOM,      "wooden_door_bottom"),   (OAK_DOOR_TOP,      "wooden_door_top"),
    (SPRUCE_DOOR_BOTTOM,   "spruce_door_bottom"),   (SPRUCE_DOOR_TOP,   "spruce_door_top"),
    (BIRCH_DOOR_BOTTOM,    "birch_door_bottom"),    (BIRCH_DOOR_TOP,    "birch_door_top"),
    (JUNGLE_DOOR_BOTTOM,   "jungle_door_bottom"),   (JUNGLE_DOOR_TOP,   "jungle_door_top"),
    (ACACIA_DOOR_BOTTOM,   "acacia_door_bottom"),   (ACACIA_DOOR_TOP,   "acacia_door_top"),
    (DARK_OAK_DOOR_BOTTOM, "dark_oak_door_bottom"), (DARK_OAK_DOOR_TOP, "dark_oak_door_top"),
    (IRON_DOOR_BOTTOM,     "iron_door_bottom"),     (IRON_DOOR_TOP,     "iron_door_top"),
]
for bid, modelname in _dvars:
    m = modeljson(modelname)
    if m:
        elems, fuvs, ftex = m
        CUSTOM_BLOCKS[bid] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
        BLOCK_DATA[bid] = ftex

# buttons
for bid, modelname in [
        (STONE_BUTTON, "stone_button"), 
        (WOODEN_BUTTON, "wooden_button")
]:
    m = modeljson(modelname)
    if m:
        elems, fuvs, ftex = m
        CUSTOM_BLOCKS[bid] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
        BLOCK_DATA[bid] = ftex

# plats
for bid, tex in [
    (STONE_PRESSURE_PLATE,  "blocks/stone"),
    (WOODEN_PRESSURE_PLATE, "blocks/planks_oak"),
    (LIGHT_WEIGHTED_PRESSURE_PLATE, "blocks/gold_block"),
    (HEAVY_WEIGHTED_PRESSURE_PLATE, "blocks/iron_block")
]:
    m = modeljson("pressure_plate_up", {"texture": tex})
    if m:
        elems, fuvs, ftex = m
        CUSTOM_BLOCKS[bid] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
        BLOCK_DATA[bid] = ftex



# trapdoors
m = modeljson("trapdoor_bottom", {"texture": "blocks/trapdoor"})
if m:
    elems, fuvs, ftex = m
    CUSTOM_BLOCKS[OAK_TRAPDOOR] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
    BLOCK_DATA[OAK_TRAPDOOR] = ftex

m = modeljson("iron_trapdoor_bottom")
if m:
    elems, fuvs, ftex = m
    CUSTOM_BLOCKS[IRON_TRAPDOOR] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
    BLOCK_DATA[IRON_TRAPDOOR] = ftex




m = modeljson("ladder")
if m:
    elems, fuvs, ftex = m
    CUSTOM_BLOCKS[LADDER] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
    BLOCK_DATA[LADDER] = ftex


m = modeljson("dragon_egg")
if m:
    elems, fuvs, ftex = m
    CUSTOM_BLOCKS[DRAGON_EGG] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
    BLOCK_DATA[DRAGON_EGG] = ftex


m = modeljson("snow_height2")
if m:
    elems, fuvs, ftex = m
    CUSTOM_BLOCKS[SNOW] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
    BLOCK_DATA[SNOW] = ftex


m = modeljson("fire_floor", {"fire": "blocks/fire_layer_0"})
if m:
    elems, fuvs, ftex = m
    CUSTOM_BLOCKS[FIRE] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
    BLOCK_DATA[FIRE] = ftex


# TODO  - chesrts
_chelems = [elemfaces([1, 0, 1], [15, 14, 15])]
for bid in [CHEST, TRAPPED_CHEST, ENDER_CHEST]:
    CUSTOM_BLOCKS[bid] = (MODE_CUSTOM, _chelems, UV_MODE_IDX, False, None)


_ccols = [
    (CARPET_WHITE,   "carpet_white"),   (CARPET_ORANGE, "carpet_orange"),
    (CARPET_MAGENTA, "carpet_magenta"), (CARPET_LIGHT_BLUE, "carpet_light_blue"),
    (CARPET_YELLOW,  "carpet_yellow"),  (CARPET_LIME,  "carpet_lime"),
    (CARPET_PINK,    "carpet_pink"),    (CARPET_GRAY,  "carpet_gray"),
    (CARPET_SILVER,  "carpet_silver"),  (CARPET_CYAN,  "carpet_cyan"),
    (CARPET_PURPLE,  "carpet_purple"),  (CARPET_BLUE,  "carpet_blue"),
    (CARPET_BROWN,   "carpet_brown"),   (CARPET_GREEN, "carpet_green"),
    (CARPET_RED,     "carpet_red"),     (CARPET_BLACK, "carpet_black"),
]
for bid, modelname in _ccols:
    m = modeljson(modelname)
    if m:
        elems, fuvs, ftex = m
        CUSTOM_BLOCKS[bid] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
        BLOCK_DATA[bid] = ftex

# gates
_fgvars = [
    (OAK_FENCE_GATE,      "oak_fence_gate_closed"),
    (SPRUCE_FENCE_GATE,   "spruce_fence_gate_closed"),
    (BIRCH_FENCE_GATE,    "birch_fence_gate_closed"),
    (JUNGLE_FENCE_GATE,   "jungle_fence_gate_closed"),
    (ACACIA_FENCE_GATE,   "acacia_fence_gate_closed"),
    (DARK_OAK_FENCE_GATE, "dark_oak_fence_gate_closed"),
]
for bid, modelname in _fgvars:
    m = modeljson(modelname)
    if m:
        elems, fuvs, ftex = m
        CUSTOM_BLOCKS[bid] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
        BLOCK_DATA[bid] = ftex

# fences
_fpvars = [
    (OAK_FENCE,      "oak_fence_post"),
    (SPRUCE_FENCE,   "spruce_fence_post"),
    (BIRCH_FENCE,    "birch_fence_post"),
    (JUNGLE_FENCE,   "jungle_fence_post"),
    (ACACIA_FENCE,   "acacia_fence_post"),
    (DARK_OAK_FENCE, "dark_oak_fence_post"),
    (NETHER_BRICK_FENCE, "nether_brick_fence_post"),
]
for bid, modelname in _fpvars:
    m = modeljson(modelname)
    if m:
        elems, fuvs, ftex = m
        CUSTOM_BLOCKS[bid] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
        BLOCK_DATA[bid] = ftex

# walls
for bid, modelname in [
    (COBBLESTONE_WALL, "cobblestone_wall_post"),
    (MOSSY_COBBLESTONE_WALL, "mossy_wall_post")
]:
    m = modeljson(modelname)
    if m:
        elems, fuvs, ftex = m
        CUSTOM_BLOCKS[bid] = (MODE_CUSTOM, elems, UV_MODE_MODEL, False, fuvs)
        BLOCK_DATA[bid] = ftex


BLOCK_MODE_RENDER = np.zeros(MAX_CUSTOM, dtype=np.int32)
BLOCK_MODE_UV = np.zeros(MAX_CUSTOM, dtype=np.int32)
CULL_TOPBOT   = np.zeros(MAX_CUSTOM, dtype=np.bool_)
NUM_ELEMENTS  = np.zeros(MAX_CUSTOM, dtype=np.int32)
BLOCK_ELEMS   = np.zeros((MAX_CUSTOM, MAX_ELEMS, 6, 6, 3), dtype=np.float32)

# [BL_u, BL_v, BR_u, BR_v, TR_u, TR_v, TL_u, TL_v]
BLOCK_UVS = np.zeros((MAX_CUSTOM, MAX_ELEMS, 6, 8), dtype=np.float32)

_default_uv8 = faceuv8(0.0, 0.0, 1.0, 1.0)
for _i in range(8):
    BLOCK_UVS[:, :, :, _i] = _default_uv8[_i]



BLOCK_TEX = np.full((MAX_CUSTOM, MAX_ELEMS, 6, 2), -1.0, dtype=np.float32)
BLOCK_TINT_COLOR = np.ones((MAX_CUSTOM, 3), dtype=np.float32)

for i in range(MAX_CUSTOM):
    NUM_ELEMENTS[i] = 1
    BLOCK_ELEMS[i, 0] = elemfaces([0, 0, 0], [16, 16, 16])

for bid, (mode, elems, uv_mode, cull, fuvs) in CUSTOM_BLOCKS.items():
    if bid < MAX_CUSTOM:
        BLOCK_MODE_RENDER[bid] = mode
        BLOCK_MODE_UV[bid] = uv_mode
        CULL_TOPBOT[bid] = cull
        n, flat = flattenelems(elems)
        NUM_ELEMENTS[bid] = n
        BLOCK_ELEMS[bid] = flat
        if fuvs is not None:
            for ei, fuv in enumerate(fuvs[:MAX_ELEMS]):
                if fuv is not None:
                    BLOCK_UVS[bid, ei] = fuv
        if bid in BLOCK_DATA:
            ftl = BLOCK_DATA[bid]
            for ei, ftex in enumerate(ftl[:MAX_ELEMS]):
                if ftex is not None:
                    BLOCK_TEX[bid, ei] = ftex



BLOCK_TINT_COLOR[REDSTONE_WIRE] = [1.0, 0.0, 0.0]


STATE_ELEM_OFF = np.zeros((MAX_CUSTOM, 32), dtype=np.int32)
STATE_ELEM_NUM = np.zeros((MAX_CUSTOM, 32), dtype=np.int32)



# rail: state 0 = N/S, state 1 = E/W
_r90uv = np.array(faceuv8(0.0, 0.0, 1.0, 1.0, 90), dtype=np.float32)
for _rbid in [RAIL, POWERED_RAIL, POWERED_RAIL_ON, DETECTOR_RAIL, ACTIVATOR_RAIL]:
    BLOCK_ELEMS[_rbid, 1] = BLOCK_ELEMS[_rbid, 0]
    BLOCK_TEX[_rbid, 1] = BLOCK_TEX[_rbid, 0]
    BLOCK_UVS[_rbid, 1] = BLOCK_UVS[_rbid, 0]
    BLOCK_UVS[_rbid, 1, 0] = _r90uv
    BLOCK_UVS[_rbid, 1, 1] = _r90uv
    STATE_ELEM_OFF[_rbid, 1] = 1






# -- redston wire --

# mask bit layout: N=8, S=4, E=2, W=1  (0=none...15=all four)
#
# atlas 4,18 = full cross:
#   - E/W arm: rows y=6-9 (horiz strip, full width)
#   - N/S arm: col  x≈8, rows y=0-5 and y=10-15 (vertical)
#   - dot: x=[5,11], y=[5,11]
#
# uv formula derived from json model (redstone_none, redstone_ne, redstone_nsew):
#   u_min = 0 if W else 5,  u_max = 16 if E else 11
#   v_min = 0 if N else 5,  v_max = 16 if S else 11
# special mask=0: geometry from=[5,0.25,5] to=[11,0.25,11], same UV -> dot
# fuck you

_rd_cross = atlasuv("blocks/redstone_dust_cross")
NUM_ELEMENTS[REDSTONE_WIRE] = 1
for _mask in range(16):
    _rd_n = bool(_mask & 8)
    _rd_s = bool(_mask & 4)
    _rd_e = bool(_mask & 2)
    _rd_w = bool(_mask & 1)
    _xmin = 0 if _rd_w else 5
    _xmax = 16 if _rd_e else 11
    _zmin = 0 if _rd_n else 5
    _zmax = 16 if _rd_s else 11
    _rd_elem = elemfaces([_xmin, 0.25, _zmin], [_xmax, 0.25, _zmax])
    
    # zero all faces except 0 (top)
    for _fi in range(1, 6):
        _rd_elem[_fi, :, :] = 0.0
    BLOCK_ELEMS[REDSTONE_WIRE, _mask] = _rd_elem
    _rd_uv = np.array(faceuv8(_xmin/16.0, _zmin/16.0, _xmax/16.0, _zmax/16.0), dtype=np.float32)
    BLOCK_UVS[REDSTONE_WIRE, _mask, 0] = _rd_uv
    if _rd_cross:
        BLOCK_TEX[REDSTONE_WIRE, _mask, 0] = np.array(_rd_cross, dtype=np.float32)



# straight line variants; mask=3 EW, mask=12 NS
_rd_line = atlasuv("blocks/redstone_dust_line0")
if _rd_line:
    _rdlarr = np.array(_rd_line, dtype=np.float32)
    _rdfe = elemfaces([0, 0.25, 0], [16, 0.25, 16])
    
    for _fi in range(1, 6):
        _rdfe[_fi, :, :] = 0.0
    
    
    # EW mask=3: line0 as-is - horizontal strp
    BLOCK_ELEMS[REDSTONE_WIRE, 3] = _rdfe
    BLOCK_TEX[REDSTONE_WIRE, 3, 0] = _rdlarr
    BLOCK_UVS[REDSTONE_WIRE, 3, 0] = np.array(faceuv8(0.0, 0.0, 1.0, 1.0), dtype=np.float32)
    
    BLOCK_ELEMS[REDSTONE_WIRE, 12] = _rdfe.copy()
    BLOCK_TEX[REDSTONE_WIRE, 12, 0] = _rdlarr
    BLOCK_UVS[REDSTONE_WIRE, 12, 0] = np.array(faceuv8(0.0, 0.0, 1.0, 1.0, 90), dtype=np.float32)
    
    
    
    # e mask=2: right block half, full z, right lineuv half
    _rde = elemfaces([8, 0.25, 0], [16, 0.25, 16])
    for _fi in range(1, 6): _rde[_fi, :, :] = 0.0
    BLOCK_ELEMS[REDSTONE_WIRE, 2] = _rde
    BLOCK_TEX[REDSTONE_WIRE, 2, 0] = _rdlarr
    BLOCK_UVS[REDSTONE_WIRE, 2, 0] = np.array(faceuv8(0.5, 0.0, 1.0, 1.0), dtype=np.float32)
    
    # w mask=1: left block half, full z, left lineuv half
    _rdw = elemfaces([0, 0.25, 0], [8, 0.25, 16])
    for _fi in range(1, 6): _rdw[_fi, :, :] = 0.0
    BLOCK_ELEMS[REDSTONE_WIRE, 1] = _rdw
    BLOCK_TEX[REDSTONE_WIRE, 1, 0] = _rdlarr
    BLOCK_UVS[REDSTONE_WIRE, 1, 0] = np.array(faceuv8(0.0, 0.0, 0.5, 1.0), dtype=np.float32)
    
    # s mask=4: full x, south block half, bottom lineuv half (rot 90)
    _rds = elemfaces([0, 0.25, 8], [16, 0.25, 16])
    for _fi in range(1, 6): _rds[_fi, :, :] = 0.0
    BLOCK_ELEMS[REDSTONE_WIRE, 4] = _rds
    BLOCK_TEX[REDSTONE_WIRE, 4, 0] = _rdlarr
    BLOCK_UVS[REDSTONE_WIRE, 4, 0] = np.array(faceuv8(0.5, 0.0, 1.0, 1.0, 90), dtype=np.float32)
    
    # n mask=8: full x, north block half, top lineuv half (rot 90)
    _rdn = elemfaces([0, 0.25, 0], [16, 0.25, 8])
    for _fi in range(1, 6): _rdn[_fi, :, :] = 0.0
    BLOCK_ELEMS[REDSTONE_WIRE, 8] = _rdn
    BLOCK_TEX[REDSTONE_WIRE, 8, 0] = _rdlarr
    BLOCK_UVS[REDSTONE_WIRE, 8, 0] = np.array(faceuv8(0.0, 0.0, 0.5, 1.0, 90), dtype=np.float32)






# flat quad geometry; orient -> UV rotation
# after atlas vflip: arc @fuv(1,0)=BR
# 0 = SE, 90=NE, 180=NW, 270=SW

_rcurved = modeljson("normal_rail_curved")
if _rcurved:
    _rcelems, _rcfuvs, _rcftex = _rcurved
    _rcturned = atlasuv("blocks/rail_normal_turned")
    _cangles = [90, 180, 270, 0]  # NE, NW, SW, SE
    for _ci, _ca in enumerate(_cangles):
        _slot = 2 + _ci
        BLOCK_ELEMS[RAIL, _slot] = BLOCK_ELEMS[RAIL, 0].copy()
        _cuv = np.array(faceuv8(0.0, 0.0, 1.0, 1.0, _ca), dtype=np.float32)
        BLOCK_UVS[RAIL, _slot] = BLOCK_UVS[RAIL, 0].copy()
        BLOCK_UVS[RAIL, _slot, 0] = _cuv
        BLOCK_UVS[RAIL, _slot, 1] = _cuv
        if _rcftex:
            BLOCK_TEX[RAIL, _slot] = _rcftex[0].copy()
        if _rcturned:
            BLOCK_TEX[RAIL, _slot, 0] = np.array(_rcturned, dtype=np.float32)
            BLOCK_TEX[RAIL, _slot, 1] = np.array(_rcturned, dtype=np.float32)

# Stairs: 5 shapes * 4 orient, each has 2 straight/out || 3 inn.
# lookup idx = shape * 4 + orient (0-19, fits in 5-bit state field)

# lauout, max=48
#   shape           elems : slots  orientation
#   0     straight, 2     : 0- 7   0  + o *2
#   1     out l,    2     : 8-15   8  + o *2
#   2     out r,    2     : 16-23  16 + o *2
#   3     inn l,    3     : 24-35  24 + o *3
#   4     inn r,    3     : 36-47  36 + o *3
# orient -> y rpt deg

_srot = {0: 270, 1: 90, 2: 180, 3: 0}
_sbids = [
    OAK_STAIRS, SPRUCE_STAIRS, BIRCH_STAIRS, JUNGLE_STAIRS,
    ACACIA_STAIRS, DARK_OAK_STAIRS, STONE_STAIRS, COBBLESTONE_STAIRS,
    BRICK_STAIRS, STONE_BRICK_STAIRS, NETHER_BRICK_STAIRS,
    SANDSTONE_STAIRS, QUARTZ_STAIRS, RED_SANDSTONE_STAIRS,
]
_smcnms = {
    OAK_STAIRS:    "oak_stairs",    SPRUCE_STAIRS:      "spruce_stairs",
    BIRCH_STAIRS:  "birch_stairs",  JUNGLE_STAIRS:      "jungle_stairs",
    ACACIA_STAIRS: "acacia_stairs", DARK_OAK_STAIRS:    "dark_oak_stairs",
    STONE_STAIRS:  "stone_stairs",  COBBLESTONE_STAIRS: "cobblestone_stairs",
    BRICK_STAIRS:  "brick_stairs",  STONE_BRICK_STAIRS: "stone_brick_stairs",
    QUARTZ_STAIRS: "quartz_stairs", RED_SANDSTONE_STAIRS: "red_sandstone_stairs",
    NETHER_BRICK_STAIRS: "nether_brick_stairs", SANDSTONE_STAIRS: "sandstone_stairs",
}
for _sbid in _sbids:
    _mcb  = _smcnms[_sbid]
    _mcin = _mcb.replace("_stairs", "_inner_stairs")
    _mcout = _mcb.replace("_stairs", "_outer_stairs")

    _mc_s = modeljson(_mcb)
    _mc_i = modeljson(_mcin)
    _mc_o = modeljson(_mcout)
    if not _mc_s:
        continue

    _se, _sf, _st = _mc_s
    _ie, _if_, _it = _mc_i if _mc_i else (_se, _sf, _st)
    _oe, _of_, _ot = _mc_o if _mc_o else (_se, _sf, _st)
    _n_s = len(_se)
    _n_i = len(_ie)
    _n_o = len(_oe)

    # shape_defs: (shape_idx, elems, fuvs, ftex, n_elems, extra_rot)
    # extra_rot=0 for left variants, 90 for right variants
    _sdefs = [
        (0, _se, _sf,  _st, _n_s,  0),  # straight
        (1, _oe, _of_, _ot, _n_o, 90),  # out l
        (2, _oe, _of_, _ot, _n_o,  0),  # out r
        (3, _ie, _if_, _it, _n_i, 90),  # inn l
        (4, _ie, _if_, _it, _n_i,  0),  # inn r
    ]
    
    
    for _shape, _elems, _fuvs, _ftexs, _n_e, _xrot in _sdefs:
        
        for _ori, _bang in _srot.items():
            
            _angle = (_bang + _xrot) % 360
            if _shape < 3:    _bslot = _shape * 8 + _ori * 2
            elif _shape == 3: _bslot = 24 + _ori * 3
            else:             _bslot = 36 + _ori * 3
            
            
            _lookup = _shape * 4 + _ori
            STATE_ELEM_OFF[_sbid, _lookup] = _bslot
            STATE_ELEM_NUM[_sbid, _lookup] = _n_e
            for _ei in range(_n_e):
                _dslot = _bslot + _ei
                if _dslot >= MAX_ELEMS:
                    break
                    
                _relem = _elems[_ei].copy()
                if _angle != 0:
                    rotelem(_relem, [8, 0, 8], "y", _angle)
                BLOCK_ELEMS[_sbid, _dslot] = _relem
                BLOCK_UVS[_sbid, _dslot] = _fuvs[_ei]
                BLOCK_TEX[_sbid, _dslot] = _ftexs[_ei]

# repeater & comparator : 4 hor ori
# state=0 FACE_N stored (look S) -> S -> 180
# state=1 FACE_S stored (look N) -> N -> 0
# state=2 FACE_E stored (look W) -> W -> 90
# state=3 FACE_W stored (look E) -> E -> 270
_frot = {0: 180, 1: 0, 2: 90, 3: 270}

for _rbid, _rmcnm, _rtx in [
    (
        REPEATER, "repeater_1tick", {
            "slab":  "blocks/stone_slab_top",
            "top":   "blocks/repeater_off",
            "unlit": "blocks/redstone_torch_off"
        }
    ),
    (
        COMPARATOR, "comparator_unlit", {
            "slab": "blocks/stone_slab_top",
            "top": "blocks/comparator_off",
            "unlit": "blocks/redstone_torch_off",
            "lit": "blocks/redstone_torch_on"
        }
    ),
]:
    _rmc = modeljson(_rmcnm, _rtx)
    if not _rmc: continue
    
    
    _relms, _rfuvs, _rftex = _rmc
    _nr = len(_relms)
    
    for _facing, _angle in _frot.items():
        _bslot = _facing * _nr
        STATE_ELEM_OFF[_rbid, _facing] = _bslot
        for _ei in range(_nr):
            _dslot = _bslot + _ei
            if _dslot >= MAX_ELEMS:
                break
            _relem = _relms[_ei].copy()
            if _angle != 0:
                rotelem(_relem, [8, 0, 8], "y", _angle)
            BLOCK_ELEMS[_rbid, _dslot] = _relem
            if _rfuvs and _ei < len(_rfuvs): BLOCK_UVS[_rbid, _dslot] = _rfuvs[_ei]
            if _rftex and _ei < len(_rftex): BLOCK_TEX[_rbid, _dslot] = _rftex[_ei]

BLOCK_CUSTOM_FACES = BLOCK_ELEMS[:, 0, :, :, :]
BLOCK_STATE_HEIGHT = np.zeros(MAX_CUSTOM, dtype=np.bool_)
BLOCK_TYPE_CULL    = np.zeros(MAX_CUSTOM, dtype=np.bool_)

# neighbor conNs
CONNECT_NONE = 0
CONNECT_FENCE = 1   # fences
CONNECT_WALL = 2    # walls

FAMILY_NONE = 0
FAMILY_FENCE = 1         # fences + gates
FAMILY_NETHER_FENCE = 2 
FAMILY_WALL = 3          # cobble walls
FAMILY_PANE = 4 
FAMILY_BARS = 5 

MAX_ARM_ELEMS = 4

# arm arrays: [bid, direction(N=0/S=1/E=2/W=3), arm_elem_idx, face, vert, xyz]
CONNECT_TYPE   = np.zeros(MAX_CUSTOM, dtype=np.int32)
CONNECT_FAMILY = np.zeros(MAX_CUSTOM, dtype=np.int32)
BLOCK_ARM_NUM  = np.zeros((MAX_CUSTOM, 4), dtype=np.int32)
BLOCK_ARM_ELEM = np.zeros((MAX_CUSTOM, 4, MAX_ARM_ELEMS, 6, 6, 3), dtype=np.float32)
BLOCK_ARM_FUVS = np.zeros((MAX_CUSTOM, 4, MAX_ARM_ELEMS, 6, 8),    dtype=np.float32)
BLOCK_ARM_FTEX = np.full((MAX_CUSTOM,  4, MAX_ARM_ELEMS, 6, 2), -1.0, dtype=np.float32)

for _i in range(8):
    BLOCK_ARM_FUVS[:, :, :, :, _i] = _default_uv8[_i]


def elemfaceuvs(from_c, to_c):
    x0, y0, z0 = from_c[0], from_c[1], from_c[2]
    x1, y1, z1 = to_c[0], to_c[1], to_c[2]
    r = np.zeros((6, 8), dtype=np.float32)
    r[0] = faceuv8(x0/16, z0/16, x1/16, z1/16)         # top u=x v=z
    r[1] = faceuv8(x0/16, z0/16, x1/16, z1/16)         # bot u=x v=z
    r[2] = faceuv8(x0/16, (16-y1)/16, x1/16, (16-y0)/16)  # n
    r[3] = faceuv8(x0/16, (16-y1)/16, x1/16, (16-y0)/16)  # s
    r[4] = faceuv8(z0/16, (16-y1)/16, z1/16, (16-y0)/16)  # e  u=Z
    r[5] = faceuv8(z0/16, (16-y1)/16, z1/16, (16-y0)/16)  # w  u=Z
    return r


def regarms(bid, n, adefs):
    atlas = atlasuv(f"blocks/{n}")
    for di, bars in enumerate(adefs):
        BLOCK_ARM_NUM[bid, di] = len(bars)
        for ai, (f, t) in enumerate(bars):
            BLOCK_ARM_ELEM[bid, di, ai] = elemfaces(f, t)
            BLOCK_ARM_FUVS[bid, di, ai] = elemfaceuvs(f, t)
            if atlas:
                for fi in range(6):
                    BLOCK_ARM_FTEX[bid, di, ai, fi] = atlas


def regfencearms(bid, n):
    regarms(bid, n, [
        [([7,12,0],[9,15,6]),  ([7,6,0],[9,9,6])],  # n
        [([7,12,10],[9,15,16]),([7,6,10],[9,9,16])], # s
        [([10,12,7],[16,15,9]),([10,6,7],[16,9,9])], # e
        [([0,12,7],[6,15,9]),  ([0,6,7],[6,9,9])],   # w
    ])


def regwallarms(bid, n):
    regarms(bid, n, [
        [([5,0,0],[11,13,4])],   # n
        [([5,0,12],[11,13,16])], # s
        [([12,0,5],[16,13,11])], # e
        [([0,0,5],[4,13,11])],   # w
    ])


def regpanearms(bid, ptx, etx):
    # n/s arms: glass e/w
    # e/w arms: glass n/s
    patl = atlasuv(f"blocks/{ptx}")
    eatl = atlasuv(f"blocks/{etx}")
    aco  = [
        ([7, 0, 0], [9, 16, 7]),    # n
        ([7, 0, 9], [9, 16, 16]),   # s
        ([9, 0, 7], [16, 16, 9]),   # e
        ([0, 0, 7], [7, 16, 9]),    # w
    ]
    gfi = [{4, 5}, {4, 5}, {2, 3}, {2, 3}]
    for di, (f, t) in enumerate(aco):
        BLOCK_ARM_NUM[bid, di] = 1
        BLOCK_ARM_ELEM[bid, di, 0] = elemfaces(f, t)
        BLOCK_ARM_FUVS[bid, di, 0] = elemfaceuvs(f, t)
        
        
        for fi in range(6):
            if fi in gfi[di]:
                if patl:   BLOCK_ARM_FTEX[bid, di, 0, fi] = patl
            else: 
                if eatl: BLOCK_ARM_FTEX[bid, di, 0, fi] = eatl


def regbarsarms(bid, n):
    regarms(bid, n, [
        [([7, 0, 0], [9, 16, 7])],  # n
        [([7, 0, 9], [9, 16, 16])], # s
        [([9, 0, 7], [16, 16, 9])], # e
        [([0, 0, 7], [7, 16, 9])],  # w
    ])


_ftexs = {
    OAK_FENCE: "planks_oak",       SPRUCE_FENCE: "planks_spruce",
    BIRCH_FENCE: "planks_birch",   JUNGLE_FENCE: "planks_jungle",
    ACACIA_FENCE: "planks_acacia", DARK_OAK_FENCE: "planks_big_oak",
    NETHER_BRICK_FENCE: "nether_brick",
}
for bid, tex in _ftexs.items():
    regfencearms(bid, tex)
    CONNECT_TYPE[bid]   = CONNECT_FENCE
    CONNECT_FAMILY[bid] = FAMILY_NETHER_FENCE if bid == NETHER_BRICK_FENCE else FAMILY_FENCE

# fence gates connect-to by fences but have no arms
for bid in [
    OAK_FENCE_GATE, SPRUCE_FENCE_GATE, BIRCH_FENCE_GATE,
    JUNGLE_FENCE_GATE, ACACIA_FENCE_GATE, DARK_OAK_FENCE_GATE
]:
    CONNECT_FAMILY[bid] = FAMILY_FENCE

regwallarms(COBBLESTONE_WALL, "cobblestone")
CONNECT_TYPE[COBBLESTONE_WALL]   = CONNECT_WALL
CONNECT_FAMILY[COBBLESTONE_WALL] = FAMILY_WALL

regwallarms(MOSSY_COBBLESTONE_WALL, "cobblestone_mossy")
CONNECT_TYPE[MOSSY_COBBLESTONE_WALL]   = CONNECT_WALL
CONNECT_FAMILY[MOSSY_COBBLESTONE_WALL] = FAMILY_WALL

for _gpid, _ptx, _etx in _pvars:
    regpanearms(_gpid, _ptx, _etx)
    CONNECT_TYPE[_gpid]   = CONNECT_FENCE
    CONNECT_FAMILY[_gpid] = FAMILY_PANE

regbarsarms(IRON_BARS, "iron_bars")
CONNECT_TYPE[IRON_BARS]   = CONNECT_FENCE
CONNECT_FAMILY[IRON_BARS] = FAMILY_BARS


def iscustom(bid): return bid in CUSTOM_BLOCKS
def numelems(bid): return NUM_ELEMENTS[bid]
def rendermode(bid): return BLOCK_MODE_RENDER[bid]
