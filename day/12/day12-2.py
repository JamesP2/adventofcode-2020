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


def rotate_waypoint(old_position, angle):
    angle = math.radians(angle)

    return [
        round(math.cos(angle) * old_position[0] - math.sin(angle) * old_position[1]),
        round(math.sin(angle) * old_position[0] + math.cos(angle) * old_position[1]),
    ]


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
            waypoint_relative_position = rotate_waypoint(
                waypoint_relative_position, value
            )
        elif action == "R":
            waypoint_relative_position = rotate_waypoint(
                waypoint_relative_position, -value
            )
        elif action == "F":
            ship_position[0] += waypoint_relative_position[0] * value
            ship_position[1] += waypoint_relative_position[1] * value

        vprint(
            "Instruction: {}{}, Ship Postion: {}, Waypoint Position: {}".format(
                action, value, ship_position, waypoint_relative_position
            )
        )

vprint("At the end of the instructions the Manhattan distance is:")
print((abs(ship_position[0]) + abs(ship_position[1])))