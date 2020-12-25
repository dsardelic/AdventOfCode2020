def solution(input_rel_uri):
    with open(input_rel_uri) as ifile:
        joltages = sorted(int(line) for line in ifile.readlines())
    # from collections import Counter;assert set(Counter(joltages).values()) == {1}
    joltage_distribution = {1: 0, 2: 0, 3: 0}
    prev_joltage = 0
    for joltage in joltages:
        joltage_distribution[joltage - prev_joltage] += 1
        prev_joltage = joltage
    return joltage_distribution[1] * (joltage_distribution[3] + 1)


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
