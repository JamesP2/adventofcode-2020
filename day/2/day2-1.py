import re

valid_passwords = 0

with open('input') as file:
    for line in file:
        # Almost did line[:-2] but then the last line would be too short
        line = line.replace('\n', '')

        # Split line into [minimum, maximum, letter, password]
        min_occurances, max_occurances, letter, password = re.split(
            '-| |: ', line)

        min_occurances = int(min_occurances)
        max_occurances = int(max_occurances)

        occurances = password.count(letter)

        print('{} occurs in password {} {} times. Min {}, Max {}'.format(
            letter, password, occurances, min_occurances, max_occurances))

        if min_occurances <= occurances <= max_occurances:
            valid_passwords += 1
        else:
            print('Not valid!')


print('There are {} valid passwords in the data set.'.format(valid_passwords))
