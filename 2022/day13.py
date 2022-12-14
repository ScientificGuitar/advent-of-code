from copy import deepcopy

raw = open("2022/input/day13.txt", "r").read().strip()
pairs = raw.split("\n\n")
pairs = [pair.split("\n") for pair in pairs]
pairs = [[eval(pair[0]), eval(pair[1])] for pair in pairs]


def is_right_order(left, right):
    for i in range(min(len(left), len(right))):
        if isinstance(left[i], list) and isinstance(right[i], list):
            if is_right_order(left[i], right[i]) == True:
                return True
            if is_right_order(left[i], right[i]) == False:
                return False
        elif isinstance(left[i], list):
            right[i] = [right[i]]
            if is_right_order(left[i], right[i]) == True:
                return True
            if is_right_order(left[i], right[i]) == False:
                return False
        elif isinstance(right[i], list):
            left[i] = [left[i]]
            if is_right_order(left[i], right[i]) == True:
                return True
            if is_right_order(left[i], right[i]) == False:
                return False
        else:
            if left[i] < right[i]:
                return True
            elif left[i] > right[i]:
                return False
    if len(left) < len(right):
        return True
    elif len(left) > len(right):
        return False


def bubbleSort(seq):
    n = len(seq)
    for _ in range(n - 1):
        flag = 0
        for j in range(n - 1):
            left = seq[j]
            right = seq[j + 1]
            if not is_right_order(left, right):
                tmp = seq[j]
                seq[j] = seq[j + 1]
                seq[j + 1] = tmp
                flag = 1
        if flag == 0:
            break
    return seq


def part_one():
    data = deepcopy(pairs)
    right_order_count = 0
    for pair in data:
        left = pair[0]
        right = pair[1]
        if is_right_order(left, right):
            right_order_count += data.index(pair) + 1
    return right_order_count


def part_two():
    data = deepcopy(pairs)
    combined = []
    for p in data:
        combined.append(p[0])
        combined.append(p[1])
    combined.append([[2]])
    combined.append([[6]])
    combined = bubbleSort(combined)
    packet1 = combined.index([[[[2]]]]) + 1
    packet2 = combined.index([[[[6]]]]) + 1
    return packet1 * packet2
