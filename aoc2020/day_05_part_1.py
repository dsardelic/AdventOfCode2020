def row_from_code(code: str) -> int:
    return int(code[:7].replace("F", "0").replace("B", "1"), 2)


def col_from_code(code: str) -> int:
    return int(code[-3:].replace("L", "0").replace("R", "1"), 2)


def solution(input_rel_uri):
    with open(input_rel_uri) as ifile:
        codes = [line.strip() for line in ifile.readlines()]
    return max(row_from_code(code) * 8 + col_from_code(code) for code in codes)


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
