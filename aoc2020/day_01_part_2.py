def solution(input_rel_uri):
    with open(input_rel_uri) as ifile:
        entries = sorted(int(line.strip()) for line in ifile.readlines())
    i = 0
    while i < len(entries) - 2:
        j, k = i + 1, len(entries) - 1
        while j < k:
            sum_ = entries[i] + entries[j] + entries[k]
            if sum_ == 2020:
                return entries[i] * entries[j] * entries[k]
            if sum_ < 2020:
                j += 1
            else:
                k -= 1
        i += 1


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
