import unittest

from aoc2020 import day_24_part_2


class TestDay24Part2(unittest.TestCase):
    def test_do_another_day(self):
        data = {
            "input/day_24_example.txt": [15, 12, 25, 14, 23, 28, 41, 37, 49, 37],
        }
        for input_file_rel_uri, exp_black_tile_count_per_day in data.items():
            (
                act_black_tiles_cordss,
                act_is_black_tile_per_coords,
            ) = day_24_part_2.prepare_initial_exhibit(input_file_rel_uri)
            for day, exp_black_tile_count in enumerate(exp_black_tile_count_per_day):
                with self.subTest(input_file_rel_uri=input_file_rel_uri, day=day):
                    day_24_part_2.do_another_day(
                        act_black_tiles_cordss, act_is_black_tile_per_coords
                    )
                    self.assertEqual(len(act_black_tiles_cordss), exp_black_tile_count)

    def test_solution(self):
        data = [
            ["input/day_24_example.txt", 2208],
            ["input/day_24.txt", 3955],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_24_part_2.solution(input_file_rel_uri), exp_solution
                )
