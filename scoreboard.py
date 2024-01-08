import json
import random
import subprocess
from pathlib import Path
import re

script_dir = Path(__file__).resolve().parent

def convert_scoreboard_name(objective_name: str) -> str:
    """
    Converts the given objective name to a formatted version suitable for a scoreboard.
    
    Args:
        objective_name: The objective name to convert.
        
    Returns:
        The converted objective name.
        
    Raises:
        ValueError: If the objective name is empty.
    """
    if not objective_name:
        raise ValueError("Objective name cannot be empty")

    _objective_name = remove_minecraft_prefix(objective_name)
    _objective_name = replace_special_characters(_objective_name)
    _objective_name = convert_to_title_case(_objective_name)

    return _objective_name


def remove_minecraft_prefix(objective_name: str) -> str:
    """
    Removes the 'minecraft.' prefix from the objective name.
    
    Args:
        objective_name: The objective name to remove the prefix from.
        
    Returns:
        The objective name without the 'minecraft.' prefix.
    """
    return re.sub("minecraft\\.", "", objective_name)


def replace_special_characters(objective_name: str) -> str:
    """
    Replaces special characters '.', ':' and '_' with a space in the objective name.
    
    Args:
        objective_name: The objective name to replace the special characters in.
        
    Returns:
        The objective name with the special characters replaced.
    """
    return re.sub("[.:_]", " ", objective_name)


def convert_to_title_case(objective_name: str) -> str:
    """
    Converts the objective name to title case and removes the 'Custom ' prefix.
    
    Args:
        objective_name: The objective name to convert to title case.
        
    Returns:
        The objective name in title case without the 'Custom ' prefix.
    """
    return objective_name.lower().title().replace("Custom ", "")
    
    

# Create the "usedStats.list" file if it doesn't exist
used_stats_file = script_dir / "data/usedStats.list"
used_stats_file.touch(exist_ok=True)

# Read the stats from the "stats.list" file and remove the used stats from the set
stats_file = script_dir / "data/stats.list"
with stats_file.open() as stats_file, used_stats_file.open(mode="r+") as used_stats_file:
    stats = set(stats_file.read().splitlines())
    used_stats = set(used_stats_file.read().splitlines())
    unused_stats = stats - used_stats

    # Choose a random stat from the remaining stats
    chosen_stat = random.choice(tuple(unused_stats))

    # Add the chosen stat to the "usedStats.list" file
    used_stats_file.write(f"{chosen_stat}\n")

    # Run the "mc_NBT_top_scores.py" script to freeze the previous scores into secret_stat.json
    script_file = script_dir / "utils/mc_NBT_top_scores.py"
    subprocess.run(
        [
            "python3",
            script_file,
            "-i",
            script_dir / "../../server-config/survival/world/data/scoreboard.dat",
            "-w",
            "tab_overlord",
            "-t",
            "secret_stat.json",
        ]
    )

    with open(script_dir / "data/usedStats.list", "r") as _used_stats_file:
        lines = _used_stats_file.readlines()
        if lines:
            old_objective_name = convert_scoreboard_name(lines[-1].strip())
        else:
            exit("File is empty, Please rerun the script :)")
    
    _commands = []

    # Reset the tracking scoreboard
    _commands.append("scoreboard objectives remove old_tab_overlord")
    _commands.append(f'scoreboard objectives add old_tab_overlord dummy "{old_objective_name}"')

    # Copy scores
    with open("secret_stat.json", "r") as secret_stat_file:
        secret_stat_json = json.load(secret_stat_file)

        for score in secret_stat_json["scores"]["tab_overlord"]["scores"]:
            _commands.append(f"scoreboard players set {score['playerName']} old_tab_overlord {score['score']}")

    # Replace the tracking scoreboard
    _commands.append("scoreboard objectives remove tab_overlord")
    _commands.append(f'scoreboard objectives add tab_overlord {chosen_stat}')

    _commands_string = "\n".join(_commands)
    print(_commands_string)
    subprocess.run(["docker-compose", "exec", "-T", "survival", "rcon-cli"], input=_commands_string.encode())
