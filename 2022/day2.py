def get_input():
    """Get and parse the input."""
    f = open("input/day2.txt", "r")
    raw = f.read().strip()
    games = [[hands for hands in game.split()] for game in raw.split("\n")]
    return games


def part1(data):
    """Solve part 1."""
    score = 0
    for opp, me in data:
        opp = "ABC".index(opp)
        me = "XYZ".index(me)
        score += me + 1
        if me == opp:
            score += 3
        if (me == 0 and opp == 2) or (me == 1 and opp == 0) or (me == 2 and opp == 1):
            score += 6
    return score


def part2(data):
    """Solve part 2."""
    score = 0
    for opp, result in data:
        opp = "ABC".index(opp)
        result = "XYZ".index(result)
        score += result * 3
        if result == 0:
            score += ((opp + 2) % 3) + 1
        elif result == 1:
            score += opp + 1
        elif result == 2:
            score += ((opp + 1) % 3) + 1
    return score


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
