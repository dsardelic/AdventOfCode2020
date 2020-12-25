import functools
import itertools
import re


def find_valid_tickets(tickets, allowed_ranges_per_field):
    all_allowed_ranges = list(
        itertools.chain.from_iterable(allowed_ranges_per_field.values())
    )

    def is_valid(ticket):
        return all(
            any(value in allowed_range for allowed_range in all_allowed_ranges)
            for value in ticket
        )

    return tuple(ticket for ticket in tickets if is_valid(ticket))


def field_ordering(valid_tickets, allowed_ranges_per_field):
    def is_valid_fit(index, field):
        return all(
            any(
                valid_ticket[index] in range_
                for range_ in allowed_ranges_per_field[field]
            )
            for valid_ticket in valid_tickets
        )

    # assert len(allowed_ranges_per_field.keys()) == len(tickets[0])
    indices_to_resolve = list(range(len(valid_tickets[0])))
    fields_per_index = {
        index: tuple(
            field
            for field in allowed_ranges_per_field.keys()
            if is_valid_fit(index, field)
        )
        for index in range(len(valid_tickets[0]))
    }
    while indices_to_resolve:
        resolved_fields = []
        for index in list(indices_to_resolve):
            possible_fields = fields_per_index[index]
            # assert possible_fields != tuple()
            if len(possible_fields) == 1:
                fields_per_index[index] = possible_fields[0]
                resolved_fields.append(possible_fields[0])
                indices_to_resolve.remove(index)
        if indices_to_resolve:
            for index in indices_to_resolve:
                fields_per_index[index] = tuple(
                    field
                    for field in fields_per_index[index]
                    if field not in resolved_fields
                )
    return fields_per_index


def solution(input_rel_uri):
    with open(input_rel_uri) as ifile:
        information_groups = ifile.read().split("\n\n")
    allowed_ranges_per_field = {
        tokens[0]: (
            range(int(tokens[1]), int(tokens[2]) + 1),
            range(int(tokens[3]), int(tokens[4]) + 1),
        )
        for line in information_groups[0].split("\n")
        for tokens in [
            re.fullmatch(r"([\w ]+): (\d+)-(\d+) or (\d+)-(\d+)", line).groups()
        ]
    }
    my_ticket = tuple(
        int(token) for token in information_groups[1].strip().split("\n")[1].split(",")
    )
    all_tickets = tuple(
        tuple(int(value) for value in line.split(","))
        for line in information_groups[2].strip().split("\n")[1:]
    )
    return functools.reduce(
        int.__mul__,
        (
            my_ticket[field_index]
            for field_index, field in field_ordering(
                find_valid_tickets(all_tickets, allowed_ranges_per_field),
                allowed_ranges_per_field,
            ).items()
            if field
            in (
                field
                for field in allowed_ranges_per_field.keys()
                if field.startswith("departure")
            )
        ),
        1,
    )


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
