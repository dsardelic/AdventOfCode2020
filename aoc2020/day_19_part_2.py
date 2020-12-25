import regex


def is_valid_message(message, rule_strings):
    def create_regex_per_rule_ids(rule_strings):
        regex_per_rule_ids = {}
        rule_regex = r"(\d+): \"(\w+)\""
        subrule_regex = r"(\d+):((?: \d+)+)(?:(?: \|)((?: \d+)+))?"
        for rule_string in rule_strings:
            if match := regex.match(rule_regex, rule_string):
                regex_per_rule_ids[int(match.group(1))] = match.group(2)
            else:
                match = regex.match(subrule_regex, rule_string)
                regex_per_rule_ids[int(match.group(1))] = [
                    tuple(int(rule_id) for rule_id in match.group(2).strip().split(" "))
                ]
                if match.group(3):
                    regex_per_rule_ids[int(match.group(1))] += [
                        tuple(
                            int(rule_id)
                            for rule_id in match.group(3).strip().split(" ")
                        )
                    ]
        return regex_per_rule_ids

    def assemble_regex(rule_id, regex_per_rule_ids):
        def merge_consecutive_regexes(rule_ids, regex_per_rule_ids):
            return "".join(
                assemble_regex(rule_id, regex_per_rule_ids) for rule_id in rule_ids
            )

        if isinstance(regex_per_rule_ids[rule_id], str):
            return regex_per_rule_ids[rule_id]
        if rule_id == 8:
            return "(?:" + assemble_regex(42, regex_per_rule_ids) + ")+"
        if rule_id == 11:
            return "".join(
                (
                    "(",
                    assemble_regex(42, regex_per_rule_ids),
                    "(?1)?",
                    assemble_regex(31, regex_per_rule_ids),
                    ")",
                )
            )
        return "".join(
            (
                "(?:",
                "|".join(
                    merge_consecutive_regexes(rule_ids, regex_per_rule_ids)
                    for rule_ids in regex_per_rule_ids[rule_id]
                ),
                ")",
            )
        )

    return (
        regex.fullmatch(
            assemble_regex(0, create_regex_per_rule_ids(rule_strings)), message
        )
        is not None
    )


def solution(input_rel_uri):
    with open(input_rel_uri) as ifile:
        data_groups = ifile.read().split("\n\n")
    rule_strings = data_groups[0].split("\n")
    received_messages = data_groups[1].strip().split("\n")
    return sum(is_valid_message(message, rule_strings) for message in received_messages)


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
