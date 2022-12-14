def get_input():
    """Get and parse the input."""
    f = open("input/day6.txt", "r")
    raw = f.read().strip()
    return raw


def part1(data):
    """Solve part 1."""
    for i in range(len(data) - 3):
        if len(set(data[i : i + 4])) == 4:
            return i + 4


def part2(data):
    """Solve part 2."""
    for i in range(len(data) - 13):
        if len(set(data[i : i + 14])) == 14:
            return i + 14


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
