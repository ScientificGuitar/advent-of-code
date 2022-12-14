import numpy as np
from networkx import DiGraph, shortest_path
from copy import deepcopy


def get_input():
    """Get and parse the input."""
    f = open("input/day12.txt", "r")
    raw = f.read().strip()
    idx = "abcdefghijklmnopqrstuvwxyz"
    grid = np.array(
        [
            [idx.index(col) if col in [c for c in idx] else col for col in row]
            for row in raw.split("\n")
        ]
    )
    return grid


def part1(data):
    """Solve part 1."""
    data = deepcopy(data)
    start = np.where(data == "S")
    end = np.where(data == "E")
    data[start] = 0
    data[end] = 25
    data = data.astype(int)
    sx, sy = start[0][0], start[1][0]
    ex, ey = end[0][0], end[1][0]
    dij = DiGraph()
    height, width = data.shape
    cardinals = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for y in range(height):
        for x in range(width):
            for dir in cardinals:
                nx = x + dir[0]
                ny = y + dir[1]
                if nx in range(width) and ny in range(height):
                    a = data[y][x]
                    b = data[ny][nx]
                    if a + 1 >= b:
                        dij.add_edge((x, y), (nx, ny))
    p = shortest_path(dij, (sy, sx), (ey, ex))
    return len(p) - 1


def part2(data):
    """Solve part 2."""
    data = deepcopy(data)
    s = np.where(data == "S")
    e = np.where(data == "E")
    data[s] = 0
    data[e] = 25
    data = data.astype(int)
    starts = list(zip(*np.where(data == 0)))
    paths = []
    for start in starts:
        sx, sy = start[0], start[1]
        ex, ey = e[0][0], e[1][0]
        dij = DiGraph()
        height, width = data.shape
        cardinals = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for y in range(height):
            for x in range(width):
                for dir in cardinals:
                    nx = x + dir[0]
                    ny = y + dir[1]
                    if nx in range(width) and ny in range(height):
                        a = data[y][x]
                        b = data[ny][nx]
                        if a + 1 >= b:
                            dij.add_edge((x, y), (nx, ny))
        try:
            p = shortest_path(dij, (sy, sx), (ey, ex))
            paths.append(len(p) - 1)
        except:
            p = None
    return min(paths)


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
