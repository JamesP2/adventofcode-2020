import argparse
import sys

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

memory = {}

masks = []


def generate_masks(mask, start_index=0):
    masks = []

    for index in range(start_index, len(mask)):
        if mask[index] == "X":
            new_mask_0 = mask[0:index] + "0" + mask[index + 1 :]
            new_mask_1 = mask[0:index] + "1" + mask[index + 1 :]

            if "X" in new_mask_0:
                masks.extend(generate_masks(new_mask_0, start_index=index))
            else:
                vprint(new_mask_0)
                masks.append(int(new_mask_0, 2))

            if "X" in new_mask_1:
                masks.extend(generate_masks(new_mask_1, start_index=index))
            else:
                vprint(new_mask_1)
                masks.append(int(new_mask_1, 2))

    return masks


for line in lines:
    var, value = line.split(" = ")
    if var == "mask":
        masks = generate_masks(value)

        vprint("Generated {} masks from {}".format(len(masks), value))
    else:
        index = int(var[4:-1])
        for mask in masks:
            masked_index = index ^ mask
            memory[masked_index] = int(value)
            vprint("Index {} value {}".format(masked_index, memory[masked_index]))

vprint(memory)

sum = 0
for value in memory.values():
    sum += value

vprint("The sum of all values in memory is:")
print(sum)
