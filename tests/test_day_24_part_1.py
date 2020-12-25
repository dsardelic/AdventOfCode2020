import unittest

from aoc2020 import day_24_part_1


class TestDay24Part1(unittest.TestCase):
    def test_parse_directions(self):
        data = [
            ["esenee", ["e", "se", "ne", "e"]],
        ]
        for tile_identifier, exp_directions in data:
            with self.subTest(tile_identifier=tile_identifier):
                self.assertEqual(
                    day_24_part_1.parse_directions(tile_identifier), exp_directions
                )

    def test_get_tile_coordinates(self):
        data = [
            ["esew", (1, -1)],
            ["nwwswee", (0, 0)],
        ]
        for tile_identifier, exp_tile_coordinates in data:
            with self.subTest(tile_identifier=tile_identifier):
                self.assertEqual(
                    day_24_part_1.get_tile_coordinates(tile_identifier),
                    exp_tile_coordinates,
                )

    def test_solution(self):
        data = [
            ["input/day_24_example.txt", 10],
            ["input/day_24.txt", 434],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_24_part_1.solution(input_file_rel_uri), exp_solution
                )
