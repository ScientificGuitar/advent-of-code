from copy import deepcopy


def get_input():
    """Get and parse the input."""
    f = open("input/day11.txt", "r")
    raw = f.read().strip()
    notes = raw.split("\n\n")
    notes_dict = {}
    for monkey in notes:
        lines = monkey.split("\n")
        monkey = lines[0].split()[1][:-1]
        items = lines[1].split(": ")[1].split(", ")
        operation = lines[2].split(" = ")[-1]
        test = int(lines[3].split()[-1])
        if_true = lines[4].split()[-1]
        if_false = lines[5].split()[-1]
        notes_dict[monkey] = {
            "items": items,
            "operation": operation,
            "test": test,
            "if_true": if_true,
            "if_false": if_false,
            "inspects": 0,
        }
    return notes_dict


def part1(data):
    """Solve part 1."""
    data = deepcopy(data)
    for _ in range(20):
        for i in data:
            for __ in range(len(data[i]["items"])):
                item = data[i]["items"].pop(0)
                item = str(eval(data[i]["operation"].replace("old", item)) // 3)
                data[i]["inspects"] += 1
                if int(item) % data[i]["test"] == 0:
                    data[data[i]["if_true"]]["items"].append(item)
                else:
                    data[data[i]["if_false"]]["items"].append(item)
    inspects = []
    for i in data:
        inspects.append(data[i]["inspects"])
    inspects.sort(reverse=True)
    monkey_business = inspects[0] * inspects[1]
    return monkey_business


def part2(data):
    """Solve part 2."""
    data = deepcopy(data)
    mod = 1
    for i in data:
        mod *= data[i]["test"]
    for _ in range(10000):
        for i in data:
            for __ in range(len(data[i]["items"])):
                item = data[i]["items"].pop(0)
                item = str(eval(data[i]["operation"].replace("old", item)) % mod)
                data[i]["inspects"] += 1
                if int(item) % data[i]["test"] == 0:
                    data[data[i]["if_true"]]["items"].append(item)
                else:
                    data[data[i]["if_false"]]["items"].append(item)
    inspects = []
    for i in data:
        inspects.append(data[i]["inspects"])
    inspects.sort(reverse=True)
    monkey_business = inspects[0] * inspects[1]
    return monkey_business


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
