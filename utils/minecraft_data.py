import json
import os
from pathlib import Path
import requests


def extract(version: str):
    if not os.path.exists(os.path.join(os.getcwd(), "data")):
        os.mkdir(os.path.join(os.getcwd(), "data"))

    if not os.path.exists(f"{os.path.join(os.getcwd(), 'data')}/{version}.json"):

        print(f"Extracting data for version {version}")

        try:
            version_request_data = requests.get(
                f"https://raw.githubusercontent.com/Pokechu22/Burger/gh-pages/{version}.json"
            ).json()[0]

            _tmp = {}
            _tmp["blocks"] = version_request_data["blocks"]
            _tmp["entities"] = version_request_data["entities"]
            _tmp["items"] = version_request_data["items"]
            _tmp["recipes"] = version_request_data["recipes"]
            _tmp["language"] = version_request_data["language"]

            with open(
                f"{Path.joinpath(Path.cwd(), 'data')}/{version}.json", "w"
            ) as json_file:
                json.dump(_tmp, json_file)

            print(
                f"Extracted data for version {version}, saved into data/{version}.json"
            )

        except:
            print(f"Could not extract data for version {version}")
            return


class minecraft_data:
    def __init__(self, blocks, entities, items, recipes, language):
        self.blocks = blocks["block"]
        self.entities = entities["entity"]
        self.items = items["item"]
        self.recipes = recipes
        self.language = language

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)
