import unittest

from aoc2020 import day_18_part_2


class TestDay18Part2(unittest.TestCase):
    def test_solve_equation(self):
        data = [
            ["1 + 2 * 3 + 4 * 5 + 6", 231],
            ["1 + (2 * 3) + (4 * (5 + 6))", 51],
            ["2 * 3 + (4 * 5)", 46],
            ["5 + (8 * 3 + 9 + 3 * 4 * 3)", 1445],
            ["5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 669060],
            ["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 23340],
        ]
        for equation, exp_result in data:
            with self.subTest(equation=equation):
                self.assertEqual(day_18_part_2.solve_equation(equation), exp_result)

    def test_solution(self):
        data = [
            ["input/day_18.txt", 360029542265462],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_18_part_2.solution(input_file_rel_uri), exp_solution
                )
