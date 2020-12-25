import unittest

from aoc2020 import day_20_part_2


class TestDay20Part2(unittest.TestCase):
    def test_solution(self):
        data = [
            ["input/day_20_example.txt", 273],
            ["input/day_20.txt", 1599],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_20_part_2.solution(input_file_rel_uri), exp_solution
                )
