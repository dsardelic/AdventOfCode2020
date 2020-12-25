import unittest

from aoc2020 import day_03_part_2


class TestDay03Part2(unittest.TestCase):
    def test_solution(self):
        data = [
            ["input/day_03_example.txt", 336],
            ["input/day_03.txt", 3952146825],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_03_part_2.solution(input_file_rel_uri), exp_solution
                )
