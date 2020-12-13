import sys
import re

valid_passwords = 0

with open(sys.argv[1]) as file:
    for line in file:
        # Almost did line[:-2] but then the last line would be too short
        line = line.replace('\n', '')

        # Split line into [minimum, maximum, char, password]
        first_index, second_index, char, password = re.split(
            '-| |: ', line)

        first_index = int(first_index) - 1
        second_index = int(second_index) - 1

        valid = True if (password[first_index] == char and password[second_index] != char) or (
            password[first_index] != char and password[second_index] == char) else False

        print('Looking for {} in password {}. Char {} = {}, Char {} = {}, {}'.format(
            char, password, first_index, password[first_index], second_index, password[second_index], 'Valid' if valid else 'Not Valid!'))

        if valid:
            valid_passwords += 1


print('There are {} valid passwords in the data set.'.format(valid_passwords))
