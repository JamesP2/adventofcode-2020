import argparse
import re

parser = argparse.ArgumentParser(description="Template")
parser.add_argument("file", metavar="INPUT_FILE", type=str, help="Input filename")
parser.add_argument(
    "--verbose", "-v", action="store_true", default=False, help="Verbose output"
)

args = parser.parse_args()


def vprint(*x):
    if args.verbose:
        if len(x) == 1:
            print(x[0])
        else:
            print(x)

with open(args.file) as file:
    for line in file:
        line = line.replace("\n", "")
        vprint("line")