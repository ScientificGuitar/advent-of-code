raw = open("2022/input/day10.txt", "r").read().strip()
program = [[inst for inst in instruction.split()] for instruction in raw.split("\n")]


def part_one():
    cycle = 0
    x = 1
    x_register = [x]
    for instruction in program:
        match instruction[0]:
            case "noop":
                cycle += 1
                x_register.append(x)
            case "addx":
                cycle += 1
                x_register.append(x)
                cycle += 1
                x += int(instruction[1])
                x_register.append(x)
    sum_signal_strength = 0
    for i in range(19, len(x_register), 40):
        sum_signal_strength += (i + 1) * x_register[i]
    return sum_signal_strength


def part_two():
    cycle = 0
    x = 1
    x_register = [x]
    for instruction in program:
        match instruction[0]:
            case "noop":
                cycle += 1
                x_register.append(x)
            case "addx":
                cycle += 1
                x_register.append(x)
                cycle += 1
                x += int(instruction[1])
                x_register.append(x)
    screen = [[], [], [], [], [], []]
    for i in range(len(x_register) - 1):
        draw_col = i % 40
        draw_row = i // 40
        x_val = x_register[i]
        if abs(draw_col - x_val) > 1:
            screen[draw_row].append(".")
        else:
            screen[draw_row].append("#")
    result = ""
    for row in screen:
        result += "".join(row) + "\n"
    return result
