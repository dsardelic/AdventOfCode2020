import re


def solution(input_rel_uri):
    input_regex = r"(\d+)-(\d+) (\w): (\w+)"
    with open(input_rel_uri) as ifile:
        matches = [re.match(input_regex, line.strip()) for line in ifile.readlines()]
    valid_count = 0
    for match in matches:
        position1, position2, char, password = match.groups()
        position1, position2 = int(position1), int(position2)
        # assert position2 <= len(password)
        if (password[position1 - 1] == char) + (password[position2 - 1] == char) == 1:
            valid_count += 1
    return valid_count


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
