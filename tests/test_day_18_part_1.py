import unittest

from aoc2020 import day_18_part_1


class TestDay18Part1(unittest.TestCase):
    def test_solve_equation(self):
        data = [
            ["1 + 2 * 3 + 4 * 5 + 6", 71],
            ["1 + (2 * 3) + (4 * (5 + 6))", 51],
            ["2 * 3 + (4 * 5)", 26],
            ["5 + (8 * 3 + 9 + 3 * 4 * 3)", 437],
            ["5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 12240],
            ["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 13632],
        ]
        for equation, exp_result in data:
            with self.subTest(equation=equation):
                self.assertEqual(day_18_part_1.solve_equation(equation), exp_result)

    def test_solution(self):
        data = [
            ["input/day_18.txt", 75592527415659],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_18_part_1.solution(input_file_rel_uri), exp_solution
                )
