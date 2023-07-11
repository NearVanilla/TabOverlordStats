import json
import os
import subprocess
from pathlib import Path


def extract(version: str):
    if not os.path.exists(os.path.join(os.getcwd(), "data")):
        os.mkdir(os.path.join(os.getcwd(), "data"))

    if not os.path.exists(f"{os.path.join(os.getcwd(), 'data')}/{version}.json"):
        print(f"Extracting data for version {version}")
        subprocess.run(["python", Path.joinpath(Path.cwd().joinpath("Burger/munch.py")), "--download", version, "--toppings", "blocks,entities,items,recipes", "-o", f"{Path.joinpath(Path.cwd(), 'data')}/{version}.json"])
        os.remove(Path(os.getcwd(), f"{version}.jar"))
        print(f"Extracted data for version {version}, saved into data/{version}.json")


class minecraft_data:
    def __init__(self, blocks, classes, entities, items, language, recipes, source, tags, version):
        self.blocks = blocks
        self.classes = classes
        self.entities = entities
        self.items = items
        self.language = language
        self.recipes = recipes
        self.source = source
        self.tags = tags
        self.version = version

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict[0])
