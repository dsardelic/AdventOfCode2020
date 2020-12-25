import unittest

from aoc2020 import day_09_part_1


class TestDay09Part1(unittest.TestCase):
    def test_get_weak_element(self):
        input_rel_uri = "input/day_09_example.txt"
        data = [
            [[26], 25, None],
            [[49], 25, None],
            [[100], 25, 100],
            [[50], 25, 50],
            [[45, 26], 25, None],
            [[45, 65], 25, 65],
            [[45, 64], 25, None],
            [[45, 66], 25, None],
        ]
        with open(input_rel_uri) as ifile:
            stream = [int(line.strip()) for line in ifile.readlines()]
        for suffix, preamble_size, exp_weak_element in data:
            with self.subTest(input_file=input_rel_uri, suffix=suffix):
                self.assertEqual(
                    day_09_part_1.get_weak_element(stream + suffix, preamble_size),
                    exp_weak_element,
                )

    def test_solution(self):
        data = [
            ["input/day_09_example.txt", 25, None],
            ["input/day_09_example1.txt", 5, 127],
            ["input/day_09.txt", 25, 1721308972],
        ]
        for input_file_rel_uri, preamble_size, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_09_part_1.solution(input_file_rel_uri, preamble_size),
                    exp_solution,
                )
