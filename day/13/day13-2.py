import argparse

parser = argparse.ArgumentParser(description="Shuttle Search")
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


lines = [line.rstrip("\n") for line in open(args.file)]

buses = [int(bus) if bus != "x" else None for bus in lines[1].split(",")]

vprint("Buses {}".format(buses))

current_time = 0

while True:
    valid = True
    for offset, bus in enumerate(buses):
        # If there is no bus here then skip to the next one (no constraint)
        if bus == None: continue

        if (current_time + offset) % bus != 0:
            valid = False
            break

    if valid:
        vprint("The earliest timestamp where departures match position in list is:")
        print(current_time)
        break

    current_time += 1