
### PART 1 ###
from pprint import pprint
with open("input/input15.txt") as f:
# with open("sample/sample15.txt") as f:
    warehouse,moves=f.read().split('\n\n')

# pprint(lines)
# pprint(warehouse)
# pprint(moves)

warehouse, robot = [list(line) for line in warehouse.split()], warehouse.index('@')
x, y, directions = robot % (len(warehouse[0]) + 1), robot // (len(warehouse[0]) + 1), {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}
warehouse[y][x] = '.'
for move in ''.join(moves.split()):
    x1, y1 = x + directions[move][0], y + directions[move][1]
    while warehouse[y1][x1] == 'O': x1, y1 = x1 + directions[move][0], y1 + directions[move][1]
    if warehouse[y1][x1] == '.':
        if abs(y1 - y + x1 - x) > 1: warehouse[y1][x1], warehouse[y + directions[move][1]][x + directions[move][0]] = 'O', '.'
        x, y = x + directions[move][0], y + directions[move][1]
print("Part 1 solution: ",sum([100 * i + j for i, line in enumerate(warehouse) for j, c in enumerate(line) if c == 'O']))

### PART 2 ###
with open("input/input15.txt") as f:
# with open("sample/sample15.txt") as f:
    warehouse,moves=f.read().split('\n\n')
warehouse, robot = [[('[' if i % 2 == 0 else ']') if line[i // 2] == 'O' else line[i // 2] for i in range(len(line) * 2)] for line in warehouse.split()], warehouse.index('@')
x, y, directions = robot % (len(warehouse[0]) // 2), robot // (len(warehouse[0]) // 2), {'>': 1, '<': -1, '^': -1, 'v': 1}
warehouse[y][x], warehouse[y][x + 1] = '.', '.'
for move in ''.join(moves.split()):
    if move in ['>', '<']:
        x1 = x + (directions[move])
        while warehouse[y][x1] in ['[', ']']: x1 += directions[move]
        if warehouse[y][x1] == '.':
            for x2 in range(x1, x, -directions[move]): warehouse[y][x2] = warehouse[y][x2 - directions[move]]
            x += directions[move]
    else:
        boxes = [{(x, y)}]
        while boxes[-1]:
            boxes.append(set())
            for box in boxes[-2]:
                if warehouse[box[1] + directions[move]][box[0]] == '#': break
                if warehouse[box[1] + directions[move]][box[0]] == '[': boxes[-1] |= {(box[0], box[1] + directions[move]), (box[0] + 1, box[1] + directions[move])}
                elif warehouse[box[1] + directions[move]][box[0]] == ']': boxes[-1] |= {(box[0], box[1] + directions[move]), (box[0] - 1, box[1] + directions[move])}
            else: continue
            break
        else:
            for row in list(reversed(boxes)):
                for box in row: warehouse[box[1] + directions[move]][box[0]], warehouse[box[1]][box[0]] = warehouse[box[1]][box[0]], '.'
            y += directions[move]
print("Part 2 solution: ",sum([100 * i + j for i, line in enumerate(warehouse) for j, c in enumerate(line) if c == '[']))