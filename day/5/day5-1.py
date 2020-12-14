import argparse

parser = argparse.ArgumentParser(description="Binary Boarding")
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


highest_seat_id = 0

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

        if seat_id > highest_seat_id:
            highest_seat_id = seat_id

        vprint(
            "Boarding pass {}: row {}, column {}, seat ID {}".format(
                line, row, col, seat_id
            )
        )

vprint("The highest seat ID is:")
print(highest_seat_id)
