import numpy as np

raw = open("2022/input/day15.txt", "r").read().strip()

data = [row for row in raw.split("\n")]
sensors = [
    np.array(sensor.split(": ")[0].split("x=")[1].split(", y=")).astype(int)
    for sensor in data
]
beacons = [
    np.array(beacon.split(": ")[1].split("x=")[1].split(", y=")).astype(int)
    for beacon in data
]


def part_one():
    distances = []
    y = 2000000

    for sensor, beacon in list(zip(sensors, beacons)):
        distances.append(abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1]))

    final_set = set()
    for sensor, distance in list(zip(sensors, distances)):
        if distance - abs(y - sensor[1]) > 0:
            new_min = sensor[0] - (distance - abs(y - sensor[1]))
            new_max = sensor[0] + (distance - abs(y - sensor[1]))
            no_beacon = set(range(new_min, new_max + 1))
            final_set = final_set | no_beacon

    for beacon in beacons:
        if beacon[1] == y and beacon[0] in final_set:
            final_set.remove(beacon[0])
    return(len(final_set))


def part_two():
    distances = []
    for sensor, beacon in list(zip(sensors, beacons)):
            distances.append(abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1]))

    for y in range(4000001):
        ranges = []
        for sensor, distance in list(zip(sensors, distances)):
            if distance - abs(y - sensor[1]) >= 0:
                new_min = sensor[0] - (distance - abs(y - sensor[1]))
                new_max = sensor[0] + (distance - abs(y - sensor[1]))
                ranges.append((new_min, new_max))
        ranges.sort()

        max_ = ranges[0][1]
        for i in range(1, len(ranges)-1):
            a, b = ranges[i], ranges[i+1]
            max_ = max(max_, a[1])

            if b[0] > max_ + 1:
                print(y, '\t', (max_ + 1))
                # RuntimeWarning: overflow encountered in long_scalars
                return(y + (max_ + 1) * 4000000)