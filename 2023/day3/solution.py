def p1(grid):

    coordinates = set()

    for row_index, row in enumerate(grid):
        for column, char in enumerate(row):
            if char.isdigit() or char == ".":
                continue
            for i_row in range(row_index - 1, row_index + 2):
                for i_column in range(column - 1, column + 2):
                    if i_row < 0 or i_row >= len(grid) or i_column < 0 or i_column >= len(grid[i_row]) or not grid[i_row][i_column].isdigit():
                        continue
                    while i_column > 0 and grid[i_row][i_column - 1].isdigit():
                        i_column -= 1
                    coordinates.add((i_row, i_column))

    part_numbers = []

    for row, column in coordinates:
        part_number_str = ""
        while column < len(grid[row]) and grid[row][column].isdigit():
            part_number_str += grid[row][column]
            column += 1
        part_numbers.append(int(part_number_str))

    return sum(part_numbers)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read().splitlines()

    print(f"Answer Part 1:\n{p1(data)}\n")
