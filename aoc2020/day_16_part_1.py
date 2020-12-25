import itertools
import re


def is_invalid_value(value, all_allowed_ranges):
    return not any(value in allowed_range for allowed_range in all_allowed_ranges)


def solution(input_rel_uri):
    with open(input_rel_uri) as ifile:
        information_groups = ifile.read().split("\n\n")
    limits = (
        re.fullmatch(r"[\w ]+: (\d+)-(\d+) or (\d+)-(\d+)", line).groups()
        for line in information_groups[0].split("\n")
    )
    all_allowed_ranges = list(
        itertools.chain.from_iterable(
            (
                range(int(limit[0]), int(limit[1]) + 1),
                range(int(limit[2]), int(limit[3]) + 1),
            )
            for limit in limits
        )
    )

    return sum(
        value
        for line in information_groups[2].strip().split("\n")[1:]
        for ticket in [(int(value) for value in line.strip().split(","))]
        for value in ticket
        if is_invalid_value(value, all_allowed_ranges)
    )


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
