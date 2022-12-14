import numpy as np

raw = open("2022/input/day9.txt", "r").read().strip()
motions = [[motion for motion in row.split()] for row in raw.split("\n")]


def part_one():
    head = np.array([0, 0])
    tail = np.array([0, 0])
    visited = set()
    for direction, steps in motions:
        for _ in range(int(steps)):
            match direction:
                case "R":
                    head += np.array([1, 0])
                case "U":
                    head += np.array([0, 1])
                case "L":
                    head += np.array([-1, 0])
                case "D":
                    head += np.array([0, -1])
            if np.abs(head - tail).max() > 1:
                tail += np.clip(head - tail, -1, 1)
            visited.add(tuple(tail))
    return len(visited)


def part_two():
    visited = set()
    knots = np.array([[0, 0] for _ in range(10)])
    for direction, steps in motions:
        for _ in range(int(steps)):
            match direction:
                case "R":
                    knots[0] += np.array([1, 0])
                case "U":
                    knots[0] += np.array([0, 1])
                case "L":
                    knots[0] += np.array([-1, 0])
                case "D":
                    knots[0] += np.array([0, -1])
            for j in range(1, 10):
                if np.abs(knots[j] - knots[j - 1]).max() > 1:
                    knots[j] += np.clip(knots[j - 1] - knots[j], -1, 1)
            visited.add(tuple(knots[-1]))
    return len(visited)
