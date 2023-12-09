import sys

sys.setrecursionlimit(30000)


def build_map(data):
    paths = {}
    for i in data[2:]:
        [start, to] = i.split(" = ")
        [left, right] = to[1:-1].split(", ")
        paths[start] = {"L": left, "R": right}
    return paths


def walk(key, instructions, m, steps):
    return steps if key == "ZZZ" else walk(m[key][instructions[steps % len(instructions)]], instructions, m, steps+1)


def p1(f):
    instructions = f[0]
    m = build_map(f)
    return walk("AAA", instructions, m, 0)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read().splitlines()

    print(f"Answer Part 1:\n{p1(data)}\n")
