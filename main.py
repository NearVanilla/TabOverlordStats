import argparse
import os

from utils import generate
from utils.minecraft_data import extract

parser = argparse.ArgumentParser(
    description="Creates a list of every score for scoreboards in minecraft minus the ones listed in utils/blacklist.py."
)

subparser = parser.add_subparsers(dest="command")

to_extract = subparser.add_parser(
    "extract", help="Extracts the required data for the requested version"
).add_argument("version", help="The version of minecraft you wish to use")
to_convert = subparser.add_parser(
    "convert", help="Converts the extracted data to scores"
).add_argument("version", help="The version of minecraft you wish to use")
to_extract_and_convert = subparser.add_parser(
    "both", help="Extracts the required data and then converts the scores."
).add_argument("version", help="The version of minecraft you wish to use")

args = parser.parse_args()


def check_data_exists(version):
    return os.path.exists(os.path.join(os.getcwd(), "data") + f"/{version}.json")


def check_and_extract_data(version):
    if not check_data_exists(version):
        extract(version)
    else:
        return print(f"Found existing data in data/{version}.json.")


if __name__ == "__main__":
    _version = args.version

    if args.command in ("extract", "both"):
        check_and_extract_data(_version)

    if args.command in ("convert", "both"):
        if not check_data_exists(_version):
            exit(
                f"Required data for version {_version} not found, Please re-run with `extract` argument to extract the data."
            )
        print(generate.gen(_version))
