def get_input():
    """Get and parse the input."""
    f = open("input/day1.txt", "r")
    raw = f.read().strip()
    calories = [
        sum([int(calorie) for calorie in elf.split("\n")]) for elf in raw.split("\n\n")
    ]
    calories.sort()
    return calories


def part1(data):
    """Solve part 1."""
    return data[-1]


def part2(data):
    """Solve part 2."""
    return sum(data[-3:])


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
