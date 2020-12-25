def solution(input_rel_uri):
    with open(input_rel_uri) as ifile:
        entries = sorted(int(line.strip()) for line in ifile.readlines())
    i, j = 0, len(entries) - 1
    while i < j:
        sum_ = entries[i] + entries[j]
        if sum_ == 2020:
            return entries[i] * entries[j]
        if sum_ < 2020:
            i += 1
        else:
            j -= 1


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
