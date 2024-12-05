from collections import defaultdict


def part_1(data):
    left_list = []
    right_list = []
    for row in data:
        left_num, right_num = map(int, row.split())
        left_list.append(int(left_num))
        right_list.append(int(right_num))
    left_list.sort()
    right_list.sort()

    distance = [abs(left - right) for left, right in zip(left_list, right_list)]

    return sum(distance)


def part_2(data):
    left_dict = defaultdict(int)
    right_dict = defaultdict(int)

    for row in data:
        left_num, right_num = map(int, row.split())
        left_dict[left_num] += 1
        right_dict[right_num] += 1

    score = [num * count * right_dict[num] for num, count in left_dict.items()]

    return sum(score)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read().splitlines()

    print(f"Answer Part 1:\n{part_1(data)}\n")
    print(f"Answer Part 2:\n{part_2(data)}")
