import numpy as np
from copy import deepcopy


def get_input():
    """Get and parse the input."""
    f = open("input/day14.txt", "r")
    raw = f.read().strip()
    paths = [
        np.array(
            [
                np.array([det for det in coords.split(",")]).astype(int)
                for coords in path.split(" -> ")
            ]
        )
        for path in raw.split("\n")
    ]
    return paths


def part1(data):
    """Solve part 1."""
    data = deepcopy(data)
    xmax = ymax = 0
    for l in data:
        x, y = l.max(axis=0)
        if x > xmax:
            xmax = x
        if y > ymax:
            ymax = y
    cave = np.full((ymax + 1, xmax), ".")
    for path in data:
        for i in range(len(path) - 1):
            x1 = min(path[i][0], path[i + 1][0])
            y1 = min(path[i][1], path[i + 1][1])
            x2 = max(path[i][0], path[i + 1][0]) + 1
            y2 = max(path[i][1], path[i + 1][1]) + 1
            cave[y1, x1:x2] = "#"
            cave[y1:y2, x1] = "#"
    while True:
        try:
            i += 1
            pour = np.array([500, 0])
            cave[pour[1]][pour[0]] = "+"
            sand = pour
            moving = True
            while moving:
                if cave[sand[1] + 1][sand[0]] == ".":
                    cave[sand[1]][sand[0]] = "."
                    sand += [0, 1]
                    cave[sand[1]][sand[0]] = "+"
                elif cave[sand[1] + 1][sand[0] - 1] == ".":
                    cave[sand[1]][sand[0]] = "."
                    sand += [-1, 1]
                    cave[sand[1]][sand[0]] = "+"
                elif cave[sand[1] + 1][sand[0] + 1] == ".":
                    cave[sand[1]][sand[0]] = "."
                    sand += [1, 1]
                    cave[sand[1]][sand[0]] = "+"
                else:
                    moving = False
        except:
            return np.sum(cave == "+") - 1


def part2(data):
    """Solve part 2."""
    data = deepcopy(data)
    offset = 500
    xmax = ymax = 0
    for l in data:
        x, y = l.max(axis=0)
        if x > xmax:
            xmax = x
        if y > ymax:
            ymax = y
    cave = np.full((ymax + 3, xmax + 1000), ".")
    for path in data:
        for i in range(len(path) - 1):
            x1 = min(path[i][0], path[i + 1][0]) + offset
            y1 = min(path[i][1], path[i + 1][1])
            x2 = max(path[i][0], path[i + 1][0]) + offset + 1
            y2 = max(path[i][1], path[i + 1][1]) + 1
            cave[y1, x1:x2] = "#"
            cave[y1:y2, x1] = "#"
    cave[-1] = "#"
    while np.all(cave[0, 500 + offset - 1 : 500 + offset + 2] != "+"):
        pour = np.array([500 + offset, 0])
        cave[pour[1]][pour[0]] = "+"
        sand = pour
        moving = True
        while moving:
            if cave[sand[1] + 1][sand[0]] == ".":
                cave[sand[1]][sand[0]] = "."
                sand += [0, 1]
                cave[sand[1]][sand[0]] = "+"
            elif cave[sand[1] + 1][sand[0] - 1] == ".":
                cave[sand[1]][sand[0]] = "."
                sand += [-1, 1]
                cave[sand[1]][sand[0]] = "+"
            elif cave[sand[1] + 1][sand[0] + 1] == ".":
                cave[sand[1]][sand[0]] = "."
                sand += [1, 1]
                cave[sand[1]][sand[0]] = "+"
            else:
                moving = False
    return np.sum(cave == "+")


def solve():
    """Get input and solve the different days."""
    data = get_input()
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    solutions = solve()
    print("Solutions:")
    print("\n".join(str(solution) for solution in solutions))
