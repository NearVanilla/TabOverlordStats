import json
import minecraft_data

import const


class Main:
    def __init__(self, version):
        self.version = version
        self.mcdata = minecraft_data(version)

    def has_crafting_recipe(self, item):
        try:
            item_id = item.get("name")
            recipe = self.mcdata.recipes[0]["recipes"][item_id]
            return recipe
        except KeyError:
            return None

    def make_mined(self, registry, prefix, criterion_namespace, lang):
        blacklisted = const.creative_only_items + const.unbreakable_items + const.mined_blacklist + const.default_blacklist
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
        blacklisted = const.creative_only_items + const.unbreakable_items + const.craftable_blacklist
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
        whitelisted = const.breakable_items
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