import argparse

parser = argparse.ArgumentParser(description="Custom Customs")
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


yes_sets = []

current_group_yes = []

with open(args.file) as file:
    for line in file:
        vprint(line)

        # If its a newline we are done with the current set of "yes" answers
        if line == "\n":
            vprint("Finished set {}".format(current_group_yes))
            yes_sets.append(current_group_yes)
            current_group_yes = []
            continue

        line = line.replace("\n", "")

        for char in line:
            if char not in current_group_yes:
                current_group_yes.append(char)

# Catch no blank newline at EOF
vprint("Finished set {}".format(current_group_yes))
yes_sets.append(current_group_yes)

# Sum together number of yes answers
sum = 0
for yes_set in yes_sets:
    sum += len(yes_set)

vprint("Total sum is:")
print(sum)