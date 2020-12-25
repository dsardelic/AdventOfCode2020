import unittest

from aoc2020 import day_16_part_2


class TestDay16Part2(unittest.TestCase):
    def test_find_valid_tickets(self):
        data = [
            [
                ((3, 9, 18), (15, 1, 5), (5, 14, 9)),
                {
                    "class": (range(0, 2), range(4, 20)),
                    "row": (range(0, 6), range(8, 20)),
                    "seat": (range(0, 14), range(16, 20)),
                },
                ((3, 9, 18), (15, 1, 5), (5, 14, 9)),
            ],
            [
                ((7, 3, 47), (40, 4, 50), (55, 2, 20), (38, 6, 12)),
                {
                    "class": (range(1, 4), range(5, 8)),
                    "row": (range(6, 12), range(33, 45)),
                    "seat": (range(13, 41), range(45, 51)),
                },
                ((7, 3, 47),),
            ],
        ]
        for fixture_index, (
            tickets,
            allowed_ranges_per_field,
            exp_valid_tickets,
        ) in enumerate(data):
            with self.subTest(fixture_index=fixture_index):
                self.assertEqual(
                    day_16_part_2.find_valid_tickets(tickets, allowed_ranges_per_field),
                    exp_valid_tickets,
                )

    def test_field_ordering(self):
        data = [
            [
                ((3, 9, 18), (15, 1, 5), (5, 14, 9)),
                {
                    "class": (range(0, 2), range(4, 20)),
                    "row": (range(0, 6), range(8, 20)),
                    "seat": (range(0, 14), range(16, 20)),
                },
                {0: "row", 1: "class", 2: "seat"},
            ],
            [
                ((7, 3, 47),),
                {
                    "class": (range(1, 4), range(5, 8)),
                    "row": (range(6, 12), range(33, 45)),
                    "seat": (range(13, 41), range(45, 51)),
                },
                {0: "row", 1: "class", 2: "seat"},
            ],
        ]
        for fixture_index, (
            valid_tickets,
            allowed_ranges_per_field,
            exp_field_ordering,
        ) in enumerate(data):
            with self.subTest(fixture_index=fixture_index):
                self.assertEqual(
                    day_16_part_2.field_ordering(
                        valid_tickets, allowed_ranges_per_field
                    ),
                    exp_field_ordering,
                )

    def test_solution(self):
        data = [
            ["input/day_16_example.txt", 1],
            ["input/day_16_example1.txt", 1],
            ["input/day_16.txt", 1001849322119],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_16_part_2.solution(input_file_rel_uri), exp_solution
                )
