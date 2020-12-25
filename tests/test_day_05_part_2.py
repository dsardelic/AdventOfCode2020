import unittest

from aoc2020 import day_05_part_2


class TestDay05Part2(unittest.TestCase):
    def test_solution(self):
        data = [
            ["input/day_05.txt", 522],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_05_part_2.solution(input_file_rel_uri), exp_solution
                )
