import numpy as np

raw = open("2022/input/day17.txt", "r").read().strip()
gas = [jet for jet in raw]
A = np.array([[1, 1, 1, 1]])
B = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
C = np.array([[0, 0, 1], [0, 0, 1], [1, 1, 1]])
D = np.array([[1], [1], [1], [1]])
E = np.array([[1, 1], [1, 1]])
rocks = [A, B, C, D, E]


def part_one():
    rock_count = 2022
    cave_height = rock_count // 5 * 13
    cave = np.full((cave_height, 7), 0)
    height = 0
    idx = 0

    for i in range(rock_count):
        rock = rocks[i % 5]
        y = cave_height - height - rock.shape[0] - 3
        x = 2
        while (
            np.all(cave[y : y + rock.shape[0], x : x + rock.shape[1]] + rock <= 1)
            and y < cave_height
        ):
            match gas[idx]:
                case "<":
                    x = max(0, x - 1)
                    if np.any(
                        cave[y : y + rock.shape[0], x : x + rock.shape[1]] + rock > 1
                    ):
                        x += 1
                case ">":
                    x = min(7 - rock.shape[1], x + 1)
                    if np.any(
                        cave[y : y + rock.shape[0], x : x + rock.shape[1]] + rock > 1
                    ):
                        x -= 1
            idx = (idx + 1) % len(gas)
            y += 1
        y -= 1

        height = max(height, (cave_height - y))
        cave[y : y + rock.shape[0], x : x + rock.shape[1]] += rock

    return height


def part_two():
    rock_count = 10000
    cave_height = rock_count // 5 * 13
    cave = np.full((cave_height, 7), 0)
    height = 0
    heights = []
    idx = 0

    for i in range(rock_count):
        rock = rocks[i % 5]
        y = cave_height - height - rock.shape[0] - 3
        x = 2
        while (
            np.all(cave[y : y + rock.shape[0], x : x + rock.shape[1]] + rock <= 1)
            and y < cave_height
        ):
            match gas[idx]:
                case "<":
                    x = max(0, x - 1)
                    if np.any(
                        cave[y : y + rock.shape[0], x : x + rock.shape[1]] + rock > 1
                    ):
                        x += 1
                case ">":
                    x = min(7 - rock.shape[1], x + 1)
                    if np.any(
                        cave[y : y + rock.shape[0], x : x + rock.shape[1]] + rock > 1
                    ):
                        x -= 1
            idx = (idx + 1) % len(gas)
            y += 1
        y -= 1

        height = max(height, (cave_height - y))
        heights.append(height)
        cave[y : y + rock.shape[0], x : x + rock.shape[1]] += rock

    n = 1
    repeat = 0
    repeat_value = 0
    for i in range(1, 2000):
        if (
            heights[(n + 1) * i] - heights[(n) * i]
            == heights[(n + 2) * i] - heights[(n + 1) * i]
            == heights[(n + 3) * i] - heights[(n + 2) * i]
        ):
            repeat = i
            repeat_value = heights[(n + 1) * i] - heights[(n) * i]
            break

    offset = 1000000000000 % repeat
    return 1000000000000 // repeat * repeat_value + heights[offset - 1]