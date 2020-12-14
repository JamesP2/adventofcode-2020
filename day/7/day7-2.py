import argparse
import re

parser = argparse.ArgumentParser(description="Handy Haversacks")
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


bags = []


def find_bag(bag_name):
    for bag in bags:
        if bag.name == bag_name:
            return bag


class Bag:
    name = None
    _holds_shiny_gold_bag = None
    children = None

    def __init__(self, name):
        self.name = name
        self.children = []

        if self.name == "shiny gold":
            self._holds_shiny_gold_bag = True

    def __str__(self):
        return "{} bag. Can hold: {}".format(self.name, self.children)

    def __repr__(self):
        return str(self)

    def holds_shiny_gold_bag(self):
        if self._holds_shiny_gold_bag != None:
            return self._holds_shiny_gold_bag

        for child in self.children:
            if find_bag(child[1]).holds_shiny_gold_bag():
                self._holds_shiny_gold_bag = True
                return True

        self._holds_shiny_gold_bag = False
        return False

    def get_number_of_child_bags(self):
        number_of_child_bags = 0

        for child in self.children:
            number_of_child_bags += child[0]
            number_of_child_bags += child[0] * find_bag(child[1]).get_number_of_child_bags()

        return number_of_child_bags


with open(args.file) as file:
    for line in file:
        # Strip newlines, bag/bags, full stops
        line = re.sub(r" bag(s?)|\.|\n", "", line)

        # Split into [Bag Name, [Qty Bag Name, Qty Bag Name, ...]]
        bag_rule = line.split(" contain ")
        bag_rule[1] = bag_rule[1].split(", ")

        current_bag = Bag(bag_rule[0])

        for child_rule in bag_rule[1]:
            if child_rule == "no other":
                continue
            child_bag = child_rule.split(" ", 1)
            child_bag[0] = int(child_bag[0])
            current_bag.children.append(child_bag)

        bags.append(current_bag)

vprint("Number of individual bags required in a shiny gold bag:")
print(find_bag("shiny gold").get_number_of_child_bags())