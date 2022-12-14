from copy import deepcopy

raw = open("2022/input/day11.txt", "r").read().strip()
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


def part_one():
    monkeys = deepcopy(notes_dict)
    for _ in range(20):
        for i in monkeys:
            for __ in range(len(monkeys[i]["items"])):
                item = monkeys[i]["items"].pop(0)
                item = str(eval(monkeys[i]["operation"].replace("old", item)) // 3)
                monkeys[i]["inspects"] += 1
                if int(item) % monkeys[i]["test"] == 0:
                    monkeys[monkeys[i]["if_true"]]["items"].append(item)
                else:
                    monkeys[monkeys[i]["if_false"]]["items"].append(item)
    inspects = []
    for i in monkeys:
        inspects.append(monkeys[i]["inspects"])
    inspects.sort(reverse=True)
    monkey_business = inspects[0] * inspects[1]
    return monkey_business


def part_two():
    monkeys = deepcopy(notes_dict)
    mod = 1
    for i in monkeys:
        mod *= monkeys[i]["test"]
    for _ in range(10000):
        for i in monkeys:
            for __ in range(len(monkeys[i]["items"])):
                item = monkeys[i]["items"].pop(0)
                item = str(eval(monkeys[i]["operation"].replace("old", item)) % mod)
                monkeys[i]["inspects"] += 1
                if int(item) % monkeys[i]["test"] == 0:
                    monkeys[monkeys[i]["if_true"]]["items"].append(item)
                else:
                    monkeys[monkeys[i]["if_false"]]["items"].append(item)
    inspects = []
    for i in monkeys:
        inspects.append(monkeys[i]["inspects"])
    inspects.sort(reverse=True)
    monkey_business = inspects[0] * inspects[1]
    return monkey_business
