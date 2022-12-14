raw = open("2022/input/day6.txt", "r").read().strip()


def part_one():
    for i in range(len(raw) - 3):
        if len(set(raw[i : i + 4])) == 4:
            return i + 4


def part_two():
    for i in range(len(raw) - 13):
        if len(set(raw[i : i + 14])) == 14:
            return i + 14
