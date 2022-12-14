def get_input():
    """Get and parse the input."""
    f = open("input/day7.txt", "r")
    raw = f.read().strip()
    lines = [line for line in raw.split("\n")]
    dir_tree = {}
    current_dir = []

    for line in lines:
        command = line.split()
        if command[0] == "$":
            if command[1] == "cd":
                if command[2] == "..":
                    current_dir.pop()
                else:
                    current_dir.append(command[2])
        else:
            if command[0].isdigit():
                for i in range(len(current_dir)):
                    dir = "/".join(current_dir[0 : i + 1])
                    if dir in dir_tree:
                        dir_tree[dir] += int(command[0])
                    else:
                        dir_tree[dir] = int(command[0])
    return dir_tree


def part1(data):
    """Solve part 1."""
    return sum(val for val in data.values() if val <= 100000)


def part2(data):
    """Solve part 2."""
    return min(val for val in data.values() if val >= data["/"] - 40000000)


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
