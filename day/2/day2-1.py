import sys
import re

valid_passwords = 0

with open(sys.argv[1]) as file:
    for line in file:
        # Almost did line[:-2] but then the last line would be too short
        line = line.replace('\n', '')

        # Split line into [minimum, maximum, char, password]
        min_occurances, max_occurances, char, password = re.split(
            '-| |: ', line)

        min_occurances = int(min_occurances)
        max_occurances = int(max_occurances)

        occurances = password.count(char)

        print('{} occurs in password {} {} times. Min {}, Max {}'.format(
            char, password, occurances, min_occurances, max_occurances))

        if min_occurances <= occurances <= max_occurances:
            valid_passwords += 1
        else:
            print('Not valid!')


print('There are {} valid passwords in the data set.'.format(valid_passwords))
