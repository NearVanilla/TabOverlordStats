netherite = ["netherite_" + item for item in ("helmet", "chestplate", "leggings", "boots", "pickaxe", "axe", "shovel", "sword", "hoe")]
diamond = ["diamond_" + item for item in ("helmet", "chestplate", "leggings", "boots", "pickaxe", "axe", "shovel", "sword", "hoe")]
iron = ["iron_" + item for item in ("helmet", "chestplate", "leggings", "boots", "pickaxe", "axe", "shovel", "sword", "hoe")]
gold = ["golden_" + item for item in ("helmet", "chestplate", "leggings", "boots", "pickaxe", "axe", "shovel", "sword", "hoe")]
leather = ["leather_" + item for item in ("helmet", "chestplate", "leggings", "boots")]
chainmail = ["chainmail_" + item for item in ("helmet", "chestplate", "leggings", "boots")]
wooden = ["wooden_" + item for item in ("pickaxe", "shovel", "axe", "sword", "hoe")]
stone = ["stone_" + item for item in ("pickaxe", "shovel", "axe", "sword", "hoe")]

wall_banners = [f"{0}_wall_banner".format(color for color in (
    "white", "light_gray", "gray", "black", "brown", "red", "orange", "yellow", "lime", "green", "cyan", "light_blue",
    "blue", "magenta", "purple", "pink"))]

breakable_items = netherite + diamond + iron + gold + leather + chainmail + wooden + stone + [
    "shield", "shears", "fishing_rod", "carrot_on_a_stick", "flint_and_steel", "bow", "crossbow", "trident", "elytra",
    "warped_fungus_on_a_stick", "brush", "turtle_helmet"
]

smithing_templates = [
    "sentry_armor_trim_smithing_template", "dune_armor_trim_smithing_template", "coast_armor_trim_smithing_template",
    "wild_armor_trim_smithing_template", "ward_armor_trim_smithing_template", "eye_armor_trim_smithing_template",
    "vex_armor_trim_smithing_template", "tide_armor_trim_smithing_template", "snout_armor_trim_smithing_template",
    "rib_armor_trim_smithing_template", "spire_armor_trim_smithing_template", "wayfinder_armor_trim_smithing_template",
    "shaper_armor_trim_smithing_template", "silence_armor_trim_smithing_template",
    "netherite_upgrade_smithing_template", "raiser_armor_trim_smithing_template", "host_armor_trim_smithing_template"
]

spawn_eggs = [
    'allay_spawn_egg', 'axolotl_spawn_egg', 'bat_spawn_egg', 'bee_spawn_egg', 'blaze_spawn_egg',
    'cat_spawn_egg', 'camel_spawn_egg', 'cave_spider_spawn_egg', 'chicken_spawn_egg', 'cod_spawn_egg',
    'cow_spawn_egg', 'creeper_spawn_egg', 'dolphin_spawn_egg', 'donkey_spawn_egg', 'drowned_spawn_egg',
    'elder_guardian_spawn_egg', 'ender_dragon_spawn_egg', 'enderman_spawn_egg', 'endermite_spawn_egg',
    'evoker_spawn_egg', 'fox_spawn_egg', 'frog_spawn_egg', 'ghast_spawn_egg', 'glow_squid_spawn_egg',
    'goat_spawn_egg', 'guardian_spawn_egg', 'hoglin_spawn_egg', 'horse_spawn_egg', 'husk_spawn_egg',
    'iron_golem_spawn_egg', 'llama_spawn_egg', 'magma_cube_spawn_egg', 'mooshroom_spawn_egg',
    'mule_spawn_egg', 'ocelot_spawn_egg', 'panda_spawn_egg', 'parrot_spawn_egg', 'phantom_spawn_egg',
    'pig_spawn_egg', 'piglin_spawn_egg', 'piglin_brute_spawn_egg', 'pillager_spawn_egg',
    'polar_bear_spawn_egg', 'pufferfish_spawn_egg', 'rabbit_spawn_egg', 'ravager_spawn_egg',
    'salmon_spawn_egg', 'sheep_spawn_egg', 'shulker_spawn_egg', 'silverfish_spawn_egg', 'skeleton_spawn_egg',
    'skeleton_horse_spawn_egg', 'slime_spawn_egg', 'sniffer_spawn_egg', 'snow_golem_spawn_egg',
    'spider_spawn_egg', 'squid_spawn_egg', 'stray_spawn_egg', 'strider_spawn_egg', 'tadpole_spawn_egg',
    'trader_llama_spawn_egg', 'tropical_fish_spawn_egg', 'turtle_spawn_egg', 'vex_spawn_egg',
    'villager_spawn_egg', 'vindicator_spawn_egg', 'wandering_trader_spawn_egg', 'warden_spawn_egg',
    'witch_spawn_egg', 'wither_spawn_egg', 'wither_skeleton_spawn_egg', 'wolf_spawn_egg', 'zoglin_spawn_egg',
    'zombie_spawn_egg', 'zombie_horse_spawn_egg', 'zombie_villager_spawn_egg', 'zombified_piglin_spawn_egg'
]

infested_blocks = [
    "infested_stone", "infested_cobblestone", "infested_stone_bricks",
    "infested_mossy_stone_bricks", "infested_cracked_stone_bricks", "infested_chiseled_stone_bricks",
    "infested_deepslate"
]

creative_only_items = [
    "command_block", "chain_command_block", "repeating_command_block",
    "command_block_minecart", "jigsaw", "structure_block", "structure_void", "barrier",
    "debug_stick", "light", "spawner"
]

unbreakable_items = [
    "bedrock", "end_portal_frame", "reinforced_deepslate", "end_gateway", "void_air", "cave_air", "bubble_column",
    "water", "lava", "end_portal", "attached_pumpkin_stem", "attached_melon_stem", "air", "suspicious_sand",
    "suspicious_gravel"
]

default_blacklist = unbreakable_items + creative_only_items + [
    "frogspawn", "candle_cake", "black_candle_cake", "red_candle_cake", "green_candle_cake",
    "brown_candle_cake", "blue_candle_cake", "purple_candle_cake", "cyan_candle_cake",
    "light_gray_candle_cake", "gray_candle_cake", "pink_candle_cake", "lime_candle_cake",
    "yellow_candle_cake", "light_blue_candle_cake", "magenta_candle_cake", "orange_candle_cake",
    "white_candle_cake", "knowledge_book", "chorus_plant"
]

mined_blacklist = unbreakable_items + [
    "piston_head", "spawner", "water_cauldron", "lava_cauldron", "powder_snow_cauldron", "budding_amethyst",
    "netherite_block", "respawn_anchor", "lodestone"
]

craftable_blacklist = smithing_templates + wall_banners + [
    "netherite_block", "respawn_anchor", "lodestone", "netherite_ingot"
]

dropped_blacklist = smithing_templates + spawn_eggs + infested_blocks + default_blacklist + [
    "piglin_banner_pattern", "globe_banner_pattern", "mojang_banner_pattern", "skull_banner_pattern",
    "creeper_banner_pattern", "flower_banner_pattern", "enchanted_book", "wither_skeleton_skull", "player_head",
    "zombie_head", "creeper_head", "dragon_head", "piglin_head", "skeleton_skull", "enchanted_golden_apple",
    "tall_grass", "large_fern", "dragon_egg"
]

picked_up_blacklist = spawn_eggs + infested_blocks + default_blacklist + smithing_templates + ["dragon_egg"]

killed_by_whitelist = [
    "elder_guardian", "ender_dragon", "goat", "guardian", "husk", "stray", "zoglin", "bee", "blaze", "cave_spider",
    "creeper", "dolphin", "enderman", "endermite", "evoker", "ghast", "hoglin", "iron_golem", "llama", "magma_cube",
    "panda", "phantom", "piglin_brute", "piglin", "pillager", "polar_bear", "pufferfish", "ravager", "shulker",
    "silverfish", "skeleton", "slime", "spider", "trader_llama", "vex", "vindicator", "warden", "witch", "wither",
    "wither_skeleton", "wolf", "zombie", "zombie_villager", "zombified_piglin"
]

killed_whitelist = killed_by_whitelist

custom_blacklist = [
    # generalButton, itemsButton, mobsButton are included in the stats for some reason im not sure why or what they are used for?
    "generalButton", "itemsButton", "mobsButton", "total_world_time", "leave_game", "play_time",
]
