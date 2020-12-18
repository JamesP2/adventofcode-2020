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

departure_time = int(lines[0])
buses = [int(bus) for bus in lines[1].split(",") if bus != "x"]

vprint("Depart at {}. Buses {}".format(departure_time, buses))

current_time = departure_time

while True:
    for bus in buses:
        if current_time % bus == 0:
            vprint(
                "Found bus {} at time {} after {} minutes".format(
                    bus, current_time, current_time - departure_time
                )
            )
            vprint("The product of bus * wait minutes is")
            print((current_time - departure_time) * bus)
            exit()

    current_time += 1