import unittest

from aoc2020 import day_11_part_2


class TestDay11Part2(unittest.TestCase):
    @staticmethod
    def layout_from_string(string):
        return [list(line) for line in string.strip().split("\n")]

    def test_get_surrounding_seats(self):
        data = [
            [
                ".......#.\n"
                "...#.....\n"
                ".#.......\n"
                ".........\n"
                "..#L....#\n"
                "....#....\n"
                ".........\n"
                "#........\n"
                "...#.....\n",
                (4, 3),
                ["#", "#", "#", "#", "#", "#", "#", "#"],
            ],
            [
                ".............\n"  # dummy comment to counter Black formatting
                ".L.L.#.#.#.#.\n"
                ".............\n",
                (1, 1),
                ["L"],
            ],
            [
                ".##.##.\n"
                "#.#.#.#\n"
                "##...##\n"
                "...L...\n"
                "##...##\n"
                "#.#.#.#\n"
                ".##.##.\n",
                (3, 3),
                [],
            ],
        ]
        for subtest_index, (
            layout_string,
            (row_index, col_index),
            exp_surrounding_seats,
        ) in enumerate(data):
            with self.subTest(subtest_index=subtest_index):
                layout = self.layout_from_string(layout_string)
                row_count, col_count = len(layout), len(layout[0])
                self.assertEqual(
                    day_11_part_2.get_surrounding_seats(
                        row_index, col_index, layout, row_count, col_count
                    ),
                    exp_surrounding_seats,
                )

    def test_apply_rules(self):
        layout_strings = [
            (
                "L.LL.LL.LL\n"
                "LLLLLLL.LL\n"
                "L.L.L..L..\n"
                "LLLL.LL.LL\n"
                "L.LL.LL.LL\n"
                "L.LLLLL.LL\n"
                "..L.L.....\n"
                "LLLLLLLLLL\n"
                "L.LLLLLL.L\n"
                "L.LLLLL.LL\n"
            ),
            (
                "#.##.##.##\n"
                "#######.##\n"
                "#.#.#..#..\n"
                "####.##.##\n"
                "#.##.##.##\n"
                "#.#####.##\n"
                "..#.#.....\n"
                "##########\n"
                "#.######.#\n"
                "#.#####.##\n"
            ),
            (
                "#.LL.LL.L#\n"
                "#LLLLLL.LL\n"
                "L.L.L..L..\n"
                "LLLL.LL.LL\n"
                "L.LL.LL.LL\n"
                "L.LLLLL.LL\n"
                "..L.L.....\n"
                "LLLLLLLLL#\n"
                "#.LLLLLL.L\n"
                "#.LLLLL.L#\n"
            ),
            (
                "#.L#.##.L#\n"
                "#L#####.LL\n"
                "L.#.#..#..\n"
                "##L#.##.##\n"
                "#.##.#L.##\n"
                "#.#####.#L\n"
                "..#.#.....\n"
                "LLL####LL#\n"
                "#.L#####.L\n"
                "#.L####.L#\n"
            ),
            (
                "#.L#.L#.L#\n"
                "#LLLLLL.LL\n"
                "L.L.L..#..\n"
                "##LL.LL.L#\n"
                "L.LL.LL.L#\n"
                "#.LLLLL.LL\n"
                "..L.L.....\n"
                "LLLLLLLLL#\n"
                "#.LLLLL#.L\n"
                "#.L#LL#.L#\n"
            ),
            (
                "#.L#.L#.L#\n"
                "#LLLLLL.LL\n"
                "L.L.L..#..\n"
                "##L#.#L.L#\n"
                "L.L#.#L.L#\n"
                "#.L####.LL\n"
                "..#.#.....\n"
                "LLL###LLL#\n"
                "#.LLLLL#.L\n"
                "#.L#LL#.L#\n"
            ),
            (
                "#.L#.L#.L#\n"
                "#LLLLLL.LL\n"
                "L.L.L..#..\n"
                "##L#.#L.L#\n"
                "L.L#.LL.L#\n"
                "#.LLLL#.LL\n"
                "..#.L.....\n"
                "LLL###LLL#\n"
                "#.LLLLL#.L\n"
                "#.L#LL#.L#\n"
            ),
        ]
        old_layout = self.layout_from_string(layout_strings[0])
        row_count, col_count = len(old_layout), len(old_layout[0])
        rem_layouts = (self.layout_from_string(string) for string in layout_strings[1:])
        for new_layout in rem_layouts:
            self.assertEqual(
                day_11_part_2.apply_rules(old_layout, row_count, col_count), new_layout
            )
            old_layout = new_layout

    def test_solution(self):
        data = [
            ["input/day_11_example.txt", 26],
            ["input/day_11.txt", 2011],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_11_part_2.solution(input_file_rel_uri), exp_solution
                )
