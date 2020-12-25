import unittest

from aoc2020 import day_23_part_1


class TestDay23Part1(unittest.TestCase):
    def test_move_cups(self):
        data = [
            [3, 8, 9, 1, 2, 5, 4, 6, 7],
            [2, 8, 9, 1, 5, 4, 6, 7, 3],
            [5, 4, 6, 7, 8, 9, 1, 3, 2],
            [8, 9, 1, 3, 4, 6, 7, 2, 5],
            [4, 6, 7, 9, 1, 3, 2, 5, 8],
            [1, 3, 6, 7, 9, 2, 5, 8, 4],
            [9, 3, 6, 7, 2, 5, 8, 4, 1],
            [2, 5, 8, 3, 6, 7, 4, 1, 9],
            [6, 7, 4, 1, 5, 8, 3, 9, 2],
            [5, 7, 4, 1, 8, 3, 9, 2, 6],
            [8, 3, 7, 4, 1, 9, 2, 6, 5],
        ]
        act_cups = data[0]
        max_cups = max(act_cups)
        for exp_cups in data[1:]:
            with self.subTest(act_cups=act_cups):
                self.assertEqual(day_23_part_1.move_cups(act_cups, max_cups), exp_cups)
                act_cups = exp_cups

    def test_solution(self):
        data = [
            ["input/day_23_example.txt", 10, "92658374"],
            ["input/day_23_example.txt", "67384529"],
            ["input/day_23.txt", "89372645"],
        ]
        for input_file_rel_uri, *moves_count, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_23_part_1.solution(input_file_rel_uri, *moves_count),
                    exp_solution,
                )
