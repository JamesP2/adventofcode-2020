import argparse
import re

parser = argparse.ArgumentParser(description="Encoding Error")
parser.add_argument("file", metavar="INPUT_FILE", type=str, help="Input filename")
parser.add_argument(
    "--preamble-length",
    "-p",
    type=int,
    default=25,
    help="Preamble length (test data is only 5)",
)
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


all_numbers = []
previous_numbers = []
first_invalid_number = None

with open(args.file) as file:
    for line_index, line in enumerate(file):
        line = line.replace("\n", "")
        vprint(line_index, line)

        current_number = int(line)
        all_numbers.append(current_number)

        # If we're still under preamble length then we need to read more numbers in
        if line_index < args.preamble_length:
            previous_numbers.append(current_number)
            continue

        number_valid = False

        # Otherwise we are checking to see if this number is a sum of any two
        # of the previous numbers
        for index_1 in range(0, len(previous_numbers)):

            # If the number is already valid from a previous iteration then stop checking
            if number_valid:
                break

            # Otherwise try adding it to every other number
            for index_2 in range(0, len(previous_numbers)):
                # Don't try adding to itself!
                if index_1 == index_2:
                    continue
                if (
                    previous_numbers[index_1] + previous_numbers[index_2]
                    == current_number
                ):
                    number_valid = True
                    break

        previous_numbers.pop(0)
        previous_numbers.append(current_number)

        if not number_valid:
            first_invalid_number = current_number
            break


vprint("The first invalid number found is {}".format(first_invalid_number))

for index_1 in range(0, len(all_numbers)):

    sum = all_numbers[index_1]
    smallest_number = all_numbers[index_1]
    largest_number = all_numbers[index_1]
    
    for index_2 in range(index_1 + 1, len(all_numbers)):
        # Is this number smaller or larger than the smallest or largest??
        if all_numbers[index_2] < smallest_number:
            smallest_number = all_numbers[index_2]
        if all_numbers[index_2] > largest_number:
            largest_number = all_numbers[index_2]

        
        sum += all_numbers[index_2]

        # If we've gone over the target number break out of this loop
        if sum > first_invalid_number:
            break

        # Have we struck gold?
        if sum == first_invalid_number:
            vprint("Found contigious range between indexes {} and {}".format(index_1, index_2))
            vprint("The sum of the smallest number ({}) and largest ({}) is:".format(smallest_number, largest_number))
            print(smallest_number + largest_number)
            exit()

        