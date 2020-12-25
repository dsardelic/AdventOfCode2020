def solution(input_rel_uri):
    def row_from_code(code: str) -> int:
        return int(code[:7].replace("F", "0").replace("B", "1"), 2)

    def col_from_code(code: str) -> int:
        return int(code[-3:].replace("L", "0").replace("R", "1"), 2)

    with open(input_rel_uri) as ifile:
        codes = [line.strip() for line in ifile.readlines()]
    seat_ids = [row_from_code(code) * 8 + col_from_code(code) for code in codes]
    empty_seats = set(range(min(seat_ids), max(seat_ids) + 1)).difference(seat_ids)
    for empty_seat in empty_seats:
        if empty_seat - 1 not in empty_seats and empty_seat + 1 not in empty_seats:
            return empty_seat
    return None


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
