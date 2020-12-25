import itertools


def get_surrounding_seats(seat_row_index, seat_col_index, layout, row_count, col_count):
    surrounding_seats = []
    for row_offset, col_offset in itertools.product(range(-1, 2), range(-1, 2)):
        if (row_offset, col_offset) == (0, 0):
            continue
        seek_row, seek_col = seat_row_index + row_offset, seat_col_index + col_offset
        while 0 <= seek_row < row_count and 0 <= seek_col < col_count:
            field = layout[seek_row][seek_col]
            if field in ("L", "#"):
                surrounding_seats.append(field)
                break
            seek_row, seek_col = seek_row + row_offset, seek_col + col_offset
    return surrounding_seats


def apply_rules(layout, row_count, col_count):
    new_layout = []
    for row_index, row in enumerate(layout):
        new_row = []
        for col_index, field in enumerate(row):
            if field in ["L", "#"]:
                surrounding_seats = get_surrounding_seats(
                    row_index, col_index, layout, row_count, col_count
                )
                if field == "L" and "#" not in surrounding_seats:
                    new_row.append("#")
                elif (
                    field == "#" and sum(seat == "#" for seat in surrounding_seats) >= 5
                ):
                    new_row.append("L")
                else:
                    new_row.append(field)
            else:
                new_row.append(field)
        new_layout.append(new_row)
    return new_layout


def fill_seats(layout):
    row_count, col_count = len(layout), len(layout[0])
    prev_layout = object()
    new_layout = layout
    while new_layout != prev_layout:
        prev_layout = new_layout
        new_layout = apply_rules(new_layout, row_count, col_count)
    return new_layout


def solution(input_rel_uri):
    with open(input_rel_uri) as ifile:
        layout = [list(line) for line in ifile.read().strip().split("\n")]
    return sum(
        field == "#" for field in itertools.chain.from_iterable(fill_seats(layout))
    )


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
