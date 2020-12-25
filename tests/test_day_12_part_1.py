import unittest
from collections import defaultdict

from aoc2020 import day_12_part_1


class TestDay12Part1(unittest.TestCase):
    def test_execute_instruction(self):
        data = [
            [("F", 10), ("E", (10, 0))],
            [("N", 3), ("E", (10, 3))],
            [("F", 7), ("E", (17, 3))],
            [("R", 90), ("S", (17, 3))],
            [("F", 11), ("S", (17, -8))],
        ]
        act_orientation = day_12_part_1.Orientation("E", defaultdict(int))
        for fixture_index, fixture in enumerate(data):
            with self.subTest(fixture_index=fixture_index):
                (action, value), (exp_heading, (exp_offset_ew, exp_offset_ns)) = fixture
                day_12_part_1.execute_instruction(action, value, act_orientation)
                self.assertEqual(act_orientation.heading, exp_heading)
                self.assertEqual(act_orientation.ship_abs_ew, exp_offset_ew)
                self.assertEqual(act_orientation.ship_abs_ns, exp_offset_ns)

    def test_solution(self):
        data = [
            ["input/day_12_example.txt", 25],
            ["input/day_12.txt", 1106],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_12_part_1.solution(input_file_rel_uri), exp_solution
                )
