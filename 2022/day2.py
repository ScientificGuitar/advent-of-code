raw = open("2022/input/day2.txt", "r").read().strip()

games = [[hands for hands in game.split()] for game in raw.split("\n")]


def part_one():
    score = 0
    for opp, me in games:
        opp = "ABC".index(opp)
        me = "XYZ".index(me)
        score += me + 1
        if me == opp:
            score += 3
        if (me == 0 and opp == 2) or (me == 1 and opp == 0) or (me == 2 and opp == 1):
            score += 6
    return score


def part_two():
    score = 0
    for opp, result in games:
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
