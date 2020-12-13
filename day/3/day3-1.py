import sys

map = []

with open(sys.argv[1]) as file:
    for line in file:
        map.append(list(line.replace('\n', '')))

x, y = 0, 0
trees = 0

tree = True if map[y][x] == '#' else False
map[y][x] = 'X' if tree else 'O'
while y < len(map) - 1:
    x += 3
    y += 1

    if x > len(map[y]) - 1:
        x -= len(map[y])

    tree = True if map[y][x] == '#' else False
    map[y][x] = 'X' if tree else 'O'

    if tree:
        trees += 1

for (index, line) in enumerate(map):
    print(index, line)

print('Encountered {} trees'.format(trees))