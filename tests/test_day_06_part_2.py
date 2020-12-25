import unittest

from aoc2020 import day_06_part_2


class TestDay06Part2(unittest.TestCase):
    def test_yes_count(self):
        data = [
            [["abcx", "abcy", "abcz"], 3],
            [["abc"], 3],
            [["a", "b", "c"], 0],
            [["ab", "ac"], 1],
            [["a", "a", "a", "a"], 1],
            [["b"], 1],
        ]
        for answer_strings, exp_yes_count in data:
            with self.subTest(answer_strings=answer_strings):
                self.assertEqual(day_06_part_2.yes_count(answer_strings), exp_yes_count)

    def test_solution(self):
        data = [
            ["input/day_06_example.txt", 3],
            ["input/day_06_example1.txt", 6],
            ["input/day_06.txt", 3466],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_06_part_2.solution(input_file_rel_uri), exp_solution
                )
