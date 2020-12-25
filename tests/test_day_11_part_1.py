import unittest

from aoc2020 import day_11_part_1


class TestDay11Part1(unittest.TestCase):
    @staticmethod
    def layout_from_string(string):
        return [list(line) for line in string.strip().split("\n")]

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
                "#.LL.L#.##\n"
                "#LLLLLL.L#\n"
                "L.L.L..L..\n"
                "#LLL.LL.L#\n"
                "#.LL.LL.LL\n"
                "#.LLLL#.##\n"
                "..L.L.....\n"
                "#LLLLLLLL#\n"
                "#.LLLLLL.L\n"
                "#.#LLLL.##\n"
            ),
            (
                "#.##.L#.##\n"
                "#L###LL.L#\n"
                "L.#.#..#..\n"
                "#L##.##.L#\n"
                "#.##.LL.LL\n"
                "#.###L#.##\n"
                "..#.#.....\n"
                "#L######L#\n"
                "#.LL###L.L\n"
                "#.#L###.##\n"
            ),
            (
                "#.#L.L#.##\n"
                "#LLL#LL.L#\n"
                "L.L.L..#..\n"
                "#LLL.##.L#\n"
                "#.LL.LL.LL\n"
                "#.LL#L#.##\n"
                "..L.L.....\n"
                "#L#LLLL#L#\n"
                "#.LLLLLL.L\n"
                "#.#L#L#.##\n"
            ),
            (
                "#.#L.L#.##\n"
                "#LLL#LL.L#\n"
                "L.#.L..#..\n"
                "#L##.##.L#\n"
                "#.#L.LL.LL\n"
                "#.#L#L#.##\n"
                "..L.L.....\n"
                "#L#L##L#L#\n"
                "#.LLLLLL.L\n"
                "#.#L#L#.##\n"
            ),
        ]
        old_layout = self.layout_from_string(layout_strings[0])
        row_count, col_count = len(old_layout), len(old_layout[0])
        rem_layouts = (self.layout_from_string(string) for string in layout_strings[1:])
        for new_layout in rem_layouts:
            self.assertEqual(
                day_11_part_1.apply_rules(old_layout, row_count, col_count), new_layout
            )
            old_layout = new_layout

    def test_solution(self):
        data = [
            ["input/day_11_example.txt", 37],
            ["input/day_11.txt", 2247],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_11_part_1.solution(input_file_rel_uri), exp_solution
                )
