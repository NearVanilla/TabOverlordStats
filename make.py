class Make:
    def __init__(self, minecraft_data):
        self.mcdata = minecraft_data

    def create_command(self, data):
        commands = []
        for index in data["dictionary"]:
            commands.append(
                f"""scoreboard objectives add {data["dictionary"][index]} {data["criteria"][index]} \"{data['display_names'][index]}\"""")
        print(commands)

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
        return f"{minecraft_namespace}:minecraft.{item_name}"

    def make_items(self, registry, scoreboard_prefix: str, minecraft_namespace: str, item_display_name_template: str,
                   item_condition):
        dictionary = {}
        criteria = {}
        display_names = {}
        for index in registry:
            item = registry[index]
            item_name: str = registry[index]["name"]
            display_name: str = registry[index]["displayName"]
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

    def create_make_function(self, blacklist, has_recipe=False, whitelist=None):

        def item_not_in_blacklist(item):
            return item["name"] not in blacklist

        def item_has_recipe(item):
            return self._has_crafting_recipe(item) is not None

        def item_in_whitelist(item):
            return item["name"] in whitelist

        def make_function(registry, scoreboard_prefix, minecraft_namespace, item_display_name_template):
            if whitelist is not None:
                condition = lambda item: item_in_whitelist(item)
            else:
                if has_recipe:
                    condition = lambda item: item_not_in_blacklist(item) and item_has_recipe(item)
                else:
                    condition = item_not_in_blacklist
            return self._make_items(registry, scoreboard_prefix, minecraft_namespace, item_display_name_template,
                                    condition)

        return make_function

    def _make_items(self, registry, scoreboard_prefix, minecraft_namespace, item_display_name_template, item_condition):
        return self.make_items(registry=registry, scoreboard_prefix=scoreboard_prefix,
                               minecraft_namespace=minecraft_namespace,
                               item_display_name_template=item_display_name_template, item_condition=item_condition)
