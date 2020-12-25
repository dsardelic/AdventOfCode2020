def solution(input_rel_uri):
    with open(input_rel_uri) as ifile:
        grid = [list(line.strip()) for line in ifile.readlines()]
    # assert grid[0][0] == "."
    row_count, col_count = len(grid), len(grid[0])
    offsets = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    ret_value = 1
    for offset_x, offset_y in offsets:
        i, j = 0, 0
        tree_count = 0
        while i < row_count - offset_x:
            i, j = i + offset_x, (j + offset_y) % col_count
            if grid[i][j] == "#":
                tree_count += 1
        ret_value *= tree_count
    return ret_value


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
