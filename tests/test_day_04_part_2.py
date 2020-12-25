import unittest

from aoc2020 import day_04_part_2


class TestDay04Part2(unittest.TestCase):
    def test_password_has_all_required_fields(self):
        data = [
            [
                {
                    "ecl": "gry",
                    "pid": "860033327",
                    "eyr": "2020",
                    "hcl": "#fffffd",
                    "byr": "1937",
                    "iyr": "2017",
                    "cid": "147",
                    "hgt": "183cm",
                },
                True,
            ],
            [
                {
                    "iyr": "2013",
                    "ecl": "amb",
                    "cid": "350",
                    "eyr": "2023",
                    "pid": "028048884",
                    "hcl": "#cfa07d",
                    "byr": "1929",
                },
                False,
            ],
            [
                {
                    "hcl": "#ae17e1",
                    "iyr": "2013",
                    "eyr": "2024",
                    "ecl": "brn",
                    "pid": "760753108",
                    "byr": "1931",
                    "hgt": "179cm",
                },
                True,
            ],
            [
                {
                    "hcl": "#cfa07d",
                    "eyr": "2025",
                    "pid": "166559648",
                    "iyr": "2011",
                    "ecl": "brn",
                    "hgt": "59in",
                },
                False,
            ],
        ]
        for password, is_valid in data:
            with self.subTest(password=password.keys()):
                self.assertEqual(
                    day_04_part_2.password_has_all_required_fields(password), is_valid
                )

    def test_is_valid_byr(self):
        data = [
            ["2002", True],
            ["2003", False],
        ]
        for byr, is_valid in data:
            with self.subTest(byr=byr):
                act_result = day_04_part_2.is_valid_byr(byr)
                # testing truthiness will suffice
                if is_valid:
                    self.assertTrue(act_result)
                else:
                    self.assertFalse(act_result)

    def test_is_valid_hgt(self):
        data = [
            ["60in", True],
            ["190cm", True],
            ["190in", False],
            ["190", False],
        ]
        for hgt, is_valid in data:
            with self.subTest(hgt=hgt):
                act_result = day_04_part_2.is_valid_hgt(hgt)
                if is_valid:
                    self.assertTrue(act_result)
                else:
                    self.assertFalse(act_result)

    def test_is_valid_hcl(self):
        data = [
            ["#123abc", True],
            ["#123abz", False],
            ["123abc", False],
        ]
        for hcl, is_valid in data:
            with self.subTest(hcl=hcl):
                act_result = day_04_part_2.is_valid_hcl(hcl)
                if is_valid:
                    self.assertTrue(act_result)
                else:
                    self.assertFalse(act_result)

    def test_is_valid_ecl(self):
        data = [
            ["brn", True],
            ["wat", False],
        ]
        for ecl, is_valid in data:
            with self.subTest(ecl=ecl):
                self.assertEqual(day_04_part_2.is_valid_ecl(ecl), is_valid)

    def test_is_valid_pid(self):
        data = [
            ["000000001", True],
            ["0123456789", False],
        ]
        for pid, is_valid in data:
            with self.subTest(pid=pid):
                act_result = day_04_part_2.is_valid_pid(pid)
                if is_valid:
                    self.assertTrue(act_result)
                else:
                    self.assertFalse(act_result)

    def test_solution(self):
        data = [
            ["input/day_04_example.txt", 2],
            ["input/day_04_example1.txt", 0],
            ["input/day_04_example2.txt", 4],
            ["input/day_04.txt", 158],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_04_part_2.solution(input_file_rel_uri), exp_solution
                )
