def is_safe(sequence, safe_range):
    for i in range(1, len(sequence)):
        if sequence[i] - sequence[i-1] not in safe_range:
            return False
    return True


def part_1(data):
    safe = 0
    for row in data:
        sequence = [int(x) for x in row.split()]
        safe += any(
            is_safe(sequence, safe_range)
            for safe_range in (increasing, decreasing)
        )
    return safe


def part_2(data):
    safe = 0
    for row in data:
        sequence = [int(x) for x in row.split()]
        safe += any(
            is_safe(sequence[:i] + sequence[i+1:], safe_range)
            for safe_range in (increasing, decreasing)
            for i in range(len(sequence))
        )

    return safe


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read().splitlines()
    increasing = range(1, 4)
    decreasing = range(-3, 0)
    print(f"Answer Part 1:\n{part_1(data)}\n")
    print(f"Answer Part 2:\n{part_2(data)}")
