import argparse

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


lines = [line.rstrip("\n") for line in open(args.file)]

for line in lines:
    vprint(line)
