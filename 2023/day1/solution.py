from math import inf


def part_1(data):
    sum = 0
    for row in data:
        first = next(x for x in row if x.isdigit())
        last = next(x for x in row[::-1] if x.isdigit())
        sum += int(f"{first}{last}")
    return sum


word_number = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five":  5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
# Also add numbers as strings "0": 0, "1": 1, ... "9": 9
for i in range(10):
    word_number[str(i)] = i


def part_2(data):
    sum = 0
    for row in data:
        first = min(word_number, key=lambda x: row.index(x) if x in row else inf)
        last = min(word_number, key=lambda x: row[::-1].index(x[::-1]) if x in row else inf)
        sum += int(f"{word_number[first]}{word_number[last]}")
    return sum


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read().splitlines()

    print(f"Answer Part 1:\n{part_1(data)}\n")
    print(f"Answer Part 2:\n{part_2(data)}")
