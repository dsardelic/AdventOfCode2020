import unittest

from aoc2020 import day_16_part_1


class TestDay16Part1(unittest.TestCase):
    def test_is_invalid_value(self):
        data = [
            [
                [
                    range(1, 4),
                    range(5, 8),
                    range(6, 12),
                    range(33, 45),
                    range(13, 41),
                    range(45, 51),
                ],
                [
                    (7, False),
                    (1, False),
                    (14, False),
                    (7, False),
                    (3, False),
                    (47, False),
                    (40, False),
                    (4, True),
                    (50, False),
                    (55, True),
                    (2, False),
                    (20, False),
                    (38, False),
                    (6, False),
                    (12, True),
                ],
            ],
        ]
        for fixture_index, (ranges, subfixture) in enumerate(data):
            for value, exp_is_invalid in subfixture:
                with self.subTest(fixture_index=fixture_index, value=value):
                    self.assertEqual(
                        day_16_part_1.is_invalid_value(value, ranges), exp_is_invalid
                    )

    def test_solution(self):
        data = [
            ["input/day_16_example.txt", 71],
            ["input/day_16.txt", 28884],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_16_part_1.solution(input_file_rel_uri), exp_solution
                )
