import argparse

parser = argparse.ArgumentParser(description='Toboggan Tree Mapper')
parser.add_argument('file', metavar='INPUT_FILE',
                    type=str, help='Input filename')
parser.add_argument('--x', metavar='X_STEPS', type=int, default=3,
                    help='Number of steps to take in the X direction each iteration (default 3)')
parser.add_argument('--y', metavar='Y_STEPS', type=int, default=1,
                    help='Number of steps to take in the Y direction each iteration (default 1)')

args = parser.parse_args()

map = []

with open(args.file) as file:
    for line in file:
        map.append(list(line.replace('\n', '')))

x, y = 0, 0
trees = 0

tree = True if map[y][x] == '#' else False
map[y][x] = 'X' if tree else 'O'
while y < len(map) - 1:
    x += args.x
    y += args.y

    if x > len(map[y]) - 1:
        x -= len(map[y])

    tree = True if map[y][x] == '#' else False
    map[y][x] = 'X' if tree else 'O'

    if tree:
        trees += 1

for (index, line) in enumerate(map):
    print(index, line)

print('Encountered {} trees'.format(trees))
