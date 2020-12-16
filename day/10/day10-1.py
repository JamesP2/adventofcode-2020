import argparse

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

# Our device always has a rating of 3 jolts more than the highest rated
# adaptor we have in our crazy bag of adaptors
device_adaptor_rating = highest_adaptor_rating + 3
all_adaptors.append(device_adaptor_rating)

# Order of adaptors. Start with the outlet on the plane which is 0 jolts
adaptor_order = [0]

# We need to know the number of 1 and 3 joltage differences for the solution
one_joltage_differences = 0
three_joltage_differences = 0

while len(all_adaptors) > 0:
    smallest_valid_adaptor = None
    smallest_valid_adaptor_index = None

    # Now look at remainaing adaptors
    for index, adaptor in enumerate(all_adaptors):
        vprint(all_adaptors)
        vprint(adaptor, adaptor_order[-1])

        # Is this adaptor greater than the last one used AND has a rating difference
        # <= 3?
        if adaptor > adaptor_order[-1] and adaptor - adaptor_order[-1] <= 3:
            vprint("{} is valid".format(adaptor))

            # Now we check to see if its the smallest adaptor that is valid.
            # If we don't do this we risk skipping a smaller one and then we're stuck
            if smallest_valid_adaptor == None or smallest_valid_adaptor > adaptor:
                smallest_valid_adaptor = adaptor
                smallest_valid_adaptor_index = index

    # Before we add this one figure out the exact difference in joltage
    if smallest_valid_adaptor - adaptor_order[-1] == 1:
        one_joltage_differences += 1
    elif smallest_valid_adaptor - adaptor_order[-1] == 3:
        three_joltage_differences += 1

    # The smallest adaptor we found is the right one
    adaptor_order.append(smallest_valid_adaptor)
    all_adaptors.pop(smallest_valid_adaptor_index)

vprint(adaptor_order)
vprint(
    "{} differences of 1 jolt and {} differences of 3 jolts".format(
        one_joltage_differences, three_joltage_differences
    )
)
vprint('The product of these two numbers is:')
print(one_joltage_differences * three_joltage_differences)