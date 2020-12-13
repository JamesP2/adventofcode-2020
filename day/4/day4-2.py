import argparse
import re

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

    # Strict validation per key
    for key, value in passport.items():
        # If we get to this point and the passport is already invalid
        # then we can stop checking
        if passport_valid == False:
            break

        vprint(key, value)

        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        if key == 'byr':
            passport_valid = passport_valid if 1920 <= int(
                value) <= 2002 else False
            continue

        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        elif key == 'iyr':
            passport_valid = passport_valid if 2010 <= int(
                value) <= 2020 else False
            continue

        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        elif key == 'eyr':
            passport_valid = passport_valid if 2020 <= int(
                value) <= 2030 else False
            continue

        # hgt (Height) - a number followed by either cm or in:
        #   If cm, the number must be at least 150 and at most 193.
        #   If in, the number must be at least 59 and at most 76.
        elif key == 'hgt':
            try:
                height = int(value[0:-2])
                unit = value[-2:]

                if unit == 'cm':
                    passport_valid = passport_valid if 150 <= height <= 193 else False
                elif unit == 'in':
                    passport_valid = passport_valid if 59 <= height <= 76 else False
                else:
                    passport_valid = False

            except:
                passport_valid = False

            continue

        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        elif key == 'hcl':
            if re.match('^#[0-9 a-f A-F]{6}$', value) == None:
                passport_valid = False
            continue

        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        elif key == 'ecl':
            if value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                passport_valid = False
            continue

        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        elif key == 'pid':
            if re.match('^[0-9]{9}$', value) == None:
                passport_valid = False
            continue
    if passport_valid:
        valid_passports += 1
    else:
        vprint('Invalid!')

vprint('Total number of valid passports:')
print(valid_passports)
