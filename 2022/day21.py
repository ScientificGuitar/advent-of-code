from sympy import solve
from collections import deque

raw = open("2022/input/day21.txt", "r").read().strip()
monkeys = [row.split(": ") for row in raw.split("\n")]
monkeys_dict = dict(monkeys)


def calc_value(monkey):
    val = monkeys_dict[monkey]
    if val.isdigit():
        return int(val)

    m1, operator, m2 = val.split()
    match operator:
        case "+":
            return calc_value(m1) + calc_value(m2)
        case "-":
            return calc_value(m1) - calc_value(m2)
        case "*":
            return calc_value(m1) * calc_value(m2)
        case "/":
            return calc_value(m1) // calc_value(m2)


def is_human_chain(monkey):
    if monkey == "humn":
        return True
    val = monkeys_dict[monkey]
    if val.isdigit():
        return

    m1, _, m2 = val.split()
    return is_human_chain(m1) or is_human_chain(m2)


def part_one():
    return calc_value("root")


def part_two():
    left, right = monkeys_dict["root"].split(" + ")

    human_chain = ""
    monkey_chain = ""
    if is_human_chain(left):
        human_chain = left
        monkey_chain = right
    else:
        human_chain = right
        monkey_chain = left

    expr = f"({human_chain})"
    pending = deque()
    pending.append(human_chain)

    while pending:
        monkey = pending.popleft()
        if monkey == "humn":
            expr = expr.replace(monkey, "x")
        else:
            val = monkeys_dict[monkey]
            if val.isdigit():
                expr = expr.replace(monkey, val)
            else:
                expr = expr.replace(monkey, f"({val})")
                m1, _, m2 = val.split()
                pending.append(m1)
                pending.append(m2)

    value = calc_value(monkey_chain)
    expr = expr + f" - {value}"
    sol = solve(expr)
    return sol[0]
