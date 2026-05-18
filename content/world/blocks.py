ATLAS_W = 20
ATLAS_H = 19

UV_W = 1.0 / ATLAS_W # 0.05
UV_H = 1.0 / ATLAS_H # ~0.0526


# text nm -> (u_index, v_index) in atlas
# v_index <- top of image
TEXTURES = {
    "anvil_base": (0, 0),
    "anvil_top_damaged_0": (1, 0),
    "anvil_top_damaged_1": (2, 0),
    "anvil_top_damaged_2": (3, 0),
    "beacon": (4, 0),
    "bed_feet_end": (5, 0),
    "bed_feet_side": (6, 0),
    "bed_feet_top": (7, 0),
    "bed_head_end": (8, 0),
    "bed_head_side": (9, 0),
    "bed_head_top": (10, 0),
    "bedrock": (11, 0),
    "bookshelf": (12, 0),
    "brewing_stand": (13, 0),
    "brewing_stand_base": (14, 0),
    "brick": (15, 0),
    "cactus_bottom": (16, 0),
    "cactus_side": (17, 0),
    "cactus_top": (18, 0),
    "cake_bottom": (19, 0),
    
    
    "cake_inner": (0, 1),
    "cake_side": (1, 1),
    "cake_top": (2, 1),
    "carrots_stage_0": (3, 1),
    "carrots_stage_1": (4, 1),
    "carrots_stage_2": (5, 1),
    "carrots_stage_3": (6, 1),
    "cauldron_bottom": (7, 1),
    "cauldron_inner": (8, 1),
    "cauldron_side": (9, 1),
    "cauldron_top": (10, 1),
    "clay": (11, 1),
    "coal_block": (12, 1),
    "coal_ore": (13, 1),
    "coarse_dirt": (14, 1),
    "cobblestone": (15, 1),
    "cobblestone_mossy": (16, 1),
    "cocoa_stage_0": (17, 1),
    "cocoa_stage_1": (18, 1),
    "cocoa_stage_2": (19, 1),
    
    
    "command_block": (0, 2),
    "comparator_off": (1, 2),
    "comparator_on": (2, 2),
    "crafting_table_front": (3, 2),
    "crafting_table_side": (4, 2),
    "crafting_table_top": (5, 2),
    "daylight_detector_inverted_top": (6, 2),
    "daylight_detector_side": (7, 2),
    "daylight_detector_top": (8, 2),
    "deadbush": (9, 2),
    "destroy_stage_0": (10, 2),
    "destroy_stage_1": (11, 2),
    "destroy_stage_2": (12, 2),
    "destroy_stage_3": (13, 2),
    "destroy_stage_4": (14, 2),
    "destroy_stage_5": (15, 2),
    "destroy_stage_6": (16, 2),
    "destroy_stage_7": (17, 2),
    "destroy_stage_8": (18, 2),
    "destroy_stage_9": (19, 2),
    
    
    "diamond_block": (0, 3),
    "diamond_ore": (1, 3),
    "dirt": (2, 3),
    "dirt_podzol_side": (3, 3),
    "dirt_podzol_top": (4, 3),
    "dispenser_front_horizontal": (5, 3),
    "dispenser_front_vertical": (6, 3),
    "door_acacia_lower": (7, 3),
    "door_acacia_upper": (8, 3),
    "door_birch_lower": (9, 3),
    "door_birch_upper": (10, 3),
    "door_dark_oak_lower": (11, 3),
    "door_dark_oak_upper": (12, 3),
    "door_iron_lower": (13, 3),
    "door_iron_upper": (14, 3),
    "door_jungle_lower": (15, 3),
    "door_jungle_upper": (16, 3),
    "door_spruce_lower": (17, 3),
    "door_spruce_upper": (18, 3),
    "door_wood_lower": (19, 3),
    
    
    "door_wood_upper": (0, 4),
    "double_plant_fern_bottom": (1, 4),
    "double_plant_fern_top": (2, 4),
    "double_plant_grass_bottom": (3, 4),
    "double_plant_grass_top": (4, 4),
    "double_plant_paeonia_bottom": (5, 4),
    "double_plant_paeonia_top": (6, 4),
    "double_plant_rose_bottom": (7, 4),
    "double_plant_rose_top": (8, 4),
    "double_plant_sunflower_back": (9, 4),
    "double_plant_sunflower_bottom": (10, 4),
    "double_plant_sunflower_front": (11, 4),
    "double_plant_sunflower_top": (12, 4),
    "double_plant_syringa_bottom": (13, 4),
    "double_plant_syringa_top": (14, 4),
    "dragon_egg": (15, 4),
    "dropper_front_horizontal": (16, 4),
    "dropper_front_vertical": (17, 4),
    "emerald_block": (18, 4),
    "emerald_ore": (19, 4),
    
    
    "enchanting_table_bottom": (0, 5),
    "enchanting_table_side": (1, 5),
    "enchanting_table_top": (2, 5),
    "end_stone": (3, 5),
    "endframe_eye": (4, 5),
    "endframe_side": (5, 5),
    "endframe_top": (6, 5),
    "farmland_dry": (7, 5),
    "farmland_wet": (8, 5),
    "fern": (9, 5),
    "fire_layer_0": (10, 5),
    "fire_layer_1": (11, 5),
    "flower_allium": (12, 5),
    "flower_blue_orchid": (13, 5),
    "flower_dandelion": (14, 5),
    "flower_houstonia": (15, 5),
    "flower_oxeye_daisy": (16, 5),
    "flower_pot": (17, 5),
    "flower_rose": (18, 5),
    "flower_tulip_orange": (19, 5),
    
    
    "flower_tulip_pink": (0, 6),
    "flower_tulip_red": (1, 6),
    "flower_tulip_white": (2, 6),
    "furnace_front_off": (3, 6),
    "furnace_front_on": (4, 6),
    "furnace_side": (5, 6),
    "furnace_top": (6, 6),
    "glass": (7, 6),
    "glass_black": (8, 6),
    "glass_blue": (9, 6),
    "glass_brown": (10, 6),
    "glass_cyan": (11, 6),
    "glass_gray": (12, 6),
    "glass_green": (13, 6),
    "glass_light_blue": (14, 6),
    "glass_lime": (15, 6),
    "glass_magenta": (16, 6),
    "glass_orange": (17, 6),
    "glass_pane_top": (18, 6),
    "glass_pane_top_black": (19, 6),
    
    
    "glass_pane_top_blue": (0, 7),
    "glass_pane_top_brown": (1, 7),
    "glass_pane_top_cyan": (2, 7),
    "glass_pane_top_gray": (3, 7),
    "glass_pane_top_green": (4, 7),
    "glass_pane_top_light_blue": (5, 7),
    "glass_pane_top_lime": (6, 7),
    "glass_pane_top_magenta": (7, 7),
    "glass_pane_top_orange": (8, 7),
    "glass_pane_top_pink": (9, 7),
    "glass_pane_top_purple": (10, 7),
    "glass_pane_top_red": (11, 7),
    "glass_pane_top_silver": (12, 7),
    "glass_pane_top_white": (13, 7),
    "glass_pane_top_yellow": (14, 7),
    "glass_pink": (15, 7),
    "glass_purple": (16, 7),
    "glass_red": (17, 7),
    "glass_silver": (18, 7),
    "glass_white": (19, 7),
    
    
    "glass_yellow": (0, 8),
    "glowstone": (1, 8),
    "gold_block": (2, 8),
    "gold_ore": (3, 8),
    "grass_side": (4, 8),
    "grass_side_overlay": (5, 8),
    "grass_side_snowed": (6, 8),
    "grass_top": (7, 8),
    "gravel": (8, 8),
    "hardened_clay": (9, 8),
    "hardened_clay_stained_black": (10, 8),
    "hardened_clay_stained_blue": (11, 8),
    "hardened_clay_stained_brown": (12, 8),
    "hardened_clay_stained_cyan": (13, 8),
    "hardened_clay_stained_gray": (14, 8),
    "hardened_clay_stained_green": (15, 8),
    "hardened_clay_stained_light_blue": (16, 8),
    "hardened_clay_stained_lime": (17, 8),
    "hardened_clay_stained_magenta": (18, 8),
    "hardened_clay_stained_orange": (19, 8),
    
    
    "hardened_clay_stained_pink": (0, 9),
    "hardened_clay_stained_red": (1, 9),
    "hardened_clay_stained_silver": (2, 9),
    "hardened_clay_stained_white": (3, 9),
    "hardened_clay_stained_yellow": (4, 9),
    "hay_block_side": (5, 9),
    "hay_block_top": (6, 9),
    "hopper_inside": (7, 9),
    "hopper_outside": (8, 9),
    "hopper_top": (9, 9),
    "ice": (10, 9),
    "ice_packed": (11, 9),
    "iron_bars": (12, 9),
    "iron_block": (13, 9),
    "iron_ore": (14, 9),
    "iron_trapdoor": (15, 9),
    "jukebox_side": (16, 9),
    "jukebox_top": (17, 9),
    "ladder": (18, 9),
    "lapis_block": (19, 9),
    
    
    "lapis_ore": (0, 10),
    "lava_flow": (1, 10),
    "lava_still": (2, 10),
    "leaves_acacia": (3, 10),
    "leaves_big_oak": (4, 10),
    "leaves_birch": (5, 10),
    "leaves_jungle": (6, 10),
    "leaves_oak": (7, 10),
    "leaves_spruce": (8, 10),
    "lever": (9, 10),
    "log_acacia": (10, 10),
    "log_acacia_top": (11, 10),
    "log_big_oak": (12, 10),
    "log_big_oak_top": (13, 10),
    "log_birch": (14, 10),
    "log_birch_top": (15, 10),
    "log_jungle": (16, 10),
    "log_jungle_top": (17, 10),
    "log_oak": (18, 10),
    "log_oak_top": (19, 10),
    
    
    "log_spruce": (0, 11),
    "log_spruce_top": (1, 11),
    "melon_side": (2, 11),
    "melon_stem_connected": (3, 11),
    "melon_stem_disconnected": (4, 11),
    "melon_top": (5, 11),
    "mob_spawner": (6, 11),
    "mushroom_block_inside": (7, 11),
    "mushroom_block_skin_brown": (8, 11),
    "mushroom_block_skin_red": (9, 11),
    "mushroom_block_skin_stem": (10, 11),
    "mushroom_brown": (11, 11),
    "mushroom_red": (12, 11),
    "mycelium_side": (13, 11),
    "mycelium_top": (14, 11),
    "nether_brick": (15, 11),
    "nether_wart_stage_0": (16, 11),
    "nether_wart_stage_1": (17, 11),
    "nether_wart_stage_2": (18, 11),
    "netherrack": (19, 11),
    
    
    "noteblock": (0, 12),
    "obsidian": (1, 12),
    "piston_bottom": (2, 12),
    "piston_inner": (3, 12),
    "piston_side": (4, 12),
    "piston_top_normal": (5, 12),
    "piston_top_sticky": (6, 12),
    "planks_acacia": (7, 12),
    "planks_big_oak": (8, 12),
    "planks_birch": (9, 12),
    "planks_jungle": (10, 12),
    "planks_oak": (11, 12),
    "planks_spruce": (12, 12),
    "potatoes_stage_0": (13, 12),
    "potatoes_stage_1": (14, 12),
    "potatoes_stage_2": (15, 12),
    "potatoes_stage_3": (16, 12),
    "prismarine_bricks": (17, 12),
    "prismarine_dark": (18, 12),
    "prismarine_rough": (19, 12),
    
    
    "pumpkin_face_off": (0, 13),
    "pumpkin_face_on": (1, 13),
    "pumpkin_side": (2, 13),
    "pumpkin_stem_connected": (3, 13),
    "pumpkin_stem_disconnected": (4, 13),
    "pumpkin_top": (5, 13),
    "quartz_block_bottom": (6, 13),
    "quartz_block_chiseled": (7, 13),
    "quartz_block_chiseled_top": (8, 13),
    "quartz_block_lines": (9, 13),
    "quartz_block_lines_top": (10, 13),
    "quartz_block_side": (11, 13),
    "quartz_block_top": (12, 13),
    "quartz_ore": (13, 13),
    "rail_activator": (14, 13),
    "rail_activator_powered": (15, 13),
    "rail_detector": (16, 13),
    "rail_detector_powered": (17, 13),
    "rail_golden": (18, 13),
    "rail_golden_powered": (19, 13),
    
    
    "rail_normal": (0, 14),
    "rail_normal_turned": (1, 14),
    "red_sand": (2, 14),
    "red_sandstone_bottom": (3, 14),
    "red_sandstone_carved": (4, 14),
    "red_sandstone_normal": (5, 14),
    "red_sandstone_smooth": (6, 14),
    "red_sandstone_top": (7, 14),
    "redstone_block": (8, 14),
    "redstone_lamp_off": (9, 14),
    "redstone_lamp_on": (10, 14),
    "redstone_ore": (11, 14),
    "redstone_torch_off": (12, 14),
    "redstone_torch_on": (13, 14),
    "reeds": (14, 14),
    "repeater_off": (15, 14),
    "repeater_on": (16, 14),
    "sand": (17, 14),
    "sandstone_bottom": (18, 14),
    "sandstone_carved": (19, 14),
    
    
    "sandstone_normal": (0, 15),
    "sandstone_smooth": (1, 15),
    "sandstone_top": (2, 15),
    "sapling_acacia": (3, 15),
    "sapling_birch": (4, 15),
    "sapling_jungle": (5, 15),
    "sapling_oak": (6, 15),
    "sapling_roofed_oak": (7, 15),
    "sapling_spruce": (8, 15),
    "sea_lantern": (9, 15),
    "slime": (10, 15),
    "snow": (11, 15),
    "soul_sand": (12, 15),
    "sponge": (13, 15),
    "sponge_wet": (14, 15),
    "stone": (15, 15),
    "stone_andesite": (16, 15),
    "stone_andesite_smooth": (17, 15),
    "stone_diorite": (18, 15),
    "stone_diorite_smooth": (19, 15),
    
    
    "stone_granite": (0, 16),
    "stone_granite_smooth": (1, 16),
    "stone_slab_side": (2, 16),
    "stone_slab_top": (3, 16),
    "stonebrick": (4, 16),
    "stonebrick_carved": (5, 16),
    "stonebrick_cracked": (6, 16),
    "stonebrick_mossy": (7, 16),
    "tallgrass": (8, 16),
    "tnt_bottom": (9, 16),
    "tnt_side": (10, 16),
    "tnt_top": (11, 16),
    "torch_on": (12, 16),
    "trapdoor": (13, 16),
    "trip_wire_source": (14, 16),
    "vine": (15, 16),
    "water_flow": (16, 16),
    "water_still": (17, 16),
    "waterlily": (18, 16),
    "web": (19, 16),
    
    
    "wheat_stage_0": (0, 17),
    "wheat_stage_1": (1, 17),
    "wheat_stage_2": (2, 17),
    "wheat_stage_3": (3, 17),
    "wheat_stage_4": (4, 17),
    "wheat_stage_5": (5, 17),
    "wheat_stage_6": (6, 17),
    "wheat_stage_7": (7, 17),
    "wool_colored_black": (8, 17),
    "wool_colored_blue": (9, 17),
    "wool_colored_brown": (10, 17),
    "wool_colored_cyan": (11, 17),
    "wool_colored_gray": (12, 17),
    "wool_colored_green": (13, 17),
    "wool_colored_light_blue": (14, 17),
    "wool_colored_lime": (15, 17),
    "wool_colored_magenta": (16, 17),
    "wool_colored_orange": (17, 17),
    "wool_colored_pink": (18, 17),
    "wool_colored_purple": (19, 17),
    
    
    "wool_colored_red": (0, 18),
    "wool_colored_silver": (1, 18),
    "wool_colored_white": (2, 18),
    "wool_colored_yellow": (3, 18),
    
    
    "redstone_dust_dot": (4, 18),
    "redstone_dust_line0": (5, 18),
    "redstone_dust_line1": (6, 18),
    "item_frame": (7, 18),
    # (4,18) full cross
    # "dot" = center UV crop [5,5,11,11]
    "redstone_dust_cross": (4, 18),
    "redstone_dust_line": (5, 18),
}


def getuv(texture_name):
    if texture_name not in TEXTURES:
        return (0.0, 0.0)
    ui, vi = TEXTURES[texture_name]
    u0 = ui * UV_W
    v0 = 1.0 - (vi + 1) * UV_H
    return (u0, v0)


AIR = 0
GRASS = 1
DIRT = 2
STONE = 3
BEDROCK = 4
WATER = 5
SAND = 6
OAK_LOG = 7
OAK_LEAVES = 8
BIRCH_LEAVES = 9
TALLGRASS = 10
ANDESITE = 11
GRAVEL = 12
COARSE_DIRT = 13
SANDSTONE = 14

COBBLESTONE = 15
COBBLESTONE_MOSSY = 16
OAK_PLANKS = 17
SPRUCE_PLANKS = 18
BIRCH_PLANKS = 19
JUNGLE_PLANKS = 20
ACACIA_PLANKS = 21
DARK_OAK_PLANKS = 22
GLASS = 23
COAL_ORE = 24
IRON_ORE = 25
GOLD_ORE = 26
DIAMOND_ORE = 27
EMERALD_ORE = 28
REDSTONE_ORE = 29
LAPIS_ORE = 30
COAL_BLOCK = 31
IRON_BLOCK = 32
GOLD_BLOCK = 33
DIAMOND_BLOCK = 34
EMERALD_BLOCK = 35
REDSTONE_BLOCK = 36
LAPIS_BLOCK = 37
BRICK = 38
STONEBRICK = 39
STONEBRICK_MOSSY = 40
STONEBRICK_CRACKED = 41
STONEBRICK_CARVED = 42
NETHER_BRICK = 43
OBSIDIAN = 44
GLOWSTONE = 45
CLAY = 46
SNOW = 47
ICE = 48
ICE_PACKED = 49
NETHERRACK = 50
SOUL_SAND = 51
END_STONE = 52
PRISMARINE = 53
PRISMARINE_BRICKS = 54
PRISMARINE_DARK = 55
SEA_LANTERN = 56
SPONGE = 57
SPONGE_WET = 58
SLIME = 59
TNT = 60
BOOKSHELF = 61
CRAFTING_TABLE = 62
FURNACE = 63
NOTEBLOCK = 64
JUKEBOX = 65
MELON = 66
PUMPKIN = 67
JACK_O_LANTERN = 68
HAY_BLOCK = 69
CACTUS = 70
SPRUCE_LOG = 71
BIRCH_LOG = 72
JUNGLE_LOG = 73
ACACIA_LOG = 74
DARK_OAK_LOG = 75
SPRUCE_LEAVES = 76
JUNGLE_LEAVES = 77
ACACIA_LEAVES = 78
DARK_OAK_LEAVES = 79
QUARTZ_BLOCK = 80
QUARTZ_CHISELED = 81
QUARTZ_PILLAR = 82
SANDSTONE_CARVED = 83
SANDSTONE_SMOOTH = 84
RED_SAND = 85
RED_SANDSTONE = 86
RED_SANDSTONE_CARVED = 87
RED_SANDSTONE_SMOOTH = 88
HARDENED_CLAY = 89
MYCELIUM = 90
PODZOL = 91
REDSTONE_LAMP = 92
REDSTONE_LAMP_ON = 93
MOB_SPAWNER = 94
COMMAND_BLOCK = 95
DRAGON_EGG = 96
BEACON = 97
DIORITE = 98
DIORITE_SMOOTH = 99
GRANITE = 100
GRANITE_SMOOTH = 101
ANDESITE_SMOOTH = 102


WOOL_WHITE = 103
WOOL_ORANGE = 104
WOOL_MAGENTA = 105
WOOL_LIGHT_BLUE = 106
WOOL_YELLOW = 107
WOOL_LIME = 108
WOOL_PINK = 109
WOOL_GRAY = 110
WOOL_SILVER = 111
WOOL_CYAN = 112
WOOL_PURPLE = 113
WOOL_BLUE = 114
WOOL_BROWN = 115
WOOL_GREEN = 116
WOOL_RED = 117
WOOL_BLACK = 118

GLASS_WHITE = 119
GLASS_ORANGE = 120
GLASS_MAGENTA = 121
GLASS_LIGHT_BLUE = 122
GLASS_YELLOW = 123
GLASS_LIME = 124
GLASS_PINK = 125
GLASS_GRAY = 126
GLASS_SILVER = 127
GLASS_CYAN = 128
GLASS_PURPLE = 129
GLASS_BLUE = 130
GLASS_BROWN = 131
GLASS_GREEN = 132
GLASS_RED = 133
GLASS_BLACK = 134




CLAY_WHITE = 135
CLAY_ORANGE = 136
CLAY_MAGENTA = 137
CLAY_LIGHT_BLUE = 138
CLAY_YELLOW = 139
CLAY_LIME = 140
CLAY_PINK = 141
CLAY_GRAY = 142
CLAY_SILVER = 143
CLAY_CYAN = 144
CLAY_PURPLE = 145  # TODO add to atlas
CLAY_BLUE = 146
CLAY_BROWN = 147
CLAY_GREEN = 148
CLAY_RED = 149
CLAY_BLACK = 150

# anim
LAVA = 151
FIRE = 152
FURNACE_ON = 153
WATER_FLOWING = 154
LAVA_FLOWING = 155

# custom geometry
BARRIER = 156
HOPPER = 157
CAULDRON = 158
REDSTONE_WIRE = 159
REPEATER = 160
COMPARATOR = 161
CAKE = 162
OAK_DOOR_BOTTOM = 163
OAK_DOOR_TOP = 164
IRON_DOOR_BOTTOM = 165
IRON_DOOR_TOP = 166
BED_HEAD = 167
BED_FOOT = 168
SIGN_STANDING = 169
ITEM_FRAME_BLOCK = 170
BREWING_STAND_BLOCK = 171


SAPLING_OAK = 172
SAPLING_SPRUCE = 173
SAPLING_BIRCH = 174
SAPLING_JUNGLE = 175
SAPLING_ACACIA = 176
SAPLING_DARK_OAK = 177


DANDELION = 178
POPPY = 179
BLUE_ORCHID = 180
ALLIUM = 181
AZURE_BLUET = 182
RED_TULIP = 183
ORANGE_TULIP = 184
WHITE_TULIP = 185
PINK_TULIP = 186
OXEYE_DAISY = 187
BROWN_MUSHROOM = 188
RED_MUSHROOM = 189
DEAD_BUSH = 190
FERN = 191



SUNFLOWER = 192
LILAC = 193
DOUBLE_TALLGRASS = 194
LARGE_FERN = 195
ROSE_BUSH = 196
PEONY = 197


RAIL = 198
POWERED_RAIL = 199
POWERED_RAIL_ON = 200
DETECTOR_RAIL = 201
ACTIVATOR_RAIL = 202


TORCH = 203
REDSTONE_TORCH_OFF = 204
REDSTONE_TORCH_ON = 205



OAK_STAIRS = 206
SPRUCE_STAIRS = 207
BIRCH_STAIRS = 208
JUNGLE_STAIRS = 209
ACACIA_STAIRS = 210
DARK_OAK_STAIRS = 211
STONE_STAIRS = 212
COBBLESTONE_STAIRS = 213
BRICK_STAIRS = 214
STONE_BRICK_STAIRS = 215
NETHER_BRICK_STAIRS = 216
SANDSTONE_STAIRS = 217
QUARTZ_STAIRS = 218
RED_SANDSTONE_STAIRS = 219


STONE_SLAB = 220
SANDSTONE_SLAB = 221
COBBLESTONE_SLAB = 222
BRICK_SLAB = 223
STONE_BRICK_SLAB = 224
NETHER_BRICK_SLAB = 225
QUARTZ_SLAB = 226
OAK_SLAB = 227
SPRUCE_SLAB = 228
BIRCH_SLAB = 229
JUNGLE_SLAB = 230
ACACIA_SLAB = 231
DARK_OAK_SLAB = 232
RED_SANDSTONE_SLAB = 233


OAK_FENCE = 234
SPRUCE_FENCE = 235
BIRCH_FENCE = 236
JUNGLE_FENCE = 237
ACACIA_FENCE = 238
DARK_OAK_FENCE = 239
NETHER_BRICK_FENCE = 240



OAK_FENCE_GATE = 241
SPRUCE_FENCE_GATE = 242
BIRCH_FENCE_GATE = 243
JUNGLE_FENCE_GATE = 244
ACACIA_FENCE_GATE = 245
DARK_OAK_FENCE_GATE = 246



COBBLESTONE_WALL = 247
MOSSY_COBBLESTONE_WALL = 248
SPRUCE_DOOR_BOTTOM = 249
SPRUCE_DOOR_TOP = 250
BIRCH_DOOR_BOTTOM = 251
BIRCH_DOOR_TOP = 252
JUNGLE_DOOR_BOTTOM = 253
JUNGLE_DOOR_TOP = 254
ACACIA_DOOR_BOTTOM = 255
ACACIA_DOOR_TOP = 256
DARK_OAK_DOOR_BOTTOM = 257
DARK_OAK_DOOR_TOP = 258


STONE_BUTTON = 259
WOODEN_BUTTON = 260
STONE_PRESSURE_PLATE = 261
WOODEN_PRESSURE_PLATE = 262
LIGHT_WEIGHTED_PRESSURE_PLATE = 263
HEAVY_WEIGHTED_PRESSURE_PLATE = 264

OAK_TRAPDOOR = 265
IRON_TRAPDOOR = 266
LADDER = 267


PISTON = 268
STICKY_PISTON = 269
PISTON_HEAD = 270

DISPENSER = 271
DROPPER = 272

CHEST = 273
TRAPPED_CHEST = 274
ENDER_CHEST = 275

COBWEB = 276
LEVER = 277
TRIPWIRE_HOOK = 278
DAYLIGHT_DETECTOR = 279
DAYLIGHT_DETECTOR_INVERTED = 280

BROWN_MUSHROOM_BLOCK = 281
RED_MUSHROOM_BLOCK = 282

IRON_BARS = 283
GLASS_PANE = 284

VINE = 285
LILY_PAD = 286

WHEAT_STAGE_7 = 287
CARROTS_STAGE_3 = 288
POTATOES_STAGE_3 = 289
NETHER_WART_STAGE_2 = 290

ENCHANTING_TABLE = 291
ANVIL = 292
ANVIL_SLIGHTLY_DAMAGED = 293
ANVIL_VERY_DAMAGED = 294

END_PORTAL_FRAME = 295

FARMLAND_DRY = 296
FARMLAND_WET = 297

MONSTER_EGG_STONE = 298
MONSTER_EGG_COBBLESTONE = 299
MONSTER_EGG_STONEBRICK = 300

CARPET_WHITE = 301
CARPET_ORANGE = 302
CARPET_MAGENTA = 303
CARPET_LIGHT_BLUE = 304
CARPET_YELLOW = 305
CARPET_LIME = 306
CARPET_PINK = 307
CARPET_GRAY = 308
CARPET_SILVER = 309
CARPET_CYAN = 310
CARPET_PURPLE = 311
CARPET_BLUE = 312
CARPET_BROWN = 313
CARPET_GREEN = 314
CARPET_RED = 315
CARPET_BLACK = 316


GLASS_PANE_WHITE = 317
GLASS_PANE_ORANGE = 318
GLASS_PANE_MAGENTA = 319
GLASS_PANE_LIGHT_BLUE = 320
GLASS_PANE_YELLOW = 321
GLASS_PANE_LIME = 322
GLASS_PANE_PINK = 323
GLASS_PANE_GRAY = 324
GLASS_PANE_SILVER = 325
GLASS_PANE_CYAN = 326
GLASS_PANE_PURPLE = 327
GLASS_PANE_BLUE = 328
GLASS_PANE_BROWN = 329
GLASS_PANE_GREEN = 330
GLASS_PANE_RED = 331
GLASS_PANE_BLACK = 332
SUGAR_CANE = 333
COCOA = 334
SNOW_BLOCK = 335


# top, bottom, north -z , south +z, east +x, west-x
BLOCK_FACES = {
    GRASS: ("grass_top", "dirt", "grass_side", "grass_side", "grass_side", "grass_side"),
    DIRT: "dirt",
    STONE: "stone",
    BEDROCK: "bedrock",
    SAND: "sand",
    OAK_LOG: ("log_oak_top", "log_oak_top", "log_oak", "log_oak", "log_oak", "log_oak"),
    OAK_LEAVES: "leaves_oak",
    BIRCH_LEAVES: "leaves_birch",
    TALLGRASS: "tallgrass",
    ANDESITE: "stone_andesite",
    GRAVEL: "gravel",
    COARSE_DIRT: "coarse_dirt",
    SANDSTONE: ("sandstone_top", "sandstone_bottom", "sandstone_normal", "sandstone_normal", "sandstone_normal", "sandstone_normal"),
    COBBLESTONE: "cobblestone",
    COBBLESTONE_MOSSY: "cobblestone_mossy",
    OAK_PLANKS: "planks_oak",
    SPRUCE_PLANKS: "planks_spruce",
    BIRCH_PLANKS: "planks_birch",
    JUNGLE_PLANKS: "planks_jungle",
    ACACIA_PLANKS: "planks_acacia",
    DARK_OAK_PLANKS: "planks_big_oak",
    GLASS: "glass",
    COAL_ORE: "coal_ore",
    IRON_ORE: "iron_ore",
    GOLD_ORE: "gold_ore",
    DIAMOND_ORE: "diamond_ore",
    EMERALD_ORE: "emerald_ore",
    REDSTONE_ORE: "redstone_ore",
    LAPIS_ORE: "lapis_ore",
    COAL_BLOCK: "coal_block",
    IRON_BLOCK: "iron_block",
    GOLD_BLOCK: "gold_block",
    DIAMOND_BLOCK: "diamond_block",
    EMERALD_BLOCK: "emerald_block",
    REDSTONE_BLOCK: "redstone_block",
    LAPIS_BLOCK: "lapis_block",
    BRICK: "brick",
    STONEBRICK: "stonebrick",
    STONEBRICK_MOSSY: "stonebrick_mossy",
    STONEBRICK_CRACKED: "stonebrick_cracked",
    STONEBRICK_CARVED: "stonebrick_carved",
    NETHER_BRICK: "nether_brick",
    OBSIDIAN: "obsidian",
    GLOWSTONE: "glowstone",
    CLAY: "clay",
    SNOW: "snow",
    SNOW_BLOCK: "snow",
    ICE: "ice",
    ICE_PACKED: "ice_packed",
    NETHERRACK: "netherrack",
    SOUL_SAND: "soul_sand",
    END_STONE: "end_stone",
    PRISMARINE: "prismarine_rough",
    PRISMARINE_BRICKS: "prismarine_bricks",
    PRISMARINE_DARK: "prismarine_dark",
    SEA_LANTERN: "sea_lantern",
    SPONGE: "sponge",
    SPONGE_WET: "sponge_wet",
    SLIME: "slime",
    TNT: ("tnt_top", "tnt_bottom", "tnt_side", "tnt_side", "tnt_side", "tnt_side"),
    BOOKSHELF: ("planks_oak", "planks_oak", "bookshelf", "bookshelf", "bookshelf", "bookshelf"),
    CRAFTING_TABLE: ("crafting_table_top", "planks_oak", "crafting_table_front", "crafting_table_side", "crafting_table_front", "crafting_table_side"),
    FURNACE: ("furnace_top", "furnace_top", "furnace_front_off", "furnace_side", "furnace_side", "furnace_side"),
    NOTEBLOCK: "noteblock",
    JUKEBOX: ("jukebox_top", "jukebox_side", "jukebox_side", "jukebox_side", "jukebox_side", "jukebox_side"),
    MELON: ("melon_top", "melon_top", "melon_side", "melon_side", "melon_side", "melon_side"),
    PUMPKIN: ("pumpkin_top", "pumpkin_top", "pumpkin_face_off", "pumpkin_side", "pumpkin_side", "pumpkin_side"),
    JACK_O_LANTERN: ("pumpkin_top", "pumpkin_top", "pumpkin_face_on", "pumpkin_side", "pumpkin_side", "pumpkin_side"),
    HAY_BLOCK: ("hay_block_top", "hay_block_top", "hay_block_side", "hay_block_side", "hay_block_side", "hay_block_side"),
    CACTUS: ("cactus_top", "cactus_bottom", "cactus_side", "cactus_side", "cactus_side", "cactus_side"),
    SPRUCE_LOG: ("log_spruce_top", "log_spruce_top", "log_spruce", "log_spruce", "log_spruce", "log_spruce"),
    BIRCH_LOG: ("log_birch_top", "log_birch_top", "log_birch", "log_birch", "log_birch", "log_birch"),
    JUNGLE_LOG: ("log_jungle_top", "log_jungle_top", "log_jungle", "log_jungle", "log_jungle", "log_jungle"),
    ACACIA_LOG: ("log_acacia_top", "log_acacia_top", "log_acacia", "log_acacia", "log_acacia", "log_acacia"),
    DARK_OAK_LOG: ("log_big_oak_top", "log_big_oak_top", "log_big_oak", "log_big_oak", "log_big_oak", "log_big_oak"),
    SPRUCE_LEAVES: "leaves_spruce",
    JUNGLE_LEAVES: "leaves_jungle",
    ACACIA_LEAVES: "leaves_acacia",
    DARK_OAK_LEAVES: "leaves_big_oak",
    QUARTZ_BLOCK: ("quartz_block_top", "quartz_block_bottom", "quartz_block_side", "quartz_block_side", "quartz_block_side", "quartz_block_side"),
    QUARTZ_CHISELED: ("quartz_block_chiseled_top", "quartz_block_chiseled_top", "quartz_block_chiseled", "quartz_block_chiseled", "quartz_block_chiseled", "quartz_block_chiseled"),
    QUARTZ_PILLAR: ("quartz_block_lines_top", "quartz_block_lines_top", "quartz_block_lines", "quartz_block_lines", "quartz_block_lines", "quartz_block_lines"),
    SANDSTONE_CARVED: ("sandstone_top", "sandstone_bottom", "sandstone_carved", "sandstone_carved", "sandstone_carved", "sandstone_carved"),
    SANDSTONE_SMOOTH: ("sandstone_top", "sandstone_bottom", "sandstone_smooth", "sandstone_smooth", "sandstone_smooth", "sandstone_smooth"),
    RED_SAND: "red_sand",
    RED_SANDSTONE: ("red_sandstone_top", "red_sandstone_bottom", "red_sandstone_normal", "red_sandstone_normal", "red_sandstone_normal", "red_sandstone_normal"),
    RED_SANDSTONE_CARVED: ("red_sandstone_top", "red_sandstone_bottom", "red_sandstone_carved", "red_sandstone_carved", "red_sandstone_carved", "red_sandstone_carved"),
    RED_SANDSTONE_SMOOTH: ("red_sandstone_top", "red_sandstone_bottom", "red_sandstone_smooth", "red_sandstone_smooth", "red_sandstone_smooth", "red_sandstone_smooth"),
    HARDENED_CLAY: "hardened_clay",
    MYCELIUM: ("mycelium_top", "dirt", "mycelium_side", "mycelium_side", "mycelium_side", "mycelium_side"),
    PODZOL: ("dirt_podzol_top", "dirt", "dirt_podzol_side", "dirt_podzol_side", "dirt_podzol_side", "dirt_podzol_side"),
    REDSTONE_LAMP: "redstone_lamp_off",
    REDSTONE_LAMP_ON: "redstone_lamp_on",
    MOB_SPAWNER: "mob_spawner",
    COMMAND_BLOCK: "command_block",
    DRAGON_EGG: "dragon_egg",
    BEACON: "beacon",
    DIORITE: "stone_diorite",
    DIORITE_SMOOTH: "stone_diorite_smooth",
    GRANITE: "stone_granite",
    GRANITE_SMOOTH: "stone_granite_smooth",
    ANDESITE_SMOOTH: "stone_andesite_smooth",
    
    
    WOOL_WHITE: "wool_colored_white",
    WOOL_ORANGE: "wool_colored_orange",
    WOOL_MAGENTA: "wool_colored_magenta",
    WOOL_LIGHT_BLUE: "wool_colored_light_blue",
    WOOL_YELLOW: "wool_colored_yellow",
    WOOL_LIME: "wool_colored_lime",
    WOOL_PINK: "wool_colored_pink",
    WOOL_GRAY: "wool_colored_gray",
    WOOL_SILVER: "wool_colored_silver",
    WOOL_CYAN: "wool_colored_cyan",
    WOOL_PURPLE: "wool_colored_purple",
    WOOL_BLUE: "wool_colored_blue",
    WOOL_BROWN: "wool_colored_brown",
    WOOL_GREEN: "wool_colored_green",
    WOOL_RED: "wool_colored_red",
    WOOL_BLACK: "wool_colored_black",
    
    
    GLASS_WHITE: "glass_white",
    GLASS_ORANGE: "glass_orange",
    GLASS_MAGENTA: "glass_magenta",
    GLASS_LIGHT_BLUE: "glass_light_blue",
    GLASS_YELLOW: "glass_yellow",
    GLASS_LIME: "glass_lime",
    GLASS_PINK: "glass_pink",
    GLASS_GRAY: "glass_gray",
    GLASS_SILVER: "glass_silver",
    GLASS_CYAN: "glass_cyan",
    GLASS_PURPLE: "glass_purple",
    GLASS_BLUE: "glass_blue",
    GLASS_BROWN: "glass_brown",
    GLASS_GREEN: "glass_green",
    GLASS_RED: "glass_red",
    GLASS_BLACK: "glass_black",
    
    
    CLAY_WHITE: "hardened_clay_stained_white",
    CLAY_ORANGE: "hardened_clay_stained_orange",
    CLAY_MAGENTA: "hardened_clay_stained_magenta",
    CLAY_LIGHT_BLUE: "hardened_clay_stained_light_blue",
    CLAY_YELLOW: "hardened_clay_stained_yellow",
    CLAY_LIME: "hardened_clay_stained_lime",
    CLAY_PINK: "hardened_clay_stained_pink",
    CLAY_GRAY: "hardened_clay_stained_gray",
    CLAY_SILVER: "hardened_clay_stained_silver",
    CLAY_CYAN: "hardened_clay_stained_cyan",
    CLAY_PURPLE: "hardened_clay_stained_purple",
    CLAY_BLUE: "hardened_clay_stained_blue",
    CLAY_BROWN: "hardened_clay_stained_brown",
    CLAY_GREEN: "hardened_clay_stained_green",
    CLAY_RED: "hardened_clay_stained_red",
    CLAY_BLACK: "hardened_clay_stained_black",
    
    
    LAVA: "lava_still",
    LAVA_FLOWING: "lava_flow",
    WATER: "water_still",
    WATER_FLOWING: "water_flow",
    FIRE: "fire_layer_0",
    FURNACE_ON: ("furnace_top", "furnace_top", "furnace_front_on", "furnace_side", "furnace_side", "furnace_side"),
    
    # custom geometry

    BARRIER: "glass",  # inv only
    HOPPER: ("hopper_top", "hopper_inside", "hopper_outside", "hopper_outside", "hopper_outside", "hopper_outside"),
    CAULDRON: ("cauldron_top", "cauldron_bottom", "cauldron_side", "cauldron_side", "cauldron_side", "cauldron_side"),
    CAKE: ("cake_top", "cake_bottom", "cake_side", "cake_side", "cake_side", "cake_side"),
    REPEATER: "repeater_off",
    COMPARATOR: "comparator_off",
    OAK_DOOR_BOTTOM: "door_wood_lower",
    OAK_DOOR_TOP: "door_wood_upper",
    IRON_DOOR_BOTTOM: "door_iron_lower",
    IRON_DOOR_TOP: "door_iron_upper",
    REDSTONE_WIRE: "redstone_dust_dot",
    ITEM_FRAME_BLOCK: "item_frame",
    BREWING_STAND_BLOCK: "brewing_stand_base",
    BED_HEAD: ("bed_head_top", "planks_oak", "bed_head_end", "bed_head_side", "bed_head_side", "bed_head_side"),
    BED_FOOT: ("bed_feet_top", "planks_oak", "bed_feet_end", "bed_feet_side", "bed_feet_side", "bed_feet_side"),
    SIGN_STANDING: "planks_oak",


    SAPLING_OAK: "sapling_oak",
    SAPLING_SPRUCE: "sapling_spruce",
    SAPLING_BIRCH: "sapling_birch",
    SAPLING_JUNGLE: "sapling_jungle",
    SAPLING_ACACIA: "sapling_acacia",
    SAPLING_DARK_OAK: "sapling_roofed_oak",
    
    
    DANDELION: "flower_dandelion",
    POPPY: "flower_rose",
    BLUE_ORCHID: "flower_blue_orchid",
    ALLIUM: "flower_allium",
    AZURE_BLUET: "flower_houstonia",
    RED_TULIP: "flower_tulip_red",
    ORANGE_TULIP: "flower_tulip_orange",
    WHITE_TULIP: "flower_tulip_white",
    PINK_TULIP: "flower_tulip_pink",
    OXEYE_DAISY: "flower_oxeye_daisy",
    BROWN_MUSHROOM: "mushroom_brown",
    RED_MUSHROOM: "mushroom_red",
    DEAD_BUSH: "deadbush",
    FERN: "fern",
    
    
    SUNFLOWER: "double_plant_sunflower_bottom",
    LILAC: "double_plant_syringa_bottom",
    DOUBLE_TALLGRASS: "double_plant_grass_bottom",
    LARGE_FERN: "double_plant_fern_bottom",
    ROSE_BUSH: "double_plant_rose_bottom",
    PEONY: "double_plant_paeonia_bottom",
    
    
    RAIL: "rail_normal",
    POWERED_RAIL: "rail_golden",
    POWERED_RAIL_ON: "rail_golden_powered",
    DETECTOR_RAIL: "rail_detector",
    ACTIVATOR_RAIL: "rail_activator",
    
    
    TORCH: "torch_on",
    REDSTONE_TORCH_OFF: "redstone_torch_off",
    REDSTONE_TORCH_ON: "redstone_torch_on",
    
    
    OAK_STAIRS: "planks_oak",
    SPRUCE_STAIRS: "planks_spruce",
    BIRCH_STAIRS: "planks_birch",
    JUNGLE_STAIRS: "planks_jungle",
    ACACIA_STAIRS: "planks_acacia",
    DARK_OAK_STAIRS: "planks_big_oak",
    STONE_STAIRS: "stone",
    COBBLESTONE_STAIRS: "cobblestone",
    BRICK_STAIRS: "brick",
    STONE_BRICK_STAIRS: "stonebrick",
    NETHER_BRICK_STAIRS: "nether_brick",
    SANDSTONE_STAIRS: ("sandstone_top", "sandstone_bottom", "sandstone_normal", "sandstone_normal", "sandstone_normal", "sandstone_normal"),
    QUARTZ_STAIRS: ("quartz_block_top", "quartz_block_bottom", "quartz_block_side", "quartz_block_side", "quartz_block_side", "quartz_block_side"),
    RED_SANDSTONE_STAIRS: ("red_sandstone_top", "red_sandstone_bottom", "red_sandstone_normal", "red_sandstone_normal", "red_sandstone_normal", "red_sandstone_normal"),
    
    
    STONE_SLAB: ("stone_slab_top", "stone_slab_top", "stone_slab_side", "stone_slab_side", "stone_slab_side", "stone_slab_side"),
    SANDSTONE_SLAB: ("sandstone_top", "sandstone_bottom", "sandstone_normal", "sandstone_normal", "sandstone_normal", "sandstone_normal"),
    COBBLESTONE_SLAB: "cobblestone",
    BRICK_SLAB: "brick",
    STONE_BRICK_SLAB: "stonebrick",
    NETHER_BRICK_SLAB: "nether_brick",
    QUARTZ_SLAB: ("quartz_block_top", "quartz_block_bottom", "quartz_block_side", "quartz_block_side", "quartz_block_side", "quartz_block_side"),
    OAK_SLAB: "planks_oak",
    SPRUCE_SLAB: "planks_spruce",
    BIRCH_SLAB: "planks_birch",
    JUNGLE_SLAB: "planks_jungle",
    ACACIA_SLAB: "planks_acacia",
    DARK_OAK_SLAB: "planks_big_oak",
    RED_SANDSTONE_SLAB: ("red_sandstone_top", "red_sandstone_bottom", "red_sandstone_normal", "red_sandstone_normal", "red_sandstone_normal", "red_sandstone_normal"),
    
    
    OAK_FENCE: "planks_oak",
    SPRUCE_FENCE: "planks_spruce",
    BIRCH_FENCE: "planks_birch",
    JUNGLE_FENCE: "planks_jungle",
    ACACIA_FENCE: "planks_acacia",
    DARK_OAK_FENCE: "planks_big_oak",
    NETHER_BRICK_FENCE: "nether_brick",
    
    
    OAK_FENCE_GATE: "planks_oak",
    SPRUCE_FENCE_GATE: "planks_spruce",
    BIRCH_FENCE_GATE: "planks_birch",
    JUNGLE_FENCE_GATE: "planks_jungle",
    ACACIA_FENCE_GATE: "planks_acacia",
    DARK_OAK_FENCE_GATE: "planks_big_oak",
    
    
    COBBLESTONE_WALL: "cobblestone",
    MOSSY_COBBLESTONE_WALL: "cobblestone_mossy",
    
    
    SPRUCE_DOOR_BOTTOM: "door_spruce_lower",
    SPRUCE_DOOR_TOP: "door_spruce_upper",
    BIRCH_DOOR_BOTTOM: "door_birch_lower",
    BIRCH_DOOR_TOP: "door_birch_upper",
    JUNGLE_DOOR_BOTTOM: "door_jungle_lower",
    JUNGLE_DOOR_TOP: "door_jungle_upper",
    ACACIA_DOOR_BOTTOM: "door_acacia_lower",
    ACACIA_DOOR_TOP: "door_acacia_upper",
    DARK_OAK_DOOR_BOTTOM: "door_dark_oak_lower",
    DARK_OAK_DOOR_TOP: "door_dark_oak_upper",
    
    
    STONE_BUTTON: "stone",
    WOODEN_BUTTON: "planks_oak",
    
    
    STONE_PRESSURE_PLATE: "stone",
    WOODEN_PRESSURE_PLATE: "planks_oak",
    LIGHT_WEIGHTED_PRESSURE_PLATE: "gold_block",
    HEAVY_WEIGHTED_PRESSURE_PLATE: "iron_block",
    
    
    OAK_TRAPDOOR: "trapdoor",
    IRON_TRAPDOOR: "iron_trapdoor",
    LADDER: "ladder",
    
    
    PISTON: ("piston_top_normal", "piston_bottom", "piston_side", "piston_side", "piston_side", "piston_side"),
    STICKY_PISTON: ("piston_top_sticky", "piston_bottom", "piston_side", "piston_side", "piston_side", "piston_side"),
    PISTON_HEAD: "piston_top_normal",
    
    
    DISPENSER: ("furnace_top", "furnace_top", "dispenser_front_horizontal", "furnace_side", "furnace_side", "furnace_side"),
    DROPPER: ("furnace_top", "furnace_top", "dropper_front_horizontal", "furnace_side", "furnace_side", "furnace_side"),
    
    
    CHEST: "planks_oak",
    TRAPPED_CHEST: "planks_oak",
    ENDER_CHEST: "obsidian",
    
    
    COBWEB: "web",
    LEVER: "lever",
    TRIPWIRE_HOOK: "trip_wire_source",
    DAYLIGHT_DETECTOR: ("daylight_detector_top", "planks_oak", "daylight_detector_side", "daylight_detector_side", "daylight_detector_side", "daylight_detector_side"),
    DAYLIGHT_DETECTOR_INVERTED: ("daylight_detector_inverted_top", "planks_oak", "daylight_detector_side", "daylight_detector_side", "daylight_detector_side", "daylight_detector_side"),
    
    
    BROWN_MUSHROOM_BLOCK: "mushroom_block_skin_brown",
    RED_MUSHROOM_BLOCK: "mushroom_block_skin_red",
    
    
    IRON_BARS: "iron_bars",
    GLASS_PANE: ("glass_pane_top", "glass", "glass", "glass", "glass", "glass"),

    VINE: "vine",
    LILY_PAD: "waterlily",
    
    
    WHEAT_STAGE_7: "wheat_stage_7",
    CARROTS_STAGE_3: "carrots_stage_3",
    POTATOES_STAGE_3: "potatoes_stage_3",
    NETHER_WART_STAGE_2: "nether_wart_stage_2",
    
    
    ENCHANTING_TABLE: ("enchanting_table_top", "enchanting_table_bottom", "enchanting_table_side", "enchanting_table_side", "enchanting_table_side", "enchanting_table_side"),
    
    ANVIL: ("anvil_top_damaged_0", "anvil_base", "anvil_base", "anvil_base", "anvil_base", "anvil_base"),
    ANVIL_SLIGHTLY_DAMAGED: ("anvil_top_damaged_1", "anvil_base", "anvil_base", "anvil_base", "anvil_base", "anvil_base"),
    ANVIL_VERY_DAMAGED: ("anvil_top_damaged_2", "anvil_base", "anvil_base", "anvil_base", "anvil_base", "anvil_base"),
    
    
    END_PORTAL_FRAME: ("endframe_top", "end_stone", "endframe_side", "endframe_side", "endframe_side", "endframe_side"),
    
    
    FARMLAND_DRY: ("farmland_dry", "dirt", "dirt", "dirt", "dirt", "dirt"),
    FARMLAND_WET: ("farmland_wet", "dirt", "dirt", "dirt", "dirt", "dirt"),
    
    
    MONSTER_EGG_STONE: "stone",
    MONSTER_EGG_COBBLESTONE: "cobblestone",
    MONSTER_EGG_STONEBRICK: "stonebrick",
    
    
    CARPET_WHITE: "wool_colored_white",
    CARPET_ORANGE: "wool_colored_orange",
    CARPET_MAGENTA: "wool_colored_magenta",
    CARPET_LIGHT_BLUE: "wool_colored_light_blue",
    CARPET_YELLOW: "wool_colored_yellow",
    CARPET_LIME: "wool_colored_lime",
    CARPET_PINK: "wool_colored_pink",
    CARPET_GRAY: "wool_colored_gray",
    CARPET_SILVER: "wool_colored_silver",
    CARPET_CYAN: "wool_colored_cyan",
    CARPET_PURPLE: "wool_colored_purple",
    CARPET_BLUE: "wool_colored_blue",
    CARPET_BROWN: "wool_colored_brown",
    CARPET_GREEN: "wool_colored_green",
    CARPET_RED: "wool_colored_red",
    CARPET_BLACK: "wool_colored_black",
    
    
    GLASS_PANE_WHITE: ("glass_pane_top_white", "glass_white", "glass_white", "glass_white", "glass_white", "glass_white"),
    GLASS_PANE_ORANGE: ("glass_pane_top_orange", "glass_orange", "glass_orange", "glass_orange", "glass_orange", "glass_orange"),
    GLASS_PANE_MAGENTA: ("glass_pane_top_magenta", "glass_magenta", "glass_magenta", "glass_magenta", "glass_magenta", "glass_magenta"),
    GLASS_PANE_LIGHT_BLUE: ("glass_pane_top_light_blue", "glass_light_blue", "glass_light_blue", "glass_light_blue", "glass_light_blue", "glass_light_blue"),
    GLASS_PANE_YELLOW: ("glass_pane_top_yellow", "glass_yellow", "glass_yellow", "glass_yellow", "glass_yellow", "glass_yellow"),
    GLASS_PANE_LIME: ("glass_pane_top_lime", "glass_lime", "glass_lime", "glass_lime", "glass_lime", "glass_lime"),
    GLASS_PANE_PINK: ("glass_pane_top_pink", "glass_pink", "glass_pink", "glass_pink", "glass_pink", "glass_pink"),
    GLASS_PANE_GRAY: ("glass_pane_top_gray", "glass_gray", "glass_gray", "glass_gray", "glass_gray", "glass_gray"),
    GLASS_PANE_SILVER: ("glass_pane_top_silver", "glass_silver", "glass_silver", "glass_silver", "glass_silver", "glass_silver"),
    GLASS_PANE_CYAN: ("glass_pane_top_cyan", "glass_cyan", "glass_cyan", "glass_cyan", "glass_cyan", "glass_cyan"),
    GLASS_PANE_PURPLE: ("glass_pane_top_purple", "glass_purple", "glass_purple", "glass_purple", "glass_purple", "glass_purple"),
    GLASS_PANE_BLUE: ("glass_pane_top_blue", "glass_blue", "glass_blue", "glass_blue", "glass_blue", "glass_blue"),
    GLASS_PANE_BROWN: ("glass_pane_top_brown", "glass_brown", "glass_brown", "glass_brown", "glass_brown", "glass_brown"),
    GLASS_PANE_GREEN: ("glass_pane_top_green", "glass_green", "glass_green", "glass_green", "glass_green", "glass_green"),
    GLASS_PANE_RED: ("glass_pane_top_red", "glass_red", "glass_red", "glass_red", "glass_red", "glass_red"),
    GLASS_PANE_BLACK: ("glass_pane_top_black", "glass_black", "glass_black", "glass_black", "glass_black", "glass_black"),
    
    
    SUGAR_CANE: "reeds",
    COCOA: "cocoa_stage_2",
}



def blockuvs(blockId):
    if blockId not in BLOCK_FACES:
        return ((0.0, 0.0),) * 6
    
    faces = BLOCK_FACES[blockId]
    
    if isinstance(faces, str):
        uv = getuv(faces)
        return (uv, uv, uv, uv, uv, uv)
    
    return tuple(getuv(tex) for tex in faces)


def faceuvb(blockId, face):
    uvs = blockuvs(blockId)
    return uvs[face]



TRANSP_BLOCKS = {
    AIR, WATER, GLASS, OAK_LEAVES, BIRCH_LEAVES, SPRUCE_LEAVES, 
    JUNGLE_LEAVES, ACACIA_LEAVES, DARK_OAK_LEAVES, TALLGRASS,
    GLASS_WHITE, GLASS_ORANGE, GLASS_MAGENTA, GLASS_LIGHT_BLUE,
    GLASS_YELLOW, GLASS_LIME, GLASS_PINK, GLASS_GRAY, GLASS_SILVER,
    GLASS_CYAN, GLASS_PURPLE, GLASS_BLUE, GLASS_BROWN, GLASS_GREEN,
    GLASS_RED, GLASS_BLACK, ICE, SLIME, LAVA, FIRE, WATER_FLOWING, LAVA_FLOWING
}


NONSOLID_BLOCKS = {AIR, WATER, TALLGRASS, LAVA, FIRE, WATER_FLOWING, LAVA_FLOWING}
CROSS_BLOCKS = {TALLGRASS, FIRE}


def istransp(blockId): return blockId in TRANSP_BLOCKS
def issolidb(blockId): return blockId not in NONSOLID_BLOCKS
def iscross(blockId):  return blockId in CROSS_BLOCKS


import numpy as np

# block maxid && uvarray
# array = MAX_ID, 6-faces, 2-uv lookup 
MAX_ID = 512
UV_ARRAY = np.zeros((MAX_ID, 6, 2), dtype=np.float32)

for blockId in range(MAX_ID):
    if blockId in BLOCK_FACES:
        uvs = blockuvs(blockId)
        for face in range(6):
            UV_ARRAY[blockId, face, 0] = uvs[face][0]
            UV_ARRAY[blockId, face, 1] = uvs[face][1]



FACINGNONE = 0
FACING_H = 1  # 4 hor dir 
FACING_AX = 2 # 3 axis

# state values 10-12b
FACE_N = 0   # -z
FACE_S = 1   # +z
FACE_E  = 2  # +x
FACE_W  = 3  # -x
AXY = 0       
AXX = 1
AXZ = 2

_FACINGTYPE = np.zeros(MAX_ID, dtype=np.int8)

# horiz
for _bid in (
    FURNACE, FURNACE_ON, PUMPKIN, JACK_O_LANTERN,
    CRAFTING_TABLE, DISPENSER, DROPPER,
    CHEST, TRAPPED_CHEST, ENDER_CHEST,
    REPEATER, COMPARATOR
):
    _FACINGTYPE[_bid] = FACING_H

# stairs
for _bid in (
    OAK_STAIRS, SPRUCE_STAIRS, BIRCH_STAIRS, JUNGLE_STAIRS,
    ACACIA_STAIRS, DARK_OAK_STAIRS, STONE_STAIRS, COBBLESTONE_STAIRS,
    BRICK_STAIRS, STONE_BRICK_STAIRS, NETHER_BRICK_STAIRS,
    SANDSTONE_STAIRS, QUARTZ_STAIRS, RED_SANDSTONE_STAIRS
):
    _FACINGTYPE[_bid] = FACING_H

# axis
for _bid in (
    OAK_LOG, SPRUCE_LOG, BIRCH_LOG, JUNGLE_LOG, ACACIA_LOG, DARK_OAK_LOG,
    QUARTZ_PILLAR, HAY_BLOCK
):
    _FACINGTYPE[_bid] = FACING_AX

# [facing_val, geom_face] -> uv_face
HOR_UV_REMAP = np.array([
    [0, 1, 2, 3, 4, 5],  # n
    [0, 1, 3, 2, 5, 4],  # s
    [0, 1, 5, 4, 2, 3],  # e
    [0, 1, 4, 5, 3, 2],  # w
], dtype=np.int32)

AXIS_UV_REMAP = np.array([
    [0, 1, 2, 3, 4, 5],  # y
    [4, 5, 2, 3, 0, 1],  # x ends @ e w, else bark
    [2, 3, 0, 1, 4, 5],  # z ends @ n s, else bark
], dtype=np.int32)

# [axis, geom_face] -> rotation
AXIS_UV_ROT = np.array([
    [0, 0, 0, 0, 0, 0],  # y no rot
    [1, 1, 1, 1, 0, 0],  # x top bot n s -> 90; e w -> ends
    [0, 0, 0, 0, 1, 1],  # z e w -> 90; n s -> ends
], dtype=np.int32)
