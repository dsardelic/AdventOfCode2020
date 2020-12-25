import unittest

from aoc2020 import day_08_part_1


class TestDay08Part1(unittest.TestCase):
    def test_solution(self):
        data = [
            ["input/day_08_example.txt", 5],
            ["input/day_08.txt", 1709],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_08_part_1.solution(input_file_rel_uri), exp_solution
                )
