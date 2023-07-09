import json
import os
import random

import minecraft_data

import const
import make


class Main:
    def __init__(self, version):
        self.version = version
        self.mcdata = minecraft_data(version)
        self.make = make.Make(self.mcdata)

        if os.path.exists("custom_stats.json"):
            with open("custom_stats.json", "r") as f:
                self.custom_stats = json.loads(f.read())
        else:
            self.custom_stats = None

        self.make_mined = self.make.create_make_function(const.mined_blacklist + const.default_blacklist)
        self.make_crafted = self.make.create_make_function(const.craftable_blacklist + const.default_blacklist, has_recipe=True)
        self.make_broken = self.make.create_make_function(None, whitelist=const.breakable_items)
        self.make_dropped = self.make.create_make_function(const.dropped_blacklist + const.netherite + const.diamond + const.iron + const.gold + const.chainmail + const.leather + const.wooden + const.stone)
        self.make_picked_up = self.make.create_make_function(const.picked_up_blacklist + const.default_blacklist)
        self.make_killed = self.make.create_make_function(const.killed_blacklist + const.default_blacklist)
        self.make_killed_by = self.make.create_make_function(const.killed_by_blacklist + const.default_blacklist)
        self.make_custom = self.make.create_make_function(const.custom_blacklist + const.default_blacklist)


def print_hi():
    main = Main("1.20.1")

    mined = main.make_mined(main.mcdata.blocks, 'm', "minecraft.mined", "%s Mined")
    crafted = main.make_crafted(main.mcdata.items, "c", "minecraft.crafted", "%s Crafted")
    broken = main.make_broken(main.mcdata.items, "b", "minecraft.broken", "%s Broken")
    dropped = main.make_dropped(main.mcdata.items, "d", "minecraft.dropped", "%s Dropped")
    picked_up = main.make_picked_up(main.mcdata.items, "p", "minecraft.picked_up", "%s Picked up")
    killed = main.make_killed(main.mcdata.entities_name, "k", "minecraft.killed", "%s Killed")
    killed_by = main.make_killed_by(main.mcdata.entities_name, "kb", "minecraft.killed_by", "Killed by %s")
    custom = main.make_custom(main.custom_stats, "z", "minecraft.custom", "%s")

    with open("stats.list", "a") as stats_list:
        _tmp = []
        for stat in (mined, crafted, broken, dropped, picked_up, killed, killed_by, custom):
            _tmp += [item + "\n" for item in stat["criteria"].values()]
        stats_list.writelines(_tmp)


if __name__ == '__main__':
    print_hi()
