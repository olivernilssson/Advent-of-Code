def part_1(data):
    m = len(data)
    n = len(data[0])

    def check_word(r, c, dr, dc, word):
        for i in range(len(word)):
            if not (0 <= r + dr * i < m and 0 <= c + dc * i < n) or data[r + dr * i][c + dc * i] != word[i]:
                return False
        return True

    def count(r, c):
        if data[r][c] != 'X':
            return 0
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),       # up, down, left, right
            (-1, -1), (-1, 1), (1, -1), (1, 1)      # up-left, up-right, down-left, down-right
        ]
        return sum(check_word(r, c, dr, dc, 'XMAS') for dr, dc in directions)

    return sum(count(r, c) for r in range(m) for c in range(n))


def part_2(data):
    m = len(data)
    n = len(data[0])

    def check_pattern(r, c):
        if data[r][c] != 'A':
            return False

        directions = [
            (-1, -1), (-1, 1),      # up-left, up-right
            (1, -1), (1, 1)         # down-left, down-right
        ]

        results = [data[r + dr][c + dc] for dr, dc in directions if (0 <= r + dr < m and 0 <= c + dc < n)]
        if len(results) != 4:
            return False

        ul, ur, dl, dr = results
        return sorted(results) == ['M', 'M', 'S', 'S'] and ul != dr

    return sum(check_pattern(r, c) for r in range(1, m - 1) for c in range(1, n - 1))


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read().splitlines()
    print(f"Answer Part 1:\n{part_1(data)}\n")
    print(f"Answer Part 2:\n{part_2(data)}")
