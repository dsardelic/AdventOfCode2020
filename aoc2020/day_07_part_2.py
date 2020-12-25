import re
from collections import defaultdict


def get_content_per_color(rules):
    content_per_color = defaultdict(set)
    rule_regex = r"^([\w ]+?) bags contain((?: \d+ [\w ]+? bags?,?)*| no other bags)\.$"
    content_count_and_color_regex = r"^(\d+) ([\w ]+) bags?$"
    for rule in rules:
        color, content_count_and_colors = (
            group.strip() for group in re.match(rule_regex, rule).groups()
        )
        if content_count_and_colors != "no other bags":
            for content_count_and_color in content_count_and_colors.strip().split(", "):
                count, content_color = re.match(
                    content_count_and_color_regex, content_count_and_color
                ).groups()
                content_per_color[color].add((int(count), content_color))
    return content_per_color


def bag_count(color, content_per_color):
    if content := content_per_color[color]:
        return sum(
            count + count * bag_count(color, content_per_color)
            for count, color in content
        )
    return 0


def solution(input_rel_uri):
    with open(input_rel_uri) as ifile:
        rules = ifile.readlines()
    return bag_count("shiny gold", get_content_per_color(rules))


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
