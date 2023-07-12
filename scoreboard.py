import random
import subprocess
from pathlib import Path

# Create the "usedStats.list" file if it doesn't exist
used_stats_file = Path.joinpath(Path.cwd(), "data/usedStats.list")
if not used_stats_file.exists():
    used_stats_file.touch(exist_ok=True)

# Read the stats from the "stats.list" file and remove the used stats from the set
with open(Path.joinpath(Path.cwd(), "data/stats.list")) as stats_file, open(used_stats_file, mode="r+") as used_stats_file:
    stats = set(stats_file.read().splitlines())
    used_stats = set(used_stats_file.read().splitlines())
    stats -= used_stats

    # Choose a random stat from the remaining stats
    chosen_stat = random.choice(list(stats))

    # Add the chosen stat to the "usedStats.list" file
    used_stats_file.write(chosen_stat + "\n")

    # Run the "mc_NBT_top_scores.py" script to freeze the previous scores into secret_stat.json
    subprocess.run(["python", Path.joinpath(Path.cwd().joinpath("utils/mc_NBT_top_scores.py")), "-w", "secret", "-t", "secret_stat.json"])
