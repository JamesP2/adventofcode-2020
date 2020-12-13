numbers = []

with open('input') as file:
    for line in file:
        numbers.append(int(line))

for first in numbers:
    for second in numbers:
        for third in numbers:
            if first + second + third == 2020:
                product = first * second * third
                print(
                    '{} + {} + {} = 2020. The product of these numbers is {}'.format(first, second, third, product))
                exit(0)