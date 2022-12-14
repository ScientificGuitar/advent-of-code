from copy import deepcopy


def get_input():
    """Get and parse the input."""
    f = open("input/day5.txt", "r")
    raw = f.read()
    crates = [row for row in raw.split("\n\n")[0].split("\n")][:-1]
    positions = [pos for pos in raw.split("\n\n")[0].split("\n")[-1]]
    idx = []
    for c in positions:
        if c != " ":
            idx.append(positions.index(c))
    stacks = []
    for row in reversed(crates):
        for i in idx:
            if row[i] != " ":
                if len(stacks) <= (i - 1) // 4:
                    stacks.append([])
                stacks[(i - 1) // 4].append(row[i])
    moves = [
        [int(move.split(" ")[1]), int(move.split(" ")[3]), int(move.split(" ")[5])]
        for move in raw.split("\n\n")[1].strip().split("\n")
    ]
    return moves, stacks


def part1(data):
    """Solve part 1."""
    moves, stacks = data
    stacks = deepcopy(stacks)
    for (n, from_, to) in moves:
        for _ in range(n):
            box = stacks[from_ - 1][-1]
            stacks[from_ - 1] = stacks[from_ - 1][:-1]
            stacks[to - 1].append(box)
    tops = "".join([stack[-1] for stack in stacks])
    return tops


def part2(data):
    """Solve part 2."""
    moves, stacks = data
    stacks = deepcopy(stacks)
    for (n, from_, to) in moves:
        boxes = stacks[from_ - 1][-n:]
        stacks[from_ - 1] = stacks[from_ - 1][:-n]
        stacks[to - 1] += boxes
    tops = "".join([stack[-1] for stack in stacks])
    return tops


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
