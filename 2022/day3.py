def get_input():
    """Get and parse the input."""
    f = open("input/day3.txt", "r")
    raw = f.read().strip()
    sacks = [sack for sack in raw.split("\n")]
    return sacks


def part1(data):
    """Solve part 1."""
    sacks = [[sack[: len(sack) // 2], sack[len(sack) // 2 :]] for sack in data]
    priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sum_priorities = 0
    for sack in sacks:
        common_item = (set(sack[0]) & set(sack[1])).pop()
        sum_priorities += priority.index(common_item) + 1
    return sum_priorities


def part2(data):
    """Solve part 2."""
    sacks = [data[idx : idx + 3] for idx in range(0, len(data), 3)]
    priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sum_priorities = 0
    for sack in sacks:
        common_item = (set(sack[0]) & set(sack[1]) & set(sack[2])).pop()
        sum_priorities += priority.index(common_item) + 1

    return sum_priorities


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
