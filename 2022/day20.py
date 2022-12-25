raw = open("2022/input/day20.txt", "r").read().strip()
nums = [int(num) for num in raw.split("\n")]


def move(indices, idx, num):
    i = indices.index(idx)
    new_i = (i + num) % (len(indices) - 1)

    if num > 0:
        indices.pop(i)
        indices.insert(new_i, idx)
    elif num < 0:
        indices.pop(i)
        indices.insert(new_i, idx)


def part_one():
    indices = list(range(len(nums)))
    for idx, num in enumerate(nums):
        move(indices, idx, num)

    mixed = [nums[idx] for idx in indices]
    zero_pos = mixed.index(0)
    wrapped = mixed[zero_pos:] + mixed[:zero_pos]

    return (
        wrapped[1000 % len(wrapped)]
        + wrapped[2000 % len(wrapped)]
        + wrapped[3000 % len(wrapped)]
    )


def part_two():
    encrypted = [num * 811589153 for num in nums]
    indices = list(range(len(nums)))

    for _ in range(10):
        for idx, num in enumerate(encrypted):
            move(indices, idx, num)

    mixed = [encrypted[idx] for idx in indices]
    zero_pos = mixed.index(0)
    wrapped = mixed[zero_pos:] + mixed[:zero_pos]

    return (
        wrapped[1000 % len(wrapped)]
        + wrapped[2000 % len(wrapped)]
        + wrapped[3000 % len(wrapped)]
    )
