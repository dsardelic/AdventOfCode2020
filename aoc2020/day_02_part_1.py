import re
from collections import Counter


def solution(input_rel_uri):
    input_regex = r"(\d+)-(\d+) (\w): (\w+)"
    with open(input_rel_uri) as ifile:
        matches = [re.match(input_regex, line.strip()) for line in ifile.readlines()]
    valid_count = 0
    for match in matches:
        min_occurrence, max_occurrence, char, password = match.groups()
        # assert int(min_occurrence) <= int(max_occurrence)
        if int(min_occurrence) <= Counter(password)[char] <= int(max_occurrence):
            valid_count += 1
    return valid_count


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
