import re
from collections import defaultdict


def get_parents_per_color(rules):
    parents_per_color = defaultdict(set)
    rule_regex = r"^([\w ]+?) bags contain((?: \d+ [\w ]+? bags?,?)*| no other bags)\.$"
    children_regex = r"^\d+ ([\w ]+) bags?$"
    for rule in rules:
        parent, child_color_and_counts = (
            group.strip() for group in re.match(rule_regex, rule).groups()
        )
        if child_color_and_counts != "no other bags":
            for child_color_and_count in child_color_and_counts.strip().split(", "):
                child = re.match(children_regex, child_color_and_count).group(1)
                parents_per_color[child].add(parent)
    return parents_per_color


def get_color_ancestors(color, parents_per_color):
    ancestors = set()
    queue = [*parents_per_color[color]]
    while queue:
        ancestor = queue.pop()
        for parent in parents_per_color[ancestor]:
            if parent not in ancestors and parent not in queue:
                queue.append(parent)
        ancestors.add(ancestor)
    return ancestors


def solution(input_rel_uri):
    with open(input_rel_uri) as ifile:
        rules = ifile.readlines()
    return len(get_color_ancestors("shiny gold", get_parents_per_color(rules)))


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
