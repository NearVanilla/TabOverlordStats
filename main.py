import json
import minecraft_data


class Main:
    def __init__(self, version):
        self.version = version
        self.mcdata = minecraft_data(version)
        self.breakable_items = ["shield", "shears", "fishing_rod", "carrot_on_a_stick", "flint_and_steel", "bow",
                                "crossbow" "trident", "elytra", "warped_fungus_on_a_stick", "brush", "turtle_helmet",
                                "leather_helmet", "leather_chestplate", "leather_leggings", "leather_boots",
                                "chainmail_helmet", "chainmail_chestplate", "chainmail_leggings", "chainmail_boots",
                                "iron_helmet", "iron_chestplate", "iron_leggings", "iron_boots",
                                "diamond_helmet", "diamond_chestplate", "diamond_leggings", "diamond_boots",
                                "golden_helmet", "golden_chestplate", "golden_leggings", "golden_boots",
                                "netherite_helmet", "netherite_chestplate", "netherite_leggings", "netherite_boots",
                                "wooden_axe", "stone_axe", "iron_axe", "diamond_axe", "golden_axe", "netherite_axe",
                                "wooden_sword", "stone_sword", "iron_sword", "diamond_sword", "golden_sword",
                                "netherite_sword",
                                "wooden_pickaxe", "stone_pickaxe", "iron_pickaxe", "diamond_pickaxe", "golden_pickaxe",
                                "netherite_pickaxe",
                                "wooden_shovel", "stone_shovel", "iron_shovel", "diamond_shovel", "golden_shovel",
                                "netherite_shovel",
                                "wooden_hoe", "stone_hoe", "iron_hoe", "diamond_hoe", "golden_hoe", "netherite_hoe"
                                ]

        self.creative_only_items = ["command_block", "chain_command_block", "repeating_command_block",
                                    "command_block_minecart", "jigsaw", "structure_block", "structure_void", "barrier",
                                    "debug_stick", "light", "spawner"
                                    ]

        self.unbreakable_items = ["bedrock", "end_portal_frame", "reinforced_deepslate", "end_gateway", "void_air",
                                  "cave_air", "bubble_column", "water", "lava", "end_portal", "attached_pumpkin_stem",
                                  "attached_melon_stem", "air"
                                  ]

        self.spawn_eggs = [spawn_egg.get("name") for spawn_egg in self.mcdata.get_data.get("items") if
                           "spawn_egg" in spawn_egg.get("name")]

        self.mined_blacklist = ["piston_head", "spawner", "infested_stone", "infested_cobblestone",
                                "infested_stone_bricks", "infested_mossy_stone_bricks",
                                "infested_cracked_stone_bricks", "infested_chiseled_stone_bricks",
                                "infested_deepslate", "water_cauldron", "lava_cauldron",
                                "powder_snow_cauldron",
                                "budding_amethyst", "netherite_block", "respawn_anchor", "lodestone"
                                ]

        self.default_blacklist = self.unbreakable_items + self.creative_only_items + \
                                 ["frogspawn", "candle_cake", "black_candle_cake", "red_candle_cake",
                                  "green_candle_cake", "brown_candle_cake", "blue_candle_cake", "purple_candle_cake",
                                  "cyan_candle_cake", "light_gray_candle_cake", "gray_candle_cake", "pink_candle_cake",
                                  "lime_candle_cake", "yellow_candle_cake", "light_blue_candle_cake",
                                  "magenta_candle_cake", "orange_candle_cake", "white_candle_cake"
                                  ]

        self.craftable_blacklist = ["netherite_block", "respawn_anchor", "lodestone", "dragon_egg",
                                    "netherite_upgrade_smithing_template", "sentry_armor_trim_smithing_template",
                                    "dune_armor_trim_smithing_template", "coast_armor_trim_smithing_template",
                                    "wild_armor_trim_smithing_template", "ward_armor_trim_smithing_template",
                                    "eye_armor_trim_smithing_template", "vex_armor_trim_smithing_template",
                                    "tide_armor_trim_smithing_template", "snout_armor_trim_smithing_template",
                                    "rib_armor_trim_smithing_template", "spire_armor_trim_smithing_template",
                                    "wayfinder_armor_trim_smithing_template", "shaper_armor_trim_smithing_template",
                                    "silence_armor_trim_smithing_template", "raiser_armor_trim_smithing_template",
                                    "host_armor_trim_smithing_template", "netherite_ingot"
                                    ]

    def is_unbreakable(self, item):
        return True if item.get("name") in self.unbreakable_items else False

    def is_creative_only(self, item):
        return True if item.get("name") in self.creative_only_items else False

    def has_crafting_recipe(self, item):
        try:
            item_id = item.get("name")
            recipe = self.mcdata.recipes[0]["recipes"][item_id]
            return recipe
        except KeyError:
            return None

    def make_mined(self, registry, prefix, criterion_namespace, lang):
        blacklisted = self.creative_only_items + self.unbreakable_items + self.mined_blacklist + self.default_blacklist
        dictionary = {}
        criteria = {}
        display_names = {}
        for index in registry:
            if registry[index]["name"] not in blacklisted:
                name = prefix + "-" + registry[index]["name"]
                dictionary[name] = name
                criteria[name] = criterion_namespace + ":" + "minecraft." + registry[index]["name"]
                display_names[name] = lang % registry[index]["displayName"]

        return {
            "dictionary": dictionary,
            "criteria": criteria,
            "display_names": display_names
        }

    def make_crafted(self, registry, prefix, criterion_namespace, lang):
        blacklisted = self.creative_only_items + self.unbreakable_items + self.craftable_blacklist
        dictionary = {}
        criteria = {}
        display_names = {}
        for index in registry:
            if registry[index]["name"] not in blacklisted and self.has_crafting_recipe(registry[index]):
                name = prefix + "-" + registry[index]["name"]
                dictionary[name] = name
                criteria[name] = criterion_namespace + ":" + "minecraft." + registry[index]["name"]
                display_names[name] = lang % registry[index]["displayName"]

        return {
            "dictionary": dictionary,
            "criteria": criteria,
            "display_names": display_names
        }

    def make_broken(self, registry, prefix, criterion_namespace, lang):
        whitelisted = self.breakable_items
        dictionary = {}
        criteria = {}
        display_names = {}
        for index in registry:
            if registry[index]["name"] in whitelisted:
                name = prefix + "-" + registry[index]["name"]
                dictionary[name] = name
                criteria[name] = criterion_namespace + ":" + "minecraft." + registry[index]["name"]
                display_names[name] = lang % registry[index]["displayName"]

        return {
            "dictionary": dictionary,
            "criteria": criteria,
            "display_names": display_names
        }

    def make_dropped(self, registry, prefix, criterion_namespace, lang):
        return None

    def make_picked_up(self, registry, prefix, criterion_namespace, lang):
        return None

    def make_killed(self, registry, prefix, criterion_namespace, lang):
        return None

    def make_killed_by(self, registry, prefix, criterion_namespace, lang):
        return None

    def make_custom(self, registry, prefix, criterion_namespace, lang):
        return None


def print_hi():
    main = Main("1.20.1")

    # print(main.has_crafting_recipe("1122"))
    # print(main.is_unbreakable(main.mcdata.find_item_or_block("stone")))
    # print(main.mcdata.find_item_or_block("music_disc_13"))
    # print(main.mcdata.recipes['1136'])

    # for item in main.mcdata.get_data.get('items'):
    #     if not main.is_unbreakable(item) and not main.is_creative_only(item):
    #         print({"item": item.get("name"),
    #                "Is Unbreakable": main.is_unbreakable(item),
    #                "Is Creative Only": main.is_creative_only(item),
    #                "Has Crafting Recipe": main.has_crafting_recipe(str(item.get("id")))})

    # for block in main.mcdata.get_data.get("blocks"):
    #     if main.has_crafting_recipe(block) and block.get("name") not in main.craftable_blocks_blacklist:
    #         main.craftable_blocks.append(main.has_crafting_recipe(block)[0]["id"])
    #     material = block.get("material")
    #     material_name = block.get("name")
    #     match material:
    #         case "mineable/pickaxe":
    #             main.mineable_pickaxe.append(block) if material_name not in main.mineable_pickaxe_blacklist else None
    #         case "mineable/axe":
    #             main.mineable_axe.append(block) if material_name not in main.mineable_axe_blacklist else None
    #         case "mineable/shovel":
    #             main.mineable_shovel.append(block) if material_name not in main.mineable_shovel_blacklist else None
    #         case "mineable/hoe":
    #             main.mineable_hoe.append(block) if material_name not in main.mineable_hoe_blacklist else None
    #         case "plant":
    #             main.plant.append(block) if material_name not in main.plant_blacklist else None
    #         case _:
    #             main.default.append(block) if material_name not in main.default_blacklist else None
    #
    # mined_array = ["minecraft.mined:minecraft." + block.get("name") for array in
    #                (main.mineable_pickaxe, main.mineable_axe, main.mineable_shovel, main.mineable_hoe, main.plant, main.default) for block in array]
    #
    # craftable_array = ["minecraft.crafted:minecraft." + block for block in main.craftable_blocks]
    #
    # print(craftable_array)

    mined = main.make_mined(main.mcdata.blocks, 'm', "minecraft.mined", "%s Mined")
    crafted = main.make_crafted(main.mcdata.items, "c", "minecraft.crafted", "%s Crafted")
    broken = main.make_broken(main.mcdata.items, "b", "minecraft.broken", "%s Broken")
    dropped = main.make_dropped(main.mcdata.items, "d", "minecraft.dropped", "%s Dropped")
    picked_up = main.make_picked_up(main.mcdata.items, "p", "minecraft.picked_up", "%s Picked up")
    killed = main.make_killed(main.mcdata.entities_name, "k", "minecraft.killed", "%s Killed")
    killed_by = main.make_killed_by(main.mcdata.entities_name, "kb", "minecraft.killed_by", "Killed by %s")
    # custom = main.make_custom(custom_stats, "z", "minecraft.custom", "%s")

    print(json.dumps(broken["criteria"], indent=2))


if __name__ == '__main__':
    print_hi()
