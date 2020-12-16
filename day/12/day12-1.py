import argparse
from enum import IntEnum

parser = argparse.ArgumentParser(description="Rain Risk")
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


class Direction(IntEnum):
    EAST = 0
    SOUTH = 90
    WEST = 180
    NORTH = 270


ship_direction = 0
ship_longitute = 0
ship_latitude = 0

with open(args.file) as file:
    for line in file:
        line = line.replace("\n", "")

        action = line[0]
        value = int(line[1:])

        if action == "N" or (action == "F" and ship_direction == Direction.NORTH):
            ship_longitute += value
        elif action == "S" or (action == "F" and ship_direction == Direction.SOUTH):
            ship_longitute -= value
        elif action == "E" or (action == "F" and ship_direction == Direction.EAST):
            ship_latitude += value
        elif action == "W" or (action == "F" and ship_direction == Direction.WEST):
            ship_latitude -= value
        elif action == "L":
            ship_direction = (ship_direction - value) % 360
        elif action == "R":
            ship_direction = (ship_direction + value) % 360

        vprint(
            "Instruction {}{}. Now at Lon {} Lat {} Direction {}".format(
                action, value, ship_longitute, ship_latitude, ship_direction
            )
        )

vprint("At the end of the instructions the Manhattan distance is:")
print((abs(ship_longitute) + abs(ship_latitude)))