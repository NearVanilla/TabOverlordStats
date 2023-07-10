import json


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
