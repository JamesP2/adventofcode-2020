import argparse
from enum import IntEnum
import math

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


def rotate_waypoint(angle):
    global ship_position, waypoint_relative_position

    angle = math.radians(angle)


ship_direction = 0
ship_position = [0, 0]
waypoint_relative_position = [10, 1]

with open(args.file) as file:
    for line in file:
        line = line.replace("\n", "")

        action = line[0]
        value = int(line[1:])

        if action == "N":
            waypoint_relative_position[1] += value
        elif action == "S":
            waypoint_relative_position[1] -= value
        elif action == "E":
            waypoint_relative_position[0] += value
        elif action == "W":
            waypoint_relative_position[0] -= value
        elif action == "L":
            ship_direction = (ship_direction - value) % 360
        elif action == "R":
            ship_direction = (ship_direction + value) % 360
        elif action == "F":
            pass

        vprint(
            "Instruction {}{}. Now at Lon {} Lat {} Direction {}".format(
                action, value, ship_position[0], ship_position[1], ship_direction
            )
        )

vprint("At the end of the instructions the Manhattan distance is:")
print((abs(ship_position[0]) + abs(ship_position[1])))