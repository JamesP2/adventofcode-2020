import argparse
import re

parser = argparse.ArgumentParser(description="Docking Data")
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
mask_0 = None
mask_1 = None

memory = {}

for line in lines:
    var, value = line.split(" = ")
    if var == "mask":
        mask_0 = int(value.replace("X", "0"), 2)
        mask_1 = int(value.replace("X", "1"), 2)
        vprint("New mask {}".format(value))
    else:
        index = int(var[4:-1])
        memory[index] = (int(value) | mask_0) & mask_1
        vprint("Index {} value {}".format(index, memory[index]))

sum = 0
for value in memory.values():
    sum += value

vprint("The sum of all values in memory is:")
print(sum)
