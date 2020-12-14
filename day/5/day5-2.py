import argparse

parser = argparse.ArgumentParser(description="Binary Boarding 2")
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


# 128 rows of 8 columns
seats = [[None] * 8 for i in range(128)]
processed_passes = 0

with open(args.file) as file:
    for line in file:
        vprint(line)

        line = line.replace("\n", "")
        row_chars = line[0:7]
        col_chars = line[-3:]
        vprint(row_chars, col_chars)

        range = [0, 127]

        for char in row_chars:
            if char == "F":
                range[1] = int((range[0] + range[1]) / 2)
            elif char == "B":
                range[0] = int((range[0] + range[1]) / 2) + 1
            vprint("Char {} results in row range {}".format(char, range))

        if range[0] != range[1]:
            print("Range {} should match but it doesn't!!")

        row = range[0]

        range = [0, 7]

        for char in col_chars:
            if char == "L":
                range[1] = int((range[0] + range[1]) / 2)
            elif char == "R":
                range[0] = int((range[0] + range[1]) / 2) + 1
            vprint("Char {} results in col range {}".format(char, range))

        if range[0] != range[1]:
            print("Range {} should match but it doesn't!!")

        col = range[0]

        seat_id = int((row * 8) + col)

        vprint(
            "Boarding pass {}: row {}, column {}, seat ID {}".format(
                line, row, col, seat_id
            )
        )

        seats[row][col] = seat_id
        processed_passes += 1

last_id = 0
found_id = None

for row_index, col in enumerate(seats):
    for col_index, seat_id in enumerate(col):
        vprint("Row {}, Col {}, Seat ID {}".format(row_index, col_index, seat_id))

        # If the previous seat was empty and this seat ISN'T empty we have
        # found our seat
        if last_id == None and seat_id != None:
            vprint("Seat ID {} is empty between occupied seats".format(seat_id - 1))
            found_id = seat_id - 1

        last_id = seat_id

vprint("The ID of the empty seat amongst full seats is:")
print(found_id)