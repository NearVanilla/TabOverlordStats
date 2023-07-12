import random
import subprocess
from pathlib import Path

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
    subprocess.run(["python", script_file, "-w", "secret", "-t", "secret_stat.json"], check=True)
