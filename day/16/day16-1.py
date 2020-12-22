import argparse
from enum import Enum

parser = argparse.ArgumentParser(description="Ticket Translation")
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


class reading_stage(Enum):
    RULES = 1
    OUR_TICKET = 2
    NEARBY_TICKETS = 3


lines = [line.rstrip("\n") for line in open(args.file)]

our_ticket = []
nearby_tickets = []
rules = {}

current_stage = reading_stage.RULES

for line in lines:
    if line == "": continue
    # Rules always first
    if current_stage == reading_stage.RULES:
        rule_pair = line.split(': ')
        rule = {name: rule_pair[0], ranges: []}
        ranges = rule_pair[1].split(' or ')
        
        for current_range in ranges:
            pass


    if line == "your ticket:":
        current_stage = reading_stage.OUR_TICKET
        continue
    elif line == "nearby tickets:": 
        current_stage = reading_stage.NEARBY_TICKETS
        continue

    elif current_stage == reading_stage.OUR_TICKET:
        our_ticket = [int(value) for value in line.split(",")]
        pass
    elif current_stage == reading_stage.NEARBY_TICKETS:
        nearby_tickets.append([int(value) for value in line.split(",")])
        pass

vprint("Rules: {}".format(rules))
vprint("Our Ticket: {}".format(our_ticket))
vprint("Nearby Tickets: {}".format(nearby_tickets))