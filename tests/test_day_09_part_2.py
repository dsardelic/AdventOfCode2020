import unittest

from aoc2020 import day_09_part_2


class TestDay09Part2(unittest.TestCase):
    def test_solution(self):
        data = [
            ["input/day_09_example1.txt", 5, 62],
            ["input/day_09.txt", 25, 209694133],
        ]
        for input_file_rel_uri, preamble_size, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_09_part_2.solution(input_file_rel_uri, preamble_size),
                    exp_solution,
                )
