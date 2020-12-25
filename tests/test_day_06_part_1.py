import unittest

from aoc2020 import day_06_part_1


class TestDay06Part1(unittest.TestCase):
    def test_yes_count(self):
        data = [
            [["abcx", "abcy", "abcz"], 6],
            [["abc"], 3],
            [["a", "b", "c"], 3],
            [["ab", "ac"], 3],
            [["a", "a", "a", "a"], 1],
            [["b"], 1],
        ]
        for answer_strings, exp_yes_count in data:
            with self.subTest(answer_strings=answer_strings):
                self.assertEqual(day_06_part_1.yes_count(answer_strings), exp_yes_count)

    def test_solution(self):
        data = [
            ["input/day_06_example.txt", 6],
            ["input/day_06_example1.txt", 11],
            ["input/day_06.txt", 6549],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_06_part_1.solution(input_file_rel_uri), exp_solution
                )
