import numpy as np


def get_input():
    """Get and parse the input."""
    f = open("input/day8.txt", "r")
    raw = f.read().strip()
    trees = np.array([[int(tree) for tree in row] for row in raw.split("\n")])
    return trees


def part1(data):
    """Solve part 1."""
    visibility = np.zeros((data.shape), dtype=int)
    for row in range(len(data)):
        max = -1
        max_reversed = -1
        for col in range(len(data[row])):
            if data[row][col] > max:
                max = data[row][col]
                visibility[row][col] += 1

            reversed_row = list(reversed(data[row]))
            if reversed_row[col] > max_reversed:
                max_reversed = reversed_row[col]
                visibility[row][len(reversed_row) - col - 1] += 1
    data_t = np.transpose(data)
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


def part2(data):
    """Solve part 2."""
    up = np.zeros((data.shape), dtype=int)
    down = np.zeros((data.shape), dtype=int)
    left = np.zeros((data.shape), dtype=int)
    right = np.zeros((data.shape), dtype=int)
    for row in range(len(data)):
        tree_row = data[row]
        for col in range(len(tree_row) - 1):
            view = 0
            for i in range(col + 1, len(tree_row)):
                if tree_row[i] < tree_row[col]:
                    view += 1
                else:
                    view += 1
                    break
            right[row][col] = view
        reversed_row = list(reversed(data[row]))
        for col in range(len(reversed_row) - 1):
            view = 0
            for i in range(col + 1, len(reversed_row)):
                if reversed_row[i] < reversed_row[col]:
                    view += 1
                else:
                    view += 1
                    break
            left[row][len(reversed_row) - col - 1] = view
    data_t = np.transpose(data)
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
