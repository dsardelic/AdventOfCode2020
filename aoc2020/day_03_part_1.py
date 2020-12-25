def solution(input_rel_uri):
    with open(input_rel_uri) as ifile:
        grid = [list(line.strip()) for line in ifile.readlines()]
    # assert grid[0][0] == "."
    row_count, col_count = len(grid), len(grid[0])
    tree_count = 0
    i, j = 0, 0
    while i < row_count - 1:
        i, j = i + 1, (j + 3) % col_count
        if grid[i][j] == "#":
            tree_count += 1
    return tree_count


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
