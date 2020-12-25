import unittest

from aoc2020 import day_25_part_1


class TestDay25Part1(unittest.TestCase):
    def test_get_encryption_key_params(self):
        data = [
            [5764801, 17807724, (17807724, 8)],
            [17807724, 5764801, (17807724, 8)],
            [17807724, 5764802, (5764802, 11)],
        ]
        for public_key_1, public_key_2, exp_params in data:
            with self.subTest(public_key_1=public_key_1, public_key_2=public_key_2):
                self.assertEqual(
                    day_25_part_1.get_encryption_key_params(public_key_1, public_key_2),
                    exp_params,
                )

        exception_data = [
            [178077240, 178077241],
        ]
        for public_key_1, public_key_2 in exception_data:
            with self.subTest(public_key_1=public_key_1, public_key_2=public_key_2):
                with self.assertRaises(day_25_part_1.InvalidPublicKeyException):
                    day_25_part_1.get_encryption_key_params(public_key_1, public_key_2)

    def test_calculate_encryption_key(self):
        data = [
            [17807724, 8, 14897079],
            [5764801, 11, 14897079],
        ]
        for public_key, loop_size, exp_encryption_key in data:
            with self.subTest(public_key=public_key, loop_size=loop_size):
                self.assertEqual(
                    day_25_part_1.calculate_encryption_key(public_key, loop_size),
                    exp_encryption_key,
                )

    def test_solution(self):
        data = [
            ["input/day_25_example.txt", 14897079],
            ["input/day_25.txt", 3217885],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_25_part_1.solution(input_file_rel_uri), exp_solution
                )
