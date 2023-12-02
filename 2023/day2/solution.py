bag_contain = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def p1(f):
    total = 0
    for row in f:
        id, game = row.split(": ")
        for round in game.split("; "):
            count_color = {i.split()[1]: int(i.split()[0]) for i in round.split(", ")}
            if any(count_color.get(color, 0) > bag_contain[color] for color in bag_contain):
                break
        else:
            total += int(id.split()[-1])
    return total


def p2(f):
    total = 0
    for row in f:
        id, game = row.split(": ")
        count_color_fewest = {"red": 0, "green": 0, "blue": 0}
        for round in game.split("; "):
            count_color = {i.split()[1]: int(i.split()[0]) for i in round.split(", ")}
            count_color_fewest["red"] = max(count_color_fewest["red"], count_color.get("red", 0))
            count_color_fewest["green"] = max(count_color_fewest["green"], count_color.get("green", 0))
            count_color_fewest["blue"] = max(count_color_fewest["blue"], count_color.get("blue", 0))
        total += count_color_fewest["red"] * count_color_fewest["green"] * count_color_fewest["blue"]
    return total


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read().splitlines()

    print(f"Answer Part 1:\n{p1(data)}\n")
    print(f"Answer Part 2:\n{p2(data)}\n")
