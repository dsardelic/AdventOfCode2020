import unittest

from aoc2020 import day_15_part_2


class TestDay15Part2(unittest.TestCase):
    def test_solution(self):
        data = [
            ["input/day_15_example.txt", 175594],
            ["input/day_15_example1.txt", 2578],
            ["input/day_15_example2.txt", 3544142],
            ["input/day_15_example3.txt", 261214],
            ["input/day_15_example4.txt", 6895259],
            ["input/day_15_example5.txt", 18],
            ["input/day_15_example6.txt", 362],
            ["input/day_15.txt", 3745954],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_15_part_2.solution(input_file_rel_uri), exp_solution
                )
