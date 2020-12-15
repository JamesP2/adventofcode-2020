import argparse
import re

parser = argparse.ArgumentParser(description="Adaptor Array")
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


all_adaptors = []
highest_adaptor_rating = 0

with open(args.file) as file:
    for line_index, line in enumerate(file):
        line = line.replace("\n", "")

        current_adaptor_rating = int(line)
        all_adaptors.append(current_adaptor_rating)

        if current_adaptor_rating > highest_adaptor_rating:
            highest_adaptor_rating = current_adaptor_rating

# Our device adaptor always has a rating of 3 jolts more than the highest rated
# adaptor we have in our crazy bag of adaptors
device_adaptor_rating = highest_adaptor_rating + 3
all_adaptors.append(device_adaptor_rating)

possible_sets = 0

# Get the next adaptor to join the current adaptor order
# This is recursive so all combinations will be tried until the device adaptor
# is reached, where the function will increment the number of possible tests and return
def get_next_adaptors(current_index, current_adaptor_order, remaining_adaptors):
    global device_adaptor_rating, possible_sets

    vprint("Current Index {}, Order {}".format(current_index, current_adaptor_order))

    for index, adaptor in enumerate(remaining_adaptors):

        # If the adaptor is valid then it is an option
        if (
            adaptor > current_adaptor_order[-1]
            and adaptor - current_adaptor_order[-1] <= 3
        ):
            # This will force a new copy of the list to be made in memory
            new_remaining_adaptors = (
                remaining_adaptors[0:index] + remaining_adaptors[index + 1 :]
            )

            # If we've reached the device adaptor rating we've completed the set
            if adaptor == device_adaptor_rating:
                possible_sets += 1
                vprint("Finished Set: {}".format(current_adaptor_order + [adaptor]))
                return

            # Otherwise recurse!
            get_next_adaptors(
                current_index + 1,
                current_adaptor_order + [adaptor],
                new_remaining_adaptors,
            )


get_next_adaptors(0, [0], all_adaptors)

vprint("Number of possible sets:")
print(possible_sets)