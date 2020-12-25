import unittest

from aoc2020 import day_07_part_2


class TestDay07Part2(unittest.TestCase):
    def test_get_content_per_color(self):
        data = [
            [
                "input/day_07_example.txt",
                {
                    "light red": {(1, "bright white"), (2, "muted yellow")},
                    "dark orange": {(3, "bright white"), (4, "muted yellow")},
                    "bright white": {(1, "shiny gold")},
                    "muted yellow": {(2, "shiny gold"), (9, "faded blue")},
                    "shiny gold": {(1, "dark olive"), (2, "vibrant plum")},
                    "dark olive": {(3, "faded blue"), (4, "dotted black")},
                    "vibrant plum": {(5, "faded blue"), (6, "dotted black")},
                    "faded blue": set(),
                    "dotted black": set(),
                },
            ],
            [
                "input/day_07_example1.txt",
                {
                    "shiny gold": {(2, "dark red")},
                    "dark red": {(2, "dark orange")},
                    "dark orange": {(2, "dark yellow")},
                    "dark yellow": {(2, "dark green")},
                    "dark green": {(2, "dark blue")},
                    "dark blue": {(2, "dark violet")},
                    "dark violet": set(),
                },
            ],
        ]
        for input_file_rel_uri, exp_content_per_color in data:
            with open(input_file_rel_uri) as ifile:
                rules = ifile.readlines()
            act_exp_content_per_color = day_07_part_2.get_content_per_color(rules)
            for exp_color, exp_content in exp_content_per_color.items():
                with self.subTest(input_file=input_file_rel_uri, color=exp_color):
                    self.assertEqual(act_exp_content_per_color[exp_color], exp_content)

    def test_bag_count(self):
        data = [
            [
                "input/day_07_example.txt",
                {
                    "shiny gold": 32,
                },
            ],
            [
                "input/day_07_example1.txt",
                {
                    "shiny gold": 126,
                },
            ],
        ]
        for input_file_rel_uri, exp_bag_count_per_color in data:
            with open(input_file_rel_uri) as ifile:
                rules = ifile.readlines()
            exp_content_per_color = day_07_part_2.get_content_per_color(rules)
            for exp_color, exp_bag_count in exp_bag_count_per_color.items():
                with self.subTest(input_file=input_file_rel_uri, color=exp_color):
                    self.assertEqual(
                        day_07_part_2.bag_count(exp_color, exp_content_per_color),
                        exp_bag_count,
                    )

    def test_solution(self):
        data = [
            ["input/day_07_example.txt", 32],
            ["input/day_07_example1.txt", 126],
            ["input/day_07.txt", 85324],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_07_part_2.solution(input_file_rel_uri), exp_solution
                )
