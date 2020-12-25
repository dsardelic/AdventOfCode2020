def move_cups(cups, max_cup):
    curr_cup = cups[0]
    removed_cups, cups = cups[1:4], [cups[0]] + cups[4:]
    destination_cup = curr_cup - 1 or max_cup
    while destination_cup in removed_cups:
        destination_cup = destination_cup - 1 or max_cup
    destination_cup_index = cups.index(destination_cup)
    cups[destination_cup_index + 1 : destination_cup_index + 1] = removed_cups
    cups = cups[1:] + [cups[0]]
    return cups


def solution(input_rel_uri, moves_count=100):
    with open(input_rel_uri) as ifile:
        cups = [int(cup) for cup in ifile.read().strip()]
    max_cup = max(cups)
    for _ in range(moves_count):
        cups = move_cups(cups, max_cup)
    start_index = cups.index(1) + 1
    cups = cups * 2
    end_index = cups.index(1, start_index)
    return "".join(str(cup) for cup in cups[start_index:end_index])


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
