def get_input():
    """Get and parse the input."""
    f = open("input/day4.txt", "r")
    raw = f.read().strip()
    pairs = [
        [[int(section) for section in elf.split("-")] for elf in pair.split(",")]
        for pair in raw.split("\n")
    ]
    return pairs


def part1(data):
    """Solve part 1."""
    contained = 0
    for elf in data:
        if (elf[0][0] >= elf[1][0] and elf[0][1] <= elf[1][1]) or (
            elf[1][0] >= elf[0][0] and elf[1][1] <= elf[0][1]
        ):
            contained += 1
    return contained


def part2(data):
    """Solve part 2."""
    overlap = 0
    for elf in data:
        if (elf[0][1] >= elf[1][0] and elf[0][0] <= elf[1][0]) or (
            elf[1][1] >= elf[0][0] and elf[1][0] <= elf[0][0]
        ):
            overlap += 1
    return overlap


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
