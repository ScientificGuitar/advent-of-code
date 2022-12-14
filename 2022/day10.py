def get_input():
    """Get and parse the input."""
    f = open("input/day10.txt", "r")
    raw = f.read().strip()
    program = [
        [inst for inst in instruction.split()] for instruction in raw.split("\n")
    ]
    return program


def part1(data):
    """Solve part 1."""
    cycle = 0
    x = 1
    x_register = [x]
    for instruction in data:
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


def part2(data):
    """Solve part 2."""
    cycle = 0
    x = 1
    x_register = [x]
    for instruction in data:
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
