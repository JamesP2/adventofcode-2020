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


# Consider each direction and see how many occupied seats are visible
# An empty seat BLOCKS any occupied seats from view
def seen_occupied_seats(seats, row_index, col_index):
    occupied_seat_directions = []

    # N
    for index in range(row_index - 1, -1, -1):
        if seats[index][col_index] == "L":
            break
        if seats[index][col_index] == "#":
            occupied_seat_directions.append("N")
            break

    # NE
    offset = 1
    for index in range(row_index - 1, -1, -1):
        # Don't go out of bounds of the column
        if (
            col_index + offset > len(seats[row_index]) - 1
            or seats[index][col_index + offset] == "L"
        ):
            break
        if seats[index][col_index + offset] == "#":
            occupied_seat_directions.append("NE")
            break

        offset += 1

    # E
    for index in range(col_index + 1, len(seats[row_index])):
        if seats[row_index][index] == "L":
            break
        if seats[row_index][index] == "#":
            occupied_seat_directions.append("E")
            break

    # SE
    offset = 1
    for index in range(row_index + 1, len(seats)):
        # Don't go out of bounds of the column
        if (
            col_index + offset > len(seats[row_index]) - 1
            or seats[index][col_index + offset] == "L"
        ):
            break
        if seats[index][col_index + offset] == "#":
            occupied_seat_directions.append("SE")
            break

        offset += 1

    # S
    for index in range(row_index + 1, len(seats)):
        if seats[index][col_index] == "L":
            break
        if seats[index][col_index] == "#":
            occupied_seat_directions.append("S")
            break

    # SW
    offset = -1
    for index in range(row_index + 1, len(seats)):
        # Don't go out of bounds of the column
        if col_index + offset < 0 or seats[index][col_index + offset] == "L":
            break
        if seats[index][col_index + offset] == "#":
            occupied_seat_directions.append("SW")
            break

        offset -= 1

    # W
    for index in range(col_index - 1, -1, -1):
        if seats[row_index][index] == "L":
            break
        if seats[row_index][index] == "#":
            occupied_seat_directions.append("W")
            break

    # NW
    offset = -1
    for index in range(row_index - 1, -1, -1):
        # Don't go out of bounds of the column
        if col_index + offset < 0 or seats[index][col_index + offset] == "L":
            break
        if seats[index][col_index + offset] == "#":
            occupied_seat_directions.append("NW")
            break

        offset -= 1

    vprint(
        "Row {} Col {} sees: {}".format(row_index, col_index, occupied_seat_directions)
    )
    return len(occupied_seat_directions)


def model_seats(seats):
    # The new array of seats
    new_seats = []

    # Have we changed anything this iteration?
    changed = False

    for row_index, row in enumerate(seats):
        new_seats.append([None] * len(row))
        for col_index, seat in enumerate(row):
            # If a seat is empty (L) and there are no occupied seats in view
            # of it, the seat becomes occupied
            if seat == "L":
                if seen_occupied_seats(seats, row_index, col_index) == 0:
                    new_seats[row_index][col_index] = "#"
                    changed = True
                else:
                    new_seats[row_index][col_index] = "L"

            # If a seat is occupied (#) and five or more seats adjacent to it are
            # also occupied, it becomes empty
            elif seat == "#":
                if seen_occupied_seats(seats, row_index, col_index) >= 5:
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