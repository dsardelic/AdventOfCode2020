import unittest

from aoc2020 import day_02_part_2


class TestDay02Part2(unittest.TestCase):
    def test_solution(self):
        data = [
            ["input/day_02_example.txt", 1],
            ["input/day_02.txt", 313],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_02_part_2.solution(input_file_rel_uri), exp_solution
                )
