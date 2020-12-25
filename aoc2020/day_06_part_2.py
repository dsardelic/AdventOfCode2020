import functools

ALPHABET = {chr(ch) for ch in range(ord("a"), ord("z") + 1)}


def yes_count(answer_strings: [str]):
    return len(functools.reduce(set.intersection, answer_strings, ALPHABET))


def solution(input_rel_uri):
    with open(input_rel_uri) as ifile:
        groups = ifile.read().rstrip().split("\n\n")
    return sum(yes_count(group.split("\n")) for group in groups)


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
