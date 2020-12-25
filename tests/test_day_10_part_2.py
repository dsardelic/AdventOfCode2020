import unittest

from aoc2020 import day_10_part_2


class TestDay10Part2(unittest.TestCase):
    def test_solution(self):
        data = [
            ["input/day_10_example.txt", 8],
            ["input/day_10_example1.txt", 19208],
            ["input/day_10.txt", 3454189699072],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_10_part_2.solution(input_file_rel_uri), exp_solution
                )
