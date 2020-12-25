import unittest

from aoc2020 import day_04_part_1


class TestDay04Part1(unittest.TestCase):
    def test_solution(self):
        data = [
            ["input/day_04_example.txt", 2],
            ["input/day_04.txt", 250],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_04_part_1.solution(input_file_rel_uri), exp_solution
                )
