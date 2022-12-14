raw = open("2022/input/day3.txt", "r").read().strip()
rucksacks = [sack for sack in raw.split("\n")]


def part_one():
    sacks = [[sack[: len(sack) // 2], sack[len(sack) // 2 :]] for sack in rucksacks]
    priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sum_priorities = 0
    for sack in sacks:
        common_item = (set(sack[0]) & set(sack[1])).pop()
        sum_priorities += priority.index(common_item) + 1
    return sum_priorities


def part_two():
    sacks = [rucksacks[idx : idx + 3] for idx in range(0, len(rucksacks), 3)]
    priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sum_priorities = 0
    for sack in sacks:
        common_item = (set(sack[0]) & set(sack[1]) & set(sack[2])).pop()
        sum_priorities += priority.index(common_item) + 1

    return sum_priorities
