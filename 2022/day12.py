import numpy as np
from networkx import DiGraph, shortest_path
from copy import deepcopy


raw = open("2022/input/day12.txt", "r").read().strip()
idx = "abcdefghijklmnopqrstuvwxyz"
grid = np.array(
    [
        [idx.index(col) if col in [c for c in idx] else col for col in row]
        for row in raw.split("\n")
    ]
)


def part_one():
    mountain = deepcopy(grid)
    start = np.where(mountain == "S")
    end = np.where(mountain == "E")
    mountain[start] = 0
    mountain[end] = 25
    mountain = mountain.astype(int)
    sx, sy = start[0][0], start[1][0]
    ex, ey = end[0][0], end[1][0]
    dij = DiGraph()
    height, width = mountain.shape
    cardinals = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for y in range(height):
        for x in range(width):
            for dir in cardinals:
                nx = x + dir[0]
                ny = y + dir[1]
                if nx in range(width) and ny in range(height):
                    a = mountain[y][x]
                    b = mountain[ny][nx]
                    if a + 1 >= b:
                        dij.add_edge((x, y), (nx, ny))
    p = shortest_path(dij, (sy, sx), (ey, ex))
    return len(p) - 1


def part_two():
    mountain = deepcopy(grid)
    s = np.where(mountain == "S")
    e = np.where(mountain == "E")
    mountain[s] = 0
    mountain[e] = 25
    mountain = mountain.astype(int)
    starts = list(zip(*np.where(mountain == 0)))
    paths = []
    for start in starts:
        sx, sy = start[0], start[1]
        ex, ey = e[0][0], e[1][0]
        dij = DiGraph()
        height, width = mountain.shape
        cardinals = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for y in range(height):
            for x in range(width):
                for dir in cardinals:
                    nx = x + dir[0]
                    ny = y + dir[1]
                    if nx in range(width) and ny in range(height):
                        a = mountain[y][x]
                        b = mountain[ny][nx]
                        if a + 1 >= b:
                            dij.add_edge((x, y), (nx, ny))
        try:
            p = shortest_path(dij, (sy, sx), (ey, ex))
            paths.append(len(p) - 1)
        except:
            p = None
    return min(paths)
