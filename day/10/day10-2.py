import argparse

parser = argparse.ArgumentParser(description="Adaptor Array")
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


all_adaptors = []
highest_adaptor_rating = 0

with open(args.file) as file:
    for line_index, line in enumerate(file):
        line = line.replace("\n", "")

        current_adaptor_rating = int(line)
        all_adaptors.append(current_adaptor_rating)

        if current_adaptor_rating > highest_adaptor_rating:
            highest_adaptor_rating = current_adaptor_rating

# Our device adaptor always has a rating of 3 jolts more than the highest rated
# adaptor we have in our crazy bag of adaptors
device_adaptor_rating = highest_adaptor_rating + 3
# all_adaptors.append(device_adaptor_rating)

all_adaptors.sort(reverse=True)

possible_sets = 0


class Adaptor:
    value = 0
    parent = None
    child = None
    solutions = 0

    def __init__(self, value, parent):
        self.value = value
        self.parent = parent

    def __repr__(self):
        return "Adaptor {}, {}".format(self.value, self.solutions)

    def get_list(self):
        if self.child != None:
            return str(self) + " " + self.child.get_list()
        else:
            return str(self)

    def get_number_of_solutions(self):
        vprint(self)
        if self.parent == None:
            self.solutions = 1

        current = self.parent

        while current != None:
            vprint(current)
            if current.value - self.value <= 3:
                vprint('Valid')
                self.solutions += current.solutions
                vprint(self)
                current = current.parent
            else:
                break
        
        vprint(" ")
        vprint(self)
        return (
            self.solutions
            if self.child == None
            else self.solutions + self.child.get_number_of_solutions()
        )


end_adaptor = Adaptor(all_adaptors[0], None)
current_adaptor = end_adaptor

for index in range(1, len(all_adaptors)):
    new_adaptor = Adaptor(all_adaptors[index], current_adaptor)
    current_adaptor.child = new_adaptor
    current_adaptor = new_adaptor


print(end_adaptor.get_number_of_solutions())

print(end_adaptor.get_list())

vprint("Number of possible sets:")
print(possible_sets)