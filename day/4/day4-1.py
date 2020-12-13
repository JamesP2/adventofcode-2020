import argparse

parser = argparse.ArgumentParser(description='Passport Validator')
parser.add_argument('file', metavar='INPUT_FILE',
                    type=str, help='Input filename')
parser.add_argument('--verbose', '-v', action='store_true',
                    default=False, help='Verbose output')

args = parser.parse_args()


def vprint(*x):
    if args.verbose:
        if len(x) == 1:
            print(x[0])
        else:
            print(x)


passports = []
current_passport = {}
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid_passports = 0

with open(args.file) as file:
    for line in file:
        # If its a newline we are done with the current passport
        if line == '\n':
            passports.append(current_passport)
            current_passport = {}
            continue

        # Strip end of line newline
        line = line.replace('\n', '')

        # Otherwise split into Key:Value pairs and put these in the current
        # passport
        for kv_string in line.split(' '):
            kv_pair = kv_string.split(':')
            current_passport[kv_pair[0]] = kv_pair[1]

# The input files have no blank line at the end so append the last passport
passports.append(current_passport)

for passport in passports:
    vprint(passport)

    # Let's assume its valid (for now)
    passport_valid = True

    # Iterate through every required field and check if its there.
    # As soon as we find one missing field we can stop checking
    for field in required_fields:
        if field not in passport.keys():
            vprint('Required field {} missing!'.format(field))
            passport_valid = False
            break

    for key, value in passport.items():
        vprint(key, value)

    valid_passports += 1 if passport_valid else 0

vprint('Total number of valid passports:')
print(valid_passports)
