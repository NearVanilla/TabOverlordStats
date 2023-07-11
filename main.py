import argparse
import os
import subprocess
from pathlib import Path

from utils import make, blacklists
from utils.minecraft_data import minecraft_data

parser = argparse.ArgumentParser(description="Creates a list of every score for scoreboards in minecraft minus the ones listed in utils/blacklist.py.")

subparser = parser.add_subparsers(dest="command")

to_extract = subparser.add_parser("extract", help="Extracts the required data for the requested version").add_argument('version', help="The version of minecraft you wish to use")
to_convert = subparser.add_parser("convert", help="Converts the extracted data to scores").add_argument('version', help="The version of minecraft you wish to use")
to_extract_and_convert = subparser.add_parser("both", help="Extracts the required data and then converts the scores.").add_argument('version', help="The version of minecraft you wish to use")

args = parser.parse_args()


def check_data_exists(version):
    return os.path.exists(os.path.join(os.getcwd(), "data") + f"/{version}.json")


def check_and_extract_data(version):
    if not check_data_exists(version):
        extract(version)
    else:
        return print(f"Found existing data in data/{version}.json.")


def extract(version: str):
    if not os.path.exists(os.path.join(os.getcwd(), "data")):
        os.mkdir(os.path.join(os.getcwd(), "data"))

    if not os.path.exists(f"{os.path.join(os.getcwd(), 'data')}/{version}.json"):
        print(f"Extracting data for version {version}")
        subprocess.run(["python", Path.joinpath(Path.cwd().joinpath("Burger/munch.py")), "--download", version, "--toppings", "blocks,entities,items,recipes", "-o", f"{Path.joinpath(Path.cwd(), 'data')}/{version}.json"])
        os.remove(Path(os.getcwd(), f"{version}.jar"))
        print(f"Extracted data for version {version}, saved into data/{version}.json")


class Main:
    def __init__(self, version):
        self.version = version
        with open(f"{Path.joinpath(Path.cwd(), 'data')}/{version}.json", "r") as version_file:
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


if __name__ == '__main__':
    _version = args.version
    if args.command in ("extract", "both"):
        check_and_extract_data(_version)

    if args.command in ("convert", "both"):
        if not check_data_exists(_version):
            exit(f"Required data for version {_version} not found, Please re-run with `extract` argument to extract the data.")

        main = Main(_version)

        mined = main.make_mined(main.mcdata.blocks["block"], 'm', "minecraft.mined", "%s Mined")
        crafted = main.make_crafted(main.mcdata.items["item"], "c", "minecraft.crafted", "%s Crafted")
        broken = main.make_broken(main.mcdata.items["item"], "b", "minecraft.broken", "%s Broken")
        dropped = main.make_dropped(main.mcdata.items["item"], "d", "minecraft.dropped", "%s Dropped")
        picked_up = main.make_picked_up(main.mcdata.items["item"], "p", "minecraft.picked_up", "%s Picked up")
        killed = main.make_killed(main.mcdata.entities["entity"], "k", "minecraft.killed", "%s Killed")
        killed_by = main.make_killed_by(main.mcdata.entities["entity"], "kb", "minecraft.killed_by", "Killed by %s")
        custom = main.make_custom(main.custom_stats, "z", "minecraft.custom", "%s")

        with open(os.path.join(os.getcwd(), "data/stats.list"), "w") as stats_list:
            _tmp = []
            for stat in (mined, crafted, broken, dropped, picked_up, killed, killed_by, custom):
                _tmp += [item + "\n" for item in stat["criteria"].values()]
            stats_list.writelines(_tmp)
        print("Saved scores into data/stats.list.")
