import functools


def yes_count(answer_strings: [str]):
    return len(functools.reduce(set.union, answer_strings, set()))


def solution(input_rel_uri):
    with open(input_rel_uri) as ifile:
        groups = ifile.read().rstrip().split("\n\n")
    return sum(yes_count(group.split("\n")) for group in groups)


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
