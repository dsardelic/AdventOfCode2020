import unittest

from aoc2020 import day_21_part_1


class TestDay21Part1(unittest.TestCase):
    def test_solution(self):
        data = [
            ["input/day_21_example.txt", 5],
            ["input/day_21.txt", 2307],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_21_part_1.solution(input_file_rel_uri), exp_solution
                )
