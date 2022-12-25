import numpy as np

raw = open("2022/input/day22.txt", "r").read()
grid, path = raw.split("\n\n")

max_grid_len = 0
for row in grid.split("\n"):
    max_grid_len = max(max_grid_len, len(row))
grid = np.array(
    [np.array([col for col in row.ljust(max_grid_len)]) for row in grid.split("\n")]
)
moves = []
move = ""
for i in path:
    if i.isdigit():
        move += i
    else:
        moves.append(int(move))
        moves.append(i)
        move = ""
moves.append(int(move))
max_height, max_width = grid.shape


def wrap_2d(current, cardinal):
    dx, dy = cardinal
    x, y = current

    if dy == 0:
        newy = y
        if dx == 1:
            first_rock = np.where(grid[y] == "#")[0][0]
            first_space = np.where(grid[y] == ".")[0][0]
            newx = min(first_rock, first_space)
        else:
            first_rock = np.where(grid[y] == "#")[0][-1]
            first_space = np.where(grid[y] == ".")[0][-1]
            newx = max(first_rock, first_space)
    else:
        newx = x
        if dy == 1:
            first_rock = np.where(grid.T[x] == "#")[0][0]
            first_space = np.where(grid.T[x] == ".")[0][0]
            newy = min(first_rock, first_space)
        else:
            first_rock = np.where(grid.T[x] == "#")[0][-1]
            first_space = np.where(grid.T[x] == ".")[0][-1]
            newy = max(first_rock, first_space)

    if grid[newy][newx] == "#":
        return current
    return (newx, newy)


def move_2d(current, cardinal):
    dx, dy = cardinal
    x, y = current
    newx = x + dx
    newy = y + dy

    if (newx < 0) or (newy < 0) or (newx >= max_width) or (newy >= max_height):
        return wrap_2d(current, cardinal)
    if grid[y + dy][x + dx] == ".":
        return (x + dx, y + dy)
    if grid[y + dy][x + dx] == "#":
        return current
    else:
        return wrap_2d(current, cardinal)


def part_one():
    cardinals = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    facing = 0
    start = (np.where(grid[0] == ".")[0][0], 0)
    current = start

    for move in moves:
        if move == "R":
            facing = (facing + 1) % len(cardinals)
        elif move == "L":
            facing = (facing - 1) % len(cardinals)
        else:
            for _ in range(move):
                current = move_2d(current, cardinals[facing])

    return 1000 * (current[1] + 1) + 4 * ((current[0] + 1)) + facing