import re


def part_1(data):
    total = 0
    for a, b in mul.findall(data):
        total += int(a) * int(b)

    return total


def part_2(data):
    do = re.compile(r"do\(\)")
    dont = re.compile(r"don't\(\)")
    total = 0
    enabled = True
    for match in re.finditer(f"{do.pattern}|{dont.pattern}|{mul.pattern}", data):
        match_text = match.group()

        if do.match(match_text):
            enabled = True

        elif dont.match(match_text):
            enabled = False

        elif enabled and (mul_match := mul.match(match_text)):
            a, b = mul_match.groups()
            total += int(a) * int(b)

    return total


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read()
    mul = re.compile(r"mul\((\d+),(\d+)\)")
    print(f"Answer Part 1:\n{part_1(data)}\n")
    print(f"Answer Part 2:\n{part_2(data)}")
