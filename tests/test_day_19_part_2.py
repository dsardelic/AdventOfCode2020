import unittest

from aoc2020 import day_19_part_2


class TestDay19Part2(unittest.TestCase):
    def test_is_valid_message(self):
        data = [
            [
                (
                    "42: 9 14 | 10 1",
                    "9: 14 27 | 1 26",
                    "10: 23 14 | 28 1",
                    '1: "a"',
                    "11: 42 31",
                    "5: 1 14 | 15 1",
                    "19: 14 1 | 14 14",
                    "12: 24 14 | 19 1",
                    "16: 15 1 | 14 14",
                    "31: 14 17 | 1 13",
                    "6: 14 14 | 1 14",
                    "2: 1 24 | 14 4",
                    "0: 8 11",
                    "13: 14 3 | 1 12",
                    "15: 1 | 14",
                    "17: 14 2 | 1 7",
                    "23: 25 1 | 22 14",
                    "28: 16 1",
                    "4: 1 1",
                    "20: 14 14 | 1 15",
                    "3: 5 14 | 16 1",
                    "27: 1 6 | 14 18",
                    '14: "b"',
                    "21: 14 1 | 1 14",
                    "25: 1 1 | 1 14",
                    "22: 14 14",
                    "8: 42",
                    "26: 14 22 | 1 20",
                    "18: 15 15",
                    "7: 14 5 | 1 21",
                    "24: 14 1",
                ),
                [
                    ["abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa", False],
                    ["bbabbbbaabaabba", True],
                    ["babbbbaabbbbbabbbbbbaabaaabaaa", True],
                    ["aaabbbbbbaaaabaababaabababbabaaabbababababaaa", True],
                    ["bbbbbbbaaaabbbbaaabbabaaa", True],
                    ["bbbababbbbaaaaaaaabbababaaababaabab", True],
                    ["ababaaaaaabaaab", True],
                    ["ababaaaaabbbaba", True],
                    ["baabbaaaabbaaaababbaababb", True],
                    ["abbbbabbbbaaaababbbbbbaaaababb", True],
                    ["aaaaabbaabaaaaababaa", True],
                    ["aaaabbaaaabbaaa", False],
                    ["aaaabbaabbaaaaaaabbbabbbaaabbaabaaa", True],
                    ["babaaabbbaaabaababbaabababaaab", False],
                    ["aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba", True],
                ],
            ],
        ]
        for fixture_index, (rule_strings, validations) in enumerate(data):
            for message, exp_is_valid in validations:
                with self.subTest(fixture_index=fixture_index, message=message):
                    self.assertEqual(
                        day_19_part_2.is_valid_message(message, rule_strings),
                        exp_is_valid,
                    )

    def test_solution(self):
        data = [
            ["input/day_19_example1.txt", 12],
            ["input/day_19.txt", 311],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_19_part_2.solution(input_file_rel_uri), exp_solution
                )
