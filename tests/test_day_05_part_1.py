import unittest

from aoc2020 import day_05_part_1


class TestDay05Part1(unittest.TestCase):
    def test_row_from_code(self):
        data = [
            ["FBFBBFFRLR", 44],
            ["BFFFBBFRRR", 70],
            ["FFFBBBFRRR", 14],
            ["BBFFBBFRLL", 102],
        ]
        for code, exp_row in data:
            with self.subTest(code=code):
                self.assertEqual(day_05_part_1.row_from_code(code), exp_row)

    def test_col_from_code(self):
        data = [
            ["FBFBBFFRLR", 5],
            ["BFFFBBFRRR", 7],
            ["FFFBBBFRRR", 7],
            ["BBFFBBFRLL", 4],
        ]
        for code, exp_col in data:
            with self.subTest(code=code):
                self.assertEqual(day_05_part_1.col_from_code(code), exp_col)

    def test_solution(self):
        data = [
            ["input/day_05_example.txt", 820],
            ["input/day_05.txt", 888],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_05_part_1.solution(input_file_rel_uri), exp_solution
                )
