import argparse
import re

parser = argparse.ArgumentParser(description="Seating System")
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


seats = []


def print_seats(seats):
    for row in seats:
        string = ""
        for seat in row:
            string += seat
        print(string)


def get_adjacent_seats(seats, row_index, col_index):
    adjacent_seats = []

    # Above (N, NW, NE)
    if row_index > 0:
        # N
        adjacent_seats.append(seats[row_index - 1][col_index])
        # NW
        if col_index > 0:
            adjacent_seats.append(seats[row_index - 1][col_index - 1])
        # NE
        if col_index < len(seats[row_index]) - 1:
            adjacent_seats.append(seats[row_index - 1][col_index + 1])

    # Adjacent (W, E)
    if col_index > 0:
        adjacent_seats.append(seats[row_index][col_index - 1])
    if col_index < len(seats[row_index]) - 1:
        adjacent_seats.append(seats[row_index][col_index + 1])

    # Below (S, SW, SE)
    if row_index < len(seats) - 1:
        # S
        adjacent_seats.append(seats[row_index + 1][col_index])
        # SW
        if col_index > 0:
            adjacent_seats.append(seats[row_index + 1][col_index - 1])
        # SE
        if col_index < len(seats[row_index]) - 1:
            adjacent_seats.append(seats[row_index + 1][col_index + 1])

    return adjacent_seats


def model_seats(seats):
    # The new array of seats
    new_seats = []

    # Have we changed anything this iteration?
    changed = False

    for row_index, row in enumerate(seats):
        new_seats.append([None] * len(row))
        for col_index, seat in enumerate(row):
            # If a seat is empty (L) and there are no occupied seats adjacent
            # to it, the seat becomes occupied
            if seat == "L":
                if "#" not in get_adjacent_seats(seats, row_index, col_index):
                    new_seats[row_index][col_index] = "#"
                    changed = True
                else:
                    new_seats[row_index][col_index] = "L"

            # If a seat is occupied (#) and four or more seats adjacent to it are
            # also occupied, it becomes empty
            elif seat == "#":
                if get_adjacent_seats(seats, row_index, col_index).count("#") >= 4:
                    new_seats[row_index][col_index] = "L"
                    changed = True
                else:
                    new_seats[row_index][col_index] = "#"

            # Otherwise it must be the floor
            else:
                new_seats[row_index][col_index] = seat

    if args.verbose:
        print("After round:")
        print_seats(new_seats)
        print("Changes this round: {}".format(changed))

    return [new_seats, changed]


# Read in the map into a 2D array
with open(args.file) as file:
    for line in file:
        seats.append(list(line.replace("\n", "")))

# Model seats
new_seats = model_seats(seats)

# Track number of iterations
number_iterations = 1

while new_seats[1]:
    vprint("Remodelling")
    new_seats = model_seats(new_seats[0])
    number_iterations += 1

if args.verbose:
    print_seats(new_seats[0])
    print("{} Iterations performed".format(number_iterations))

occupied_seats = 0

# How many occupied seats?
for row in new_seats[0]:
    for seat in row:
        if seat == "#":
            occupied_seats += 1

vprint("Total number of occupied seats:")
print(occupied_seats)