import unittest

from aoc2020 import day_14_part_2


class TestDay14Part2(unittest.TestCase):
    def test_decode_mask(self):
        data = [
            [
                42,
                "000000000000000000000000000000X1001X",
                "000000000000000000000000000000X1101X",
            ],
            [
                26,
                "00000000000000000000000000000000X0XX",
                "00000000000000000000000000000001X0XX",
            ],
        ]
        for instruction_address, mask, exp_decoded_mask in data:
            with self.subTest(address=instruction_address, mask=mask):
                self.assertEqual(
                    day_14_part_2.decode_mask(instruction_address, mask),
                    exp_decoded_mask,
                )

    def test_get_decoded_addresses(self):
        data = [
            ["000000000000000000000000000000X1101X", {26, 27, 58, 59}],
            ["00000000000000000000000000000001X0XX", {16, 17, 18, 19, 24, 25, 26, 27}],
        ]
        for decoded_mask, exp_decoded_addresses in data:
            with self.subTest(mask=decoded_mask):
                self.assertEqual(
                    day_14_part_2.get_decoded_addresses(decoded_mask),
                    exp_decoded_addresses,
                )

    def test_execute_instruction(self):
        instructions = [
            "mask = 000000000000000000000000000000X1001X",
            "mem[42] = 100",
            "mask = 00000000000000000000000000000000X0XX",
            "mem[26] = 1",
        ]
        act_mask, act_memory = None, {}
        exp_mask = "00000000000000000000000000000000X0XX"
        exp_memory = {
            16: 1,
            17: 1,
            18: 1,
            19: 1,
            24: 1,
            25: 1,
            26: 1,
            27: 1,
            58: 100,
            59: 100,
        }
        for instruction in instructions:
            act_mask, act_memory = day_14_part_2.execute_instruction(
                instruction, act_mask, act_memory
            )
        self.assertEqual(act_mask, exp_mask)
        self.assertEqual(act_memory, exp_memory)

    def test_solution(self):
        data = [
            ["input/day_14_example1.txt", 208],
            ["input/day_14.txt", 3296185383161],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_14_part_2.solution(input_file_rel_uri), exp_solution
                )
