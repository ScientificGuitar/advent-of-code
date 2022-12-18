import numpy as np

raw = open("2022/input/day18.txt", "r").read().strip()
drops = [np.array(row.split(",")).astype(int) for row in raw.split("\n")]
drop_locations = set()
for x, y, z in drops:
    drop_locations.add((x, y, z))


def part_one():
    surface = 6 * len(drop_locations)
    directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

    for x, y, z in drop_locations:
        for dx, dy, dz in directions:
            if (x + dx, y + dy, z + dz) in drop_locations:
                surface -= 1

    return surface


def part_two():
    surface = 0
    pending = set([(-1, -1, -1)])
    directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    visited = set()

    while pending:
        x, y, z = pending.pop()

        if (x, y, z) in drop_locations or (x, y, z) in visited:
            continue

        visited.add((x, y, z))

        for dx, dy, dz in directions:
            if -1 <= x + dx <= 25 and -1 <= y + dy <= 25 and -1 <= z + dz <= 25:
                pending.add((x + dx, y + dy, z + dz))

    for x, y, z in drop_locations:
        for dx, dy, dz in directions:
            if (x + dx, y + dy, z + dz) in visited:
                surface += 1

    return surface
