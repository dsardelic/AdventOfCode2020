import unittest

from aoc2020 import day_07_part_1


class TestDay07Part1(unittest.TestCase):
    def test_get_parents_per_color(self):
        data = [
            [
                "input/day_07_example.txt",
                [
                    ["bright white", {"light red", "dark orange"}],
                    ["muted yellow", {"light red", "dark orange"}],
                    ["shiny gold", {"bright white", "muted yellow"}],
                    ["faded blue", {"muted yellow", "dark olive", "vibrant plum"}],
                    ["dark olive", {"shiny gold"}],
                    ["vibrant plum", {"shiny gold"}],
                    ["dotted black", {"dark olive", "vibrant plum"}],
                    ["light red", set()],
                    ["dark orange", set()],
                ],
            ],
        ]
        for input_file_rel_uri, exp_parents_per_color in data:
            with open(input_file_rel_uri) as ifile:
                rules = ifile.readlines()
            self.assertEqual(len(exp_parents_per_color), len(rules))
            act_parents_per_color = day_07_part_1.get_parents_per_color(rules)
            for color, exp_parents in exp_parents_per_color:
                with self.subTest(input_file=input_file_rel_uri, color=color):
                    self.assertEqual(exp_parents, act_parents_per_color[color])

    def test_get_color_ancestors(self):
        data = [
            [
                "input/day_07_example.txt",
                [
                    ["bright white", {"light red", "dark orange"}],
                    ["muted yellow", {"light red", "dark orange"}],
                    [
                        "shiny gold",
                        {"bright white", "muted yellow", "light red", "dark orange"},
                    ],
                    [
                        "faded blue",
                        {
                            "muted yellow",
                            "dark olive",
                            "vibrant plum",
                            "light red",
                            "dark orange",
                            "shiny gold",
                            "bright white",
                        },
                    ],
                    [
                        "dark olive",
                        {
                            "shiny gold",
                            "bright white",
                            "muted yellow",
                            "light red",
                            "dark orange",
                        },
                    ],
                    [
                        "vibrant plum",
                        {
                            "shiny gold",
                            "bright white",
                            "muted yellow",
                            "light red",
                            "dark orange",
                        },
                    ],
                    [
                        "dotted black",
                        {
                            "dark olive",
                            "vibrant plum",
                            "shiny gold",
                            "bright white",
                            "muted yellow",
                            "light red",
                            "dark orange",
                        },
                    ],
                    ["light red", set()],
                    ["dark orange", set()],
                ],
            ],
        ]
        for input_file_rel_uri, exp_ancestors_per_color in data:
            with open(input_file_rel_uri) as ifile:
                rules = ifile.readlines()
            parents_per_color = day_07_part_1.get_parents_per_color(rules)
            for color, exp_ancestors in exp_ancestors_per_color:
                with self.subTest(input_file=input_file_rel_uri, color=color):
                    self.assertEqual(
                        day_07_part_1.get_color_ancestors(color, parents_per_color),
                        exp_ancestors,
                    )

    def test_solution(self):
        data = [
            ["input/day_07_example.txt", 4],
            ["input/day_07.txt", 197],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_07_part_1.solution(input_file_rel_uri), exp_solution
                )
