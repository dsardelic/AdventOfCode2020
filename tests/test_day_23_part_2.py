import unittest

from aoc2020 import day_23_part_2


class TestDay23Part2(unittest.TestCase):
    def test_find_hiding_stars_cups_labels(self):
        data = [
            [[3, 8, 9, 1, 2, 5, 4, 6, 7], (934001, 159792)],
        ]
        for input_cup_labels, exp_cups_after_cup1_labels in data:
            with self.subTest(input_cup_labels=input_cup_labels):
                self.assertEqual(
                    day_23_part_2.find_hiding_stars_cups_labels(input_cup_labels),
                    exp_cups_after_cup1_labels,
                )

    def test_solution(self):
        data = [
            ["input/day_23.txt", 21273394210],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_23_part_2.solution(input_file_rel_uri),
                    exp_solution,
                )
