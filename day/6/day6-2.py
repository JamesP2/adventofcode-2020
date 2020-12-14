import argparse

parser = argparse.ArgumentParser(description="Custom Customs")
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


yes_sets = []

current_group = []
current_person_yes = []

with open(args.file) as file:
    for line in file:
        vprint(line)

        # If its a newline we are done with the current set of "yes" answers
        if line == "\n":
            vprint("Finished set {}".format(current_group))
            yes_sets.append(current_group)
            current_group = []
            current_person_yes = []
            continue

        line = line.replace("\n", "")

        # Get the yes answers for this person
        for char in line:
            current_person_yes.append(char)

        # Commit this persons answers to the group
        current_group.append(current_person_yes)
        current_person_yes = []

# Catch no blank newline at EOF
vprint("Finished set {}".format(current_group))
yes_sets.append(current_group)

# Find the sum of "yes" answers from EVERY person in a group
sum = 0

for group in yes_sets:
    all_yes = 0

    # Iterate through first person's answers
    for char in group[0]:

        # Assume everyone answered yes for now
        everyone_yes = True

        # Now check every other person in the group. If the yes answer is missing
        # then we don't add it to the Sum
        for person_answers in group:
            if char not in person_answers:
                everyone_yes = False
                break

        if everyone_yes:
            sum += 1


vprint("Total sum is:")
print(sum)