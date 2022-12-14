from copy import deepcopy


raw = open("2022/input/day5.txt", "r").read().strip()
crates = [row for row in raw.split("\n\n")[0].split("\n")][:-1]
positions = [pos for pos in raw.split("\n\n")[0].split("\n")[-1]]
idx = []
for c in positions:
    if c != " ":
        idx.append(positions.index(c))
s = []
for row in reversed(crates):
    for i in idx:
        if row[i] != " ":
            if len(s) <= (i - 1) // 4:
                s.append([])
            s[(i - 1) // 4].append(row[i])
moves = [
    [int(move.split(" ")[1]), int(move.split(" ")[3]), int(move.split(" ")[5])]
    for move in raw.split("\n\n")[1].strip().split("\n")
]


def part_one():
    stacks = deepcopy(s)
    for (n, from_, to) in moves:
        for _ in range(n):
            box = stacks[from_ - 1][-1]
            stacks[from_ - 1] = stacks[from_ - 1][:-1]
            stacks[to - 1].append(box)
    tops = "".join([stack[-1] for stack in stacks])
    return tops


def part_two():
    stacks = deepcopy(s)
    for (n, from_, to) in moves:
        boxes = stacks[from_ - 1][-n:]
        stacks[from_ - 1] = stacks[from_ - 1][:-n]
        stacks[to - 1] += boxes
    tops = "".join([stack[-1] for stack in stacks])
    return tops
