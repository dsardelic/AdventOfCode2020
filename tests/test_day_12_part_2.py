import unittest

from aoc2020 import day_12_part_2
from aoc2020.day_12_part_2 import Orientation


class TestDay12Part2(unittest.TestCase):
    def test_execute_instruction(self):
        data = [
            [("F", 10), Orientation(100, 10, 10, 1)],
            [("N", 3), Orientation(100, 10, 10, 4)],
            [("F", 7), Orientation(170, 38, 10, 4)],
            [("R", 90), Orientation(170, 38, 4, -10)],
            [("F", 11), Orientation(214, -72, 4, -10)],
        ]
        act_orientation = Orientation(0, 0, 10, 1)
        for fixture_index, ((action, value), exp_orientation) in enumerate(data):
            with self.subTest(fixture_index=fixture_index):
                day_12_part_2.execute_instruction(action, value, act_orientation)
                self.assertEqual(act_orientation, exp_orientation)

    def test_solution(self):
        data = [
            ["input/day_12_example.txt", 286],
            ["input/day_12.txt", 107281],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_12_part_2.solution(input_file_rel_uri), exp_solution
                )
