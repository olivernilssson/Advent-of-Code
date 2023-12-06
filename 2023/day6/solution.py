import math


def p1(f):
    times, distances = [list(map(int, row.split()[1:])) for row in f]
    total = 1
    for i in range(len(times)):
        time = times[i]
        dist = distances[i]
        total *= sum((time - hold) * hold >= dist for hold in range(time))
    return total


def p2(f):
    time, dist = [int(row.replace(" ", "").split(":")[1]) for row in f]
    lower_bound = (time - math.sqrt(time**2 - 4 * dist)) / 2
    upper_bound = (time + math.sqrt(time**2 - 4 * dist)) / 2
    return math.floor(upper_bound) - math.ceil(lower_bound) + 1


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read().splitlines()

    print(f"Answer Part 1:\n{p1(data)}\n")
    print(f"Answer Part 2:\n{p2(data)}\n")
