import itertools


def get_weak_element(stream, preamble_size):
    sums_per_index_pair = {
        index_pair: sum(stream[index] for index in index_pair)
        for index_pair in itertools.combinations(range(preamble_size), 2)
        if stream[index_pair[0]] != stream[index_pair[1]]
    }
    for value_index, value in enumerate(stream[preamble_size:], preamble_size):
        if value not in sums_per_index_pair.values():
            return value
        sums_per_index_pair = {
            index_pair: sum_
            for index_pair, sum_ in sums_per_index_pair.items()
            if index_pair[0] != value_index - preamble_size
        }
        sums_per_index_pair.update(
            {
                (prev_index, value_index): stream[prev_index] + value
                for prev_index in range(value_index - preamble_size + 1, value_index)
            }
        )
    return None


def solution(input_rel_uri, preamble_size=25):
    with open(input_rel_uri) as ifile:
        stream = [int(line.strip()) for line in ifile.readlines()]
    return get_weak_element(stream, preamble_size)


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt", 5))
