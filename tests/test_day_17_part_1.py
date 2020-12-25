import itertools
import unittest

from aoc2020 import day_17_part_1


class TestDay17Part1(unittest.TestCase):
    def test_apply_rules(self):
        def parse_plane(string):
            return [list(token) for token in string.strip().split("\n")]

        def trim_space(space):
            def plane_limits(plane):
                min_row_index, max_row_index, min_col_index, max_col_index = (
                    float("inf"),
                    -1,
                    float("inf"),
                    -1,
                )
                for row_index, row in enumerate(plane):
                    for col_index, state in enumerate(row):
                        if state == "#":
                            if min_row_index == -1:
                                min_row_index = row_index
                            min_row_index = min(row_index, min_row_index)
                            if min_col_index == -1:
                                min_col_index = col_index
                            min_col_index = min(col_index, min_col_index)
                            max_row_index = max(row_index, max_row_index)
                            max_col_index = max(col_index, max_col_index)
                return min_row_index, max_row_index, min_col_index, max_col_index

            reduced_space = [
                plane
                for plane in space
                if not all(
                    status == "." for status in itertools.chain.from_iterable(plane)
                )
            ]
            min_row_indices, max_row_indices, min_col_indices, max_col_indices = list(
                zip(*[plane_limits(plane) for plane in reduced_space])
            )
            min_row_index, max_row_index = min(min_row_indices), max(max_row_indices)
            min_col_index, max_col_index = min(min_col_indices), max(max_col_indices)
            return [
                "\n".join(
                    [
                        "".join(row[min_col_index : max_col_index + 1])
                        for row in plane[min_row_index : max_row_index + 1]
                    ]
                )
                + "\n"
                for plane in reduced_space
            ]

        act_significant_space = [
            parse_plane(
                ".#.\n"  # a much longer dummy comment to prevent Black autoformatting
                "..#\n"
                "###\n"
            )
        ]
        trimmed_exp_significant_spaces = [
            [
                (
                    "#..\n"  # dummy comment to prevent Black autoformatting
                    "..#\n"
                    ".#.\n"
                ),
                (
                    "#.#\n"  # dummy comment to prevent Black autoformatting
                    ".##\n"
                    ".#.\n"
                ),
                (
                    "#..\n"  # dummy comment to prevent Black autoformatting
                    "..#\n"
                    ".#.\n"
                ),
            ],
            [
                (
                    ".....\n"  # dummy comment to prevent Black autoformatting
                    ".....\n"
                    "..#..\n"
                    ".....\n"
                    ".....\n"
                ),
                (
                    "..#..\n"  # dummy comment to prevent Black autoformatting
                    ".#..#\n"
                    "....#\n"
                    ".#...\n"
                    ".....\n"
                ),
                (
                    "##...\n"  # dummy comment to prevent Black autoformatting
                    "##...\n"
                    "#....\n"
                    "....#\n"
                    ".###.\n"
                ),
                (
                    "..#..\n"  # dummy comment to prevent Black autoformatting
                    ".#..#\n"
                    "....#\n"
                    ".#...\n"
                    ".....\n"
                ),
                (
                    ".....\n"  # dummy comment to prevent Black autoformatting
                    ".....\n"
                    "..#..\n"
                    ".....\n"
                    ".....\n"
                ),
            ],
            [
                (
                    ".......\n"
                    ".......\n"
                    "..##...\n"
                    "..###..\n"
                    ".......\n"
                    ".......\n"
                    ".......\n"
                ),
                (
                    "..#....\n"
                    "...#...\n"
                    "#......\n"
                    ".....##\n"
                    ".#...#.\n"
                    "..#.#..\n"
                    "...#...\n"
                ),
                (
                    "...#...\n"
                    ".......\n"
                    "#......\n"
                    ".......\n"
                    ".....##\n"
                    ".##.#..\n"
                    "...#...\n"
                ),
                (
                    "..#....\n"
                    "...#...\n"
                    "#......\n"
                    ".....##\n"
                    ".#...#.\n"
                    "..#.#..\n"
                    "...#...\n"
                ),
                (
                    ".......\n"
                    ".......\n"
                    "..##...\n"
                    "..###..\n"
                    ".......\n"
                    ".......\n"
                    ".......\n"
                ),
            ],
        ]
        for fixture_index, trimmed_exp_significant_space in enumerate(
            trimmed_exp_significant_spaces
        ):
            with self.subTest(fixture_index=fixture_index):
                act_significant_space = day_17_part_1.apply_rules(act_significant_space)
                self.assertEqual(
                    trim_space(act_significant_space), trimmed_exp_significant_space
                )

    def test_solution(self):
        data = [
            ["input/day_17_example.txt", 112],
            ["input/day_17.txt", 401],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_17_part_1.solution(input_file_rel_uri), exp_solution
                )
