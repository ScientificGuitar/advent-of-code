raw = open("2022/input/day1.txt", "r").read().strip()
calories = [
    sum([int(calorie) for calorie in elf.split("\n")]) for elf in raw.split("\n\n")
]
calories.sort()


def part_one():
    return calories[-1]


def part_two():
    return sum(calories[-3:])
