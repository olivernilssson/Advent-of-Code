def parse_lottery(row):
    result = row.split(":")[1]
    win_int, outcome_int = [[int(num) for num in part.split()] for part in result.split("|")]
    return win_int, outcome_int


def p1(f):
    total = 0
    for row in f:
        win_int, outcome_int = parse_lottery(row)
        matches = sum(i in win_int for i in outcome_int)
        total += pow(2, (matches-1)) if matches > 2 else matches
    return total


def p2(f):
    cards = {}
    for i, row in enumerate(f):
        win_int, outcome_int = parse_lottery(row)
        count = sum(outcome_int.count(w) for w in win_int)
        cards[i] = cards.get(i, 0) + 1
        for j in range(i + 1, i + count + 1):
            cards[j] = cards.get(j, 0) + cards[i]
    return sum(cards.values())


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read().splitlines()

    print(f"Answer Part 1:\n{p1(data)}\n")
    print(f"Answer Part 2:\n{p2(data)}\n")
