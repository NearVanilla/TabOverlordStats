class Make:
    def __init__(self, minecraft_data):
        self.mcdata = minecraft_data

    def create_command(self, data):
        commands = []
        for index in data["dictionary"]:
            commands.append(f"""scoreboard objectives add {data["dictionary"][index]} {data["criteria"][index]} \"{data['display_names'][index]}\"""")
        return commands

    def _has_crafting_recipe(self, item):
        try:
            item_id = item["name"]
            recipe = self.mcdata.recipes[0]["recipes"][item_id]
            return recipe
        except KeyError:
            return None

    def _make_name(self, scoreboard_prefix, item_name):
        return f"{scoreboard_prefix}-{item_name}"

    def _make_minecraft_namespace(self, minecraft_namespace: str, item_name: str):
        if item_name.startswith("minecraft."):
            item_name = item_name.replace("minecraft.", "")

        return f"{minecraft_namespace}:minecraft.{item_name}"

    def make_items(self, registry, scoreboard_prefix: str, minecraft_namespace: str, item_display_name_template: str, item_condition):
        dictionary = {}
        criteria = {}
        display_names = {}

        for index in registry.values():
            item = index
            try:
                item_name = item["item_id"]
            except KeyError:
                item_name = item["text_id"]
            try:
                display_name = index["display_name"]
            except KeyError:
                display_name = None
            if item_condition(item):
                name = self._make_name(scoreboard_prefix, item_name)
                dictionary[name] = name
                criteria[name] = self._make_minecraft_namespace(minecraft_namespace, item_name)
                display_names[name] = item_display_name_template % display_name

        return {
            "dictionary": dictionary,
            "criteria": criteria,
            "display_names": display_names
        }

    def make_entities(self, registry, scoreboard_prefix: str, minecraft_namespace: str, item_display_name_template: str, item_condition, is_entity):
        dictionary = {}
        criteria = {}
        display_names = {}

        for index in registry.values():
            entity = index
            try:
                entity_name = entity["name"]
                display_name = entity["display_name"]
            except KeyError:
                display_name = None
            if item_condition(entity):
                name = self._make_name(scoreboard_prefix, entity_name)
                dictionary[name] = name
                criteria[name] = self._make_minecraft_namespace(minecraft_namespace, entity_name)
                display_names[name] = item_display_name_template % display_name

        return {
            "dictionary": dictionary,
            "criteria": criteria,
            "display_names": display_names
        }

    def make_custom(self, registry, scoreboard_prefix: str, minecraft_namespace: str, item_display_name_template: str, custom_condition, is_custom):
        dictionary = {}
        criteria = {}
        display_names = {}

        for index in registry:
            custom_name, display_name = index, registry[index]
            if custom_condition(custom_name):
                name = self._make_name(scoreboard_prefix, custom_name)
                dictionary[name] = name
                criteria[name] = self._make_minecraft_namespace(minecraft_namespace, custom_name)
                display_names[name] = item_display_name_template % display_name

        return {
            "dictionary": dictionary,
            "criteria": criteria,
            "display_names": display_names
        }

    def create_make_function(self, blacklist, has_recipe=False, is_entity=False, is_custom=False, whitelist=None):

        conditions = {
            "entity_whitelist": lambda entity: entity["name"] in whitelist,
            "item_whitelist": lambda item: item["text_id"] in whitelist,
            "recipe": lambda item: item["text_id"] not in blacklist and self._has_crafting_recipe(item),
            "custom_blacklist": lambda custom: custom not in blacklist,
            "default": lambda item: item["text_id"] not in blacklist,
        }

        if is_entity and whitelist is not None:
            condition = conditions["entity_whitelist"]
        elif whitelist is not None:
            condition = conditions["item_whitelist"]
        elif has_recipe:
            condition = conditions["recipe"]
        elif is_custom:
            condition = conditions["custom_blacklist"]
        else:
            condition = conditions["default"]

        def make_function(registry, scoreboard_prefix, minecraft_namespace, item_display_name_template):
            if is_entity:
                return self._make_entities(registry, scoreboard_prefix, minecraft_namespace, item_display_name_template, condition, is_entity)
            elif is_custom:
                return self._make_custom(registry, scoreboard_prefix, minecraft_namespace, item_display_name_template, condition, is_custom)
            else:
                return self._make_items(registry, scoreboard_prefix, minecraft_namespace, item_display_name_template, condition)

        return make_function

    def _make_items(self, registry, scoreboard_prefix, minecraft_namespace, item_display_name_template, item_condition):
        return self.make_items(registry=registry, scoreboard_prefix=scoreboard_prefix, minecraft_namespace=minecraft_namespace, item_display_name_template=item_display_name_template, item_condition=item_condition)

    def _make_entities(self, registry, scoreboard_prefix, minecraft_namespace, item_display_name_template, item_condition, is_entity):
        return self.make_entities(registry=registry, scoreboard_prefix=scoreboard_prefix, minecraft_namespace=minecraft_namespace, item_display_name_template=item_display_name_template, item_condition=item_condition, is_entity=is_entity)

    def _make_custom(self, registry, scoreboard_prefix, minecraft_namespace, item_display_name_template, custom_condition, is_custom):
        return self.make_custom(registry=registry, scoreboard_prefix=scoreboard_prefix, minecraft_namespace=minecraft_namespace, item_display_name_template=item_display_name_template, custom_condition=custom_condition, is_custom=is_custom)
