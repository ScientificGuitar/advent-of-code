raw = open("2022/input/day4.txt", "r").read().strip()
pairs = [
    [[int(section) for section in elf.split("-")] for elf in pair.split(",")]
    for pair in raw.split("\n")
]


def part_one():
    contained = 0
    for elf in pairs:
        if (elf[0][0] >= elf[1][0] and elf[0][1] <= elf[1][1]) or (
            elf[1][0] >= elf[0][0] and elf[1][1] <= elf[0][1]
        ):
            contained += 1
    return contained


def part_two():
    overlap = 0
    for elf in pairs:
        if (elf[0][1] >= elf[1][0] and elf[0][0] <= elf[1][0]) or (
            elf[1][1] >= elf[0][0] and elf[1][0] <= elf[0][0]
        ):
            overlap += 1
    return overlap
