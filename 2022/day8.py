import numpy as np


raw = open("2022/input/day8.txt", "r").read().strip()
trees = np.array([[int(tree) for tree in row] for row in raw.split("\n")])


def part_one():
    visibility = np.zeros((trees.shape), dtype=int)
    for row in range(len(trees)):
        max = -1
        max_reversed = -1
        for col in range(len(trees[row])):
            if trees[row][col] > max:
                max = trees[row][col]
                visibility[row][col] += 1

            reversed_row = list(reversed(trees[row]))
            if reversed_row[col] > max_reversed:
                max_reversed = reversed_row[col]
                visibility[row][len(reversed_row) - col - 1] += 1
    data_t = np.transpose(trees)
    visibility = np.transpose(visibility)
    for row in range(len(data_t)):
        max = -1
        max_reversed = -1
        for col in range(len(data_t[row])):
            if data_t[row][col] > max:
                max = data_t[row][col]
                visibility[row][col] += 1
            reversed_row = list(reversed(data_t[row]))
            if reversed_row[col] > max_reversed:
                max_reversed = reversed_row[col]
                visibility[row][len(reversed_row) - col - 1] += 1
    return np.count_nonzero(visibility)


def part_two():
    up = np.zeros((trees.shape), dtype=int)
    down = np.zeros((trees.shape), dtype=int)
    left = np.zeros((trees.shape), dtype=int)
    right = np.zeros((trees.shape), dtype=int)
    for row in range(len(trees)):
        tree_row = trees[row]
        for col in range(len(tree_row) - 1):
            view = 0
            for i in range(col + 1, len(tree_row)):
                if tree_row[i] < tree_row[col]:
                    view += 1
                else:
                    view += 1
                    break
            right[row][col] = view
        reversed_row = list(reversed(trees[row]))
        for col in range(len(reversed_row) - 1):
            view = 0
            for i in range(col + 1, len(reversed_row)):
                if reversed_row[i] < reversed_row[col]:
                    view += 1
                else:
                    view += 1
                    break
            left[row][len(reversed_row) - col - 1] = view
    data_t = np.transpose(trees)
    for row in range(len(data_t)):
        tree_row = data_t[row]
        for col in range(len(tree_row) - 1):
            view = 0
            for i in range(col + 1, len(tree_row)):
                if tree_row[i] < tree_row[col]:
                    view += 1
                else:
                    view += 1
                    break
            down[row][col] = view
        reversed_row = list(reversed(data_t[row]))
        for col in range(len(reversed_row) - 1):
            view = 0
            maxview = -1
            for i in range(col + 1, len(reversed_row)):
                if reversed_row[i] < reversed_row[col]:
                    view += 1
                else:
                    view += 1
                    break
            up[row][len(reversed_row) - col - 1] = view
    scene_score = right * left * down.T * up.T
    return np.max(scene_score)
