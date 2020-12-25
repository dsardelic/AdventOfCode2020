import itertools


def solution(input_rel_uri):
    with open(input_rel_uri) as ifile:
        joltages = sorted(int(line) for line in ifile.readlines())

    arrangement_count_per_joltage = {}

    def count_subarrangements(joltage, joltage_rank):
        if joltage in arrangement_count_per_joltage:
            return arrangement_count_per_joltage[joltage]
        possible_next_joltages = list(
            itertools.takewhile(
                lambda higher_joltage: higher_joltage - joltage <= 3,
                joltages[joltage_rank + 1 :],
            )
        )
        if possible_next_joltages:
            subarrangement_count = sum(
                count_subarrangements(possible_next_joltage, joltage_rank + offset)
                for offset, possible_next_joltage in enumerate(
                    possible_next_joltages, 1
                )
            )
            arrangement_count_per_joltage[joltage] = subarrangement_count
            return subarrangement_count
        arrangement_count_per_joltage[joltage] = 1
        return 1

    return count_subarrangements(0, -1)


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
