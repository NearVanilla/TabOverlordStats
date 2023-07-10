import os
import subprocess
from pathlib import Path

import blacklists
import make
from minecraft_data import minecraft_data


def extract(version):
    if not os.path.exists(f"{version}.json"):
        print(f"Extracting data for version {version}")
        subprocess.run(["python", Path.joinpath(Path.cwd().joinpath("Burger/munch.py")), "--download", version, "--toppings", "blocks,entities,items,recipes", "-o", f"{version}.json"])
        os.remove(Path(os.getcwd(), f"{version}.jar"))
        print_hi()


class Main:
    def __init__(self, version):
        self.version = version
        with open(f"{version}.json", "r") as version_file:
            self.mcdata = minecraft_data.from_json(version_file.read())

        self.make = make.Make(self.mcdata)
        self.custom_stats = self.mcdata.language["stat"]

        self.make_mined = self.make.create_make_function(blacklists.mined_blacklist + blacklists.default_blacklist)
        self.make_crafted = self.make.create_make_function(blacklists.craftable_blacklist + blacklists.default_blacklist, has_recipe=True)
        self.make_broken = self.make.create_make_function(None, whitelist=blacklists.breakable_items)
        self.make_dropped = self.make.create_make_function(blacklists.dropped_blacklist + blacklists.netherite + blacklists.diamond + blacklists.iron + blacklists.gold + blacklists.chainmail + blacklists.leather + blacklists.wooden + blacklists.stone)
        self.make_picked_up = self.make.create_make_function(blacklists.picked_up_blacklist + blacklists.default_blacklist)
        self.make_killed = self.make.create_make_function(None, is_entity=True, whitelist=blacklists.killed_whitelist)
        self.make_killed_by = self.make.create_make_function(None, is_entity=True, whitelist=blacklists.killed_by_whitelist)
        self.make_custom = self.make.create_make_function(blacklists.custom_blacklist + blacklists.default_blacklist, is_custom=True)


def print_hi():
    version = "1.20.1"

    if not Path.exists(Path.joinpath(Path.cwd(), f"{version}.json")):
        extract(version)
    else:
        main = Main(version)

        mined = main.make_mined(main.mcdata.blocks["block"], 'm', "minecraft.mined", "%s Mined")
        crafted = main.make_crafted(main.mcdata.items["item"], "c", "minecraft.crafted", "%s Crafted")
        broken = main.make_broken(main.mcdata.items["item"], "b", "minecraft.broken", "%s Broken")
        dropped = main.make_dropped(main.mcdata.items["item"], "d", "minecraft.dropped", "%s Dropped")
        picked_up = main.make_picked_up(main.mcdata.items["item"], "p", "minecraft.picked_up", "%s Picked up")
        killed = main.make_killed(main.mcdata.entities["entity"], "k", "minecraft.killed", "%s Killed")
        killed_by = main.make_killed_by(main.mcdata.entities["entity"], "kb", "minecraft.killed_by", "Killed by %s")
        custom = main.make_custom(main.custom_stats, "z", "minecraft.custom", "%s")

        with open("stats.list", "w") as stats_list:
            _tmp = []
            for stat in (mined, crafted, broken, dropped, picked_up, killed, killed_by, custom):
                _tmp += [item + "\n" for item in stat["criteria"].values()]
            stats_list.writelines(_tmp)


if __name__ == '__main__':
    print_hi()
