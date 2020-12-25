import unittest
from collections import deque

from aoc2020 import day_22_part_1


class TestDay22Part1(unittest.TestCase):
    def test_play_round(self):
        data = [
            [deque([9, 2, 6, 3, 1]), deque([5, 8, 4, 7, 10])],
            [deque([2, 6, 3, 1, 9, 5]), deque([8, 4, 7, 10])],
            [deque([6, 3, 1, 9, 5]), deque([4, 7, 10, 8, 2])],
            [deque([3, 1, 9, 5, 6, 4]), deque([7, 10, 8, 2])],
            [deque([1, 9, 5, 6, 4]), deque([10, 8, 2, 7, 3])],
        ]
        player1_card_values, player2_card_values = data[0]
        for exp_player1_card_values, exp_player2_card_values in data[1:]:
            with self.subTest(
                player1_card_values=player1_card_values,
                player2_card_values=player2_card_values,
            ):
                self.assertEqual(
                    day_22_part_1.play_round(player1_card_values, player2_card_values),
                    (exp_player1_card_values, exp_player2_card_values),
                )
                player1_card_values = exp_player1_card_values
                player2_card_values = exp_player2_card_values

        data = [
            [deque([5, 4, 1]), deque([8, 9, 7, 3, 2, 10, 6])],
            [deque([4, 1]), deque([9, 7, 3, 2, 10, 6, 8, 5])],
            [deque([1]), deque([7, 3, 2, 10, 6, 8, 5, 9, 4])],
            [deque([]), deque([3, 2, 10, 6, 8, 5, 9, 4, 7, 1])],
        ]
        player1_card_values, player2_card_values = data[0]
        for exp_player1_card_values, exp_player2_card_values in data[1:]:
            with self.subTest(
                player1_card_values=player1_card_values,
                player2_card_values=player2_card_values,
            ):
                self.assertEqual(
                    day_22_part_1.play_round(player1_card_values, player2_card_values),
                    (exp_player1_card_values, exp_player2_card_values),
                )
                player1_card_values = exp_player1_card_values
                player2_card_values = exp_player2_card_values

    def test_get_final_card_values(self):
        data = [
            [
                deque([9, 2, 6, 3, 1]),
                deque([5, 8, 4, 7, 10]),
                deque([3, 2, 10, 6, 8, 5, 9, 4, 7, 1]),
            ],
        ]
        for player1_card_values, player2_card_values, exp_final_card_sequence in data:
            with self.subTest(
                player1_card_values=player1_card_values,
                player2_card_values=player2_card_values,
            ):
                self.assertEqual(
                    day_22_part_1.get_final_card_values(
                        player1_card_values, player2_card_values
                    ),
                    exp_final_card_sequence,
                )

    def test_score(self):
        data = [
            [deque([3, 2, 10, 6, 8, 5, 9, 4, 7, 1]), 306],
        ]
        for card_values, exp_score in data:
            with self.subTest(card_values=card_values):
                self.assertEqual(day_22_part_1.score(card_values), exp_score)

    def test_solution(self):
        data = [
            ["input/day_22_example.txt", 306],
            ["input/day_22.txt", 31629],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_22_part_1.solution(input_file_rel_uri), exp_solution
                )
