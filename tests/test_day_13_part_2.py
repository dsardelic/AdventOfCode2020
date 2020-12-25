import unittest

from aoc2020 import day_13_part_2


class TestDay13Part2(unittest.TestCase):
    def test_solution(self):
        data = [
            ["input/day_13_example.txt", 1068781],
            ["input/day_13_example1.txt", 3417],
            ["input/day_13_example2.txt", 754018],
            ["input/day_13_example3.txt", 779210],
            ["input/day_13_example4.txt", 1261476],
            ["input/day_13_example5.txt", 1202161486],
            ["input/day_13.txt", 402251700208309],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_13_part_2.solution(input_file_rel_uri), exp_solution
                )
