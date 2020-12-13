numbers = []

with open('input') as file:
    for line in file:
        numbers.append(int(line))

for first in numbers:
    for second in numbers:
        if first + second == 2020:
            product = first * second
            print(
                '{} + {} = 2020. The product of these numbers is {}'.format(first, second, product))
            exit(0)