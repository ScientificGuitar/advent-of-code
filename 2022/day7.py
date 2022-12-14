raw = open("2022/input/day7.txt", "r").read().strip()
lines = [line for line in raw.split("\n")]
dir_tree = {}
current_dir = []
for line in lines:
    command = line.split()
    if command[0] == "$":
        if command[1] == "cd":
            if command[2] == "..":
                current_dir.pop()
            else:
                current_dir.append(command[2])
    else:
        if command[0].isdigit():
            for i in range(len(current_dir)):
                dir = "/".join(current_dir[0 : i + 1])
                if dir in dir_tree:
                    dir_tree[dir] += int(command[0])
                else:
                    dir_tree[dir] = int(command[0])


def part_one():
    return sum(val for val in dir_tree.values() if val <= 100000)


def part_two():
    return min(val for val in dir_tree.values() if val >= dir_tree["/"] - 40000000)
