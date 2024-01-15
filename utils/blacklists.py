from typing import List


def generate_breakable_blacklist(item_type: str) -> List[str]:
    armor_type = ["helmet", "chestplate", "leggings", "boots"]
    tool_types = ["axe", "pickaxe", "shovel", "sword", "hoe"]

    types = {
        "netherite": armor_type + tool_types,
        "diamond": armor_type + tool_types,
        "iron": armor_type + tool_types,
        "golden": armor_type + tool_types,
        "leather": armor_type,
        "chainmail": armor_type,
        "wooden": tool_types,
        "stone": tool_types,
    }

    return [item_type + "_" + type for type in types[item_type]]


breakable_items = (
    generate_breakable_blacklist("netherite")
    + generate_breakable_blacklist("diamond")
    + generate_breakable_blacklist("iron")
    + generate_breakable_blacklist("golden")
    + generate_breakable_blacklist("leather")
    + generate_breakable_blacklist("chainmail")
    + generate_breakable_blacklist("wooden")
    + generate_breakable_blacklist("stone")
    + [
        "shield",
        "shears",
        "fishing_rod",
        "carrot_on_a_stick",
        "flint_and_steel",
        "bow",
        "crossbow",
        "trident",
        "elytra",
        "warped_fungus_on_a_stick",
        "brush",
        "turtle_helmet",
    ]
)


def generate_colored_blacklist(item_type: str) -> List[str]:
    colors = [
        "white",
        "light_gray",
        "gray",
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "lime",
        "green",
        "cyan",
        "light_blue",
        "blue",
        "magenta",
        "purple",
        "pink",
    ]
    return [f"{color}{item_type}" for color in colors]


wall_banners = generate_colored_blacklist("_wall_banner")
banner = generate_colored_blacklist("_banner")
shulker_boxes = generate_colored_blacklist("_shulker_box")
stained_glass = generate_colored_blacklist("_stained_glass")
stained_glass_pane = generate_colored_blacklist("_stained_glass_pane")
terracotta = generate_colored_blacklist("_terracotta")
glazed_terracotta = generate_colored_blacklist("_glazed_terracotta")
wool = generate_colored_blacklist("_wool")
dye = generate_colored_blacklist("_dye")
concrete_powder = generate_colored_blacklist("_concrete_powder")
concrete = generate_colored_blacklist("_concrete")
carpet = generate_colored_blacklist("_carpet")
candle = generate_colored_blacklist("_candle")
candle_cake = generate_colored_blacklist("_candle_cake")
bed = generate_colored_blacklist("_bed")


smithing_templates = [
    "sentry_armor_trim_smithing_template",
    "dune_armor_trim_smithing_template",
    "coast_armor_trim_smithing_template",
    "wild_armor_trim_smithing_template",
    "ward_armor_trim_smithing_template",
    "eye_armor_trim_smithing_template",
    "vex_armor_trim_smithing_template",
    "tide_armor_trim_smithing_template",
    "snout_armor_trim_smithing_template",
    "rib_armor_trim_smithing_template",
    "spire_armor_trim_smithing_template",
    "wayfinder_armor_trim_smithing_template",
    "shaper_armor_trim_smithing_template",
    "silence_armor_trim_smithing_template",
    "netherite_upgrade_smithing_template",
    "raiser_armor_trim_smithing_template",
    "host_armor_trim_smithing_template",
]

music_discs = [
    "music_disc_11",
    "music_disc_13",
    "music_disc_5",
    "music_disc_blocks",
    "music_disc_cat",
    "music_disc_chirp",
    "music_disc_far",
    "music_disc_mall",
    "music_disc_mellohi",
    "music_disc_otherside",
    "music_disc_pigstep",
    "music_disc_relic",
    "music_disc_stal",
    "music_disc_strad",
    "music_disc_wait",
    "music_disc_ward",
    "disc_fragment_5",
]

banner_patterns = [
    "piglin_banner_pattern",
    "globe_banner_pattern",
    "mojang_banner_pattern",
    "skull_banner_pattern",
    "creeper_banner_pattern",
    "flower_banner_pattern",
]

pottery_sherds = [
    "angler_pottery_sherd",
    "archer_pottery_sherd",
    "arms_up_pottery_sherd",
    "blade_pottery_sherd",
    "brewer_pottery_sherd",
    "burn_pottery_sherd",
    "danger_pottery_sherd",
    "explorer_pottery_sherd",
    "friend_pottery_sherd",
    "heart_pottery_sherd",
    "heartbreak_pottery_sherd",
    "howl_pottery_sherd",
    "miner_pottery_sherd",
    "mourner_pottery_sherd",
    "plenty_pottery_sherd",
    "prize_pottery_sherd",
    "sheaf_pottery_sherd",
    "shelter_pottery_sherd",
    "skull_pottery_sherd",
    "snort_pottery_sherd",
]

spawn_eggs = [
    "allay_spawn_egg",
    "axolotl_spawn_egg",
    "bat_spawn_egg",
    "bee_spawn_egg",
    "blaze_spawn_egg",
    "cat_spawn_egg",
    "camel_spawn_egg",
    "cave_spider_spawn_egg",
    "chicken_spawn_egg",
    "cod_spawn_egg",
    "cow_spawn_egg",
    "creeper_spawn_egg",
    "dolphin_spawn_egg",
    "donkey_spawn_egg",
    "drowned_spawn_egg",
    "elder_guardian_spawn_egg",
    "ender_dragon_spawn_egg",
    "enderman_spawn_egg",
    "endermite_spawn_egg",
    "evoker_spawn_egg",
    "fox_spawn_egg",
    "frog_spawn_egg",
    "ghast_spawn_egg",
    "glow_squid_spawn_egg",
    "goat_spawn_egg",
    "guardian_spawn_egg",
    "hoglin_spawn_egg",
    "horse_spawn_egg",
    "husk_spawn_egg",
    "iron_golem_spawn_egg",
    "llama_spawn_egg",
    "magma_cube_spawn_egg",
    "mooshroom_spawn_egg",
    "mule_spawn_egg",
    "ocelot_spawn_egg",
    "panda_spawn_egg",
    "parrot_spawn_egg",
    "phantom_spawn_egg",
    "pig_spawn_egg",
    "piglin_spawn_egg",
    "piglin_brute_spawn_egg",
    "pillager_spawn_egg",
    "polar_bear_spawn_egg",
    "pufferfish_spawn_egg",
    "rabbit_spawn_egg",
    "ravager_spawn_egg",
    "salmon_spawn_egg",
    "sheep_spawn_egg",
    "shulker_spawn_egg",
    "silverfish_spawn_egg",
    "skeleton_spawn_egg",
    "skeleton_horse_spawn_egg",
    "slime_spawn_egg",
    "sniffer_spawn_egg",
    "snow_golem_spawn_egg",
    "spider_spawn_egg",
    "squid_spawn_egg",
    "stray_spawn_egg",
    "strider_spawn_egg",
    "tadpole_spawn_egg",
    "trader_llama_spawn_egg",
    "tropical_fish_spawn_egg",
    "turtle_spawn_egg",
    "vex_spawn_egg",
    "villager_spawn_egg",
    "vindicator_spawn_egg",
    "wandering_trader_spawn_egg",
    "warden_spawn_egg",
    "witch_spawn_egg",
    "wither_spawn_egg",
    "wither_skeleton_spawn_egg",
    "wolf_spawn_egg",
    "zoglin_spawn_egg",
    "zombie_spawn_egg",
    "zombie_horse_spawn_egg",
    "zombie_villager_spawn_egg",
    "zombified_piglin_spawn_egg",
    "breeze_spawn_egg",
]

infested_blocks = [
    "infested_stone",
    "infested_cobblestone",
    "infested_stone_bricks",
    "infested_mossy_stone_bricks",
    "infested_cracked_stone_bricks",
    "infested_chiseled_stone_bricks",
    "infested_deepslate",
]

killed_by_whitelist = [
    "elder_guardian",
    "ender_dragon",
    "goat",
    "guardian",
    "husk",
    "stray",
    "zoglin",
    "bee",
    "blaze",
    "cave_spider",
    "creeper",
    "dolphin",
    "enderman",
    "endermite",
    "evoker",
    "ghast",
    "hoglin",
    "iron_golem",
    "llama",
    "magma_cube",
    "panda",
    "phantom",
    "piglin_brute",
    "piglin",
    "pillager",
    "polar_bear",
    "pufferfish",
    "ravager",
    "shulker",
    "silverfish",
    "skeleton",
    "slime",
    "spider",
    "trader_llama",
    "vex",
    "vindicator",
    "warden",
    "witch",
    "wither",
    "wither_skeleton",
    "wolf",
    "zombie",
    "zombie_villager",
    "zombified_piglin",
]

killed_whitelist = killed_by_whitelist

custom_blacklist = [
    # generalButton, itemsButton, mobsButton are included in the stats for some reason im not sure why or what they are used for?
    "generalButton",
    "itemsButton",
    "mobsButton",
    "total_world_time",
    "leave_game",
    "play_time",
]

creative_only_items = [
    "command_block",
    "chain_command_block",
    "repeating_command_block",
    "command_block_minecart",
    "jigsaw",
    "structure_block",
    "structure_void",
    "barrier",
    "debug_stick",
    "light",
    "spawner",
]

unbreakable_items = [
    "bedrock",
    "end_portal_frame",
    "reinforced_deepslate",
    "end_gateway",
    "void_air",
    "cave_air",
    "bubble_column",
    "water",
    "lava",
    "end_portal",
    "attached_pumpkin_stem",
    "attached_melon_stem",
    "air",
    "suspicious_sand",
    "suspicious_gravel",
]

mob_heads = [
    "piglin_head",
    "piglin_wall_head",
    "player_head",
    "player_wall_head",
    "skeleton_skull",
    "skeleton_wall_skull",
    "wither_skeleton_skull",
    "wither_skeleton_wall_skull",
    "zombie_head",
    "zombie_wall_head",
    "creeper_head",
    "creeper_wall_head",
]

base_blacklist = (
    unbreakable_items
    + creative_only_items
    + infested_blocks
    + mob_heads
    + spawn_eggs
    + music_discs
    + pottery_sherds
    + candle_cake
    + banner_patterns
    + smithing_templates
    + [
        "frogspawn",
        "candle_cake",
        "knowledge_book",
        "chorus_plant",
        "dragon_egg",
        "dragon_wall_head",
        "dragon_head",
        "fire",
        "frosted_ice",
        "kelp",
        "melon_stem",
        "pumpkin_stem",
        "moving_piston",
        "netherite_block",
        "netherite_ingot",
        "netherite_scrap",
        "ancient_debris",
        "nether_star",
        "petrified_oak_slab",
        "trial_key",
        "trial_spawner",
        "bundle",
        "budding_amethyst",
        "lodestone",
        "respawn_anchor",
    ]
)

mined_blacklist = base_blacklist + [
    "piston_head",
    "spawner",
    "water_cauldron",
    "lava_cauldron",
    "powder_snow_cauldron",
]


dropped_blacklist = (
    base_blacklist
    + smithing_templates
    + spawn_eggs
    + infested_blocks
    + [
        "enchanted_book",
        "wither_skeleton_skull",
        "player_head",
        "zombie_head",
        "creeper_head",
        "dragon_head",
        "piglin_head",
        "skeleton_skull",
        "enchanted_golden_apple",
        "tall_grass",
        "large_fern",
        "dragon_egg",
    ]
)

picked_up_blacklist = base_blacklist + spawn_eggs + infested_blocks + smithing_templates
