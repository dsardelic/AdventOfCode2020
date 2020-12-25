def solution(input_rel_uri):
    with open(input_rel_uri) as ifile:
        starting_numbers = [int(token) for token in ifile.read().strip().split(",")]
    last_positions_per_number = {
        number: last_position
        for last_position, number in enumerate(starting_numbers[:-1])
    }
    number, position = starting_numbers[-1], len(starting_numbers) - 1
    while position < 2020 - 1:
        if number in last_positions_per_number:
            distance = position - last_positions_per_number[number]
            last_positions_per_number[number] = position
            number = distance
        else:
            last_positions_per_number[number] = position
            number = 0
        position += 1
    return number


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
