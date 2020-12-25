import dataclasses
import functools
import itertools

MAX_CUP_LABEL = 1_000_000
MOVES_COUNT = 10_000_000


@dataclasses.dataclass
class Cup:
    def __init__(self, label):
        self.label = label
        self.next = None

    def __repr__(self):
        return f"Cup({self.label})"


def find_hiding_stars_cups_labels(input_cup_labels):
    def create_data_structures(input_cup_labels):
        curr_cup = Cup(input_cup_labels[0])
        cup_per_label = {input_cup_labels[0]: curr_cup}
        prev_cup = curr_cup
        for cup_label in itertools.chain(
            input_cup_labels[1:], range(max(input_cup_labels) + 1, MAX_CUP_LABEL + 1)
        ):
            last_cup = Cup(cup_label)
            cup_per_label[cup_label] = last_cup
            prev_cup.next = last_cup
            prev_cup = last_cup
        last_cup.next = curr_cup
        return curr_cup, cup_per_label

    curr_cup, cup_per_label = create_data_structures(input_cup_labels)
    for _ in range(MOVES_COUNT):
        removed_cups_head = curr_cup.next
        removed_cups_labels = [removed_cups_head.label]
        last_removed_cup = removed_cups_head
        for _ in range(2):
            last_removed_cup = last_removed_cup.next
            removed_cups_labels.append(last_removed_cup.label)
        curr_cup.next = last_removed_cup.next
        destination_cup_label = curr_cup.label - 1 or MAX_CUP_LABEL
        while destination_cup_label in removed_cups_labels:
            destination_cup_label = destination_cup_label - 1 or MAX_CUP_LABEL
        destination_cup = cup_per_label[destination_cup_label]
        cup_after_destination_cup = destination_cup.next
        destination_cup.next = removed_cups_head
        last_removed_cup.next = cup_after_destination_cup
        curr_cup = curr_cup.next
    return cup_per_label[1].next.label, cup_per_label[1].next.next.label


def solution(input_rel_uri):
    with open(input_rel_uri) as ifile:
        input_cup_labels = [int(cup_label) for cup_label in ifile.read().strip()]
    return functools.reduce(
        int.__mul__, find_hiding_stars_cups_labels(input_cup_labels)
    )


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
