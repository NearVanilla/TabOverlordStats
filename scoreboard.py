import json
import random
import subprocess
from pathlib import Path
import re

script_dir = Path(__file__).resolve().parent

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
    subprocess.run(["python", script_file, "-i", script_dir / "data/scoreboard.dat", "-w", "tab_overlord", "-t", "secret_stat.json"])#, check=True)


    objective = chosen_stat
    objective = re.sub("minecraft\\.", "", objective) # Remove 'minecraft.'
    objective = re.sub("[.:_]", " ", objective) # Replace '.', ':' and '_' with a space
    objective = objective.lower().title().replace("Custom ", "") # Convert to title case

    # # Reset the tracking scoreboard
    print(['scoreboard', 'objectives', 'remove', "old_tab_overlord"])#, check=True)
    print(['scoreboard', 'objectives', 'add', 'old_tab_overlord', 'dummy', objective])#, check=True)

    # # Copy scores
    with open("secret_stat.json", "r") as secret_stat_file:
        secret_stat_json = json.load(secret_stat_file)
        
        for score in secret_stat_json['scores']['tab_overlord']['scores']:
            print(['scoreboard', 'players', 'set', score['playerName'], 'old_tab_overlord', score['score']])#, check=True)

    # # Replace the tracking scoreboard
    print(['scoreboard', 'objectives', 'remove', 'tab_overlord'])#, check=True)
    print(['scoreboard', 'objectives', 'add', 'tab_overlord', chosen_stat])#, check=True)
