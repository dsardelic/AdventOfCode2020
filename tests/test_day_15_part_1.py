import unittest

from aoc2020 import day_15_part_1


class TestDay15Part1(unittest.TestCase):
    def test_solution(self):
        data = [
            ["input/day_15_example.txt", 436],
            ["input/day_15_example1.txt", 1],
            ["input/day_15_example2.txt", 10],
            ["input/day_15_example3.txt", 27],
            ["input/day_15_example4.txt", 78],
            ["input/day_15_example5.txt", 438],
            ["input/day_15_example6.txt", 1836],
            ["input/day_15.txt", 1238],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_15_part_1.solution(input_file_rel_uri), exp_solution
                )
