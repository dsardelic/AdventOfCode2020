import unittest

from aoc2020 import day_14_part_1


class TestDay14Part1(unittest.TestCase):
    def test_apply_mask(self):
        data = [
            [11, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", 73],
            [101, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", 101],
            [0, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", 64],
        ]
        for value, mask, exp_result in data:
            with self.subTest(value=value, mask=mask):
                self.assertEqual(day_14_part_1.apply_mask(mask, value), exp_result)

    def test_write_to_memory(self):
        instructions = ["mem[8] = 11", "mem[7] = 101", "mem[8] = 0"]
        mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
        act_memory = {}
        exp_memory = {7: 101, 8: 64}
        for instruction in instructions:
            day_14_part_1.write_to_memory(instruction, mask, act_memory)
        self.assertEqual(act_memory, exp_memory)

    def test_solution(self):
        data = [
            ["input/day_14_example.txt", 165],
            ["input/day_14.txt", 14862056079561],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_14_part_1.solution(input_file_rel_uri), exp_solution
                )
