import unittest
from collections import deque

from aoc2020 import day_22_part_2


class TestDay22Part2(unittest.TestCase):
    def test_play_round(self):
        data = [
            [
                [deque([9, 2, 6, 3, 1]), deque([5, 8, 4, 7, 10])],
                [deque([2, 6, 3, 1, 9, 5]), deque([8, 4, 7, 10])],
                [deque([6, 3, 1, 9, 5]), deque([4, 7, 10, 8, 2])],
                [deque([3, 1, 9, 5, 6, 4]), deque([7, 10, 8, 2])],
                [deque([1, 9, 5, 6, 4]), deque([10, 8, 2, 7, 3])],
                [deque([9, 5, 6, 4]), deque([8, 2, 7, 3, 10, 1])],
                [deque([5, 6, 4, 9, 8]), deque([2, 7, 3, 10, 1])],
                [deque([6, 4, 9, 8, 5, 2]), deque([7, 3, 10, 1])],
                [deque([4, 9, 8, 5, 2]), deque([3, 10, 1, 7, 6])],
                [deque([9, 8, 5, 2]), deque([10, 1, 7, 6, 3, 4])],
                [deque([8, 5, 2]), deque([1, 7, 6, 3, 4, 10, 9])],
                [deque([5, 2, 8, 1]), deque([7, 6, 3, 4, 10, 9])],
                [deque([2, 8, 1]), deque([6, 3, 4, 10, 9, 7, 5])],
                [deque([8, 1]), deque([3, 4, 10, 9, 7, 5, 6, 2])],
                [deque([1, 8, 3]), deque([4, 10, 9, 7, 5, 6, 2])],
                [deque([8, 3]), deque([10, 9, 7, 5, 6, 2, 4, 1])],
                [deque([3]), deque([9, 7, 5, 6, 2, 4, 1, 10, 8])],
                [deque([]), deque([7, 5, 6, 2, 4, 1, 10, 8, 9, 3])],
            ],
            [
                [deque([9, 8, 5, 2]), deque([10, 1, 7])],
                [deque([8, 5, 2]), deque([1, 7, 10, 9])],
                [deque([5, 2, 8, 1]), deque([7, 10, 9])],
                [deque([2, 8, 1]), deque([10, 9, 7, 5])],
                [deque([8, 1]), deque([9, 7, 5, 10, 2])],
                [deque([1]), deque([7, 5, 10, 2, 9, 8])],
                [deque([]), deque([5, 10, 2, 9, 8, 7, 1])],
            ],
            [
                [deque([8, 1]), deque([3, 4, 10, 9, 7, 5])],
                [deque([1, 8, 3]), deque([4, 10, 9, 7, 5])],
                [deque([8, 3]), deque([10, 9, 7, 5, 4, 1])],
                [deque([3]), deque([9, 7, 5, 4, 1, 10, 8])],
                [deque([]), deque([7, 5, 4, 1, 10, 8, 9, 3])],
            ],
            [
                [deque([8]), deque([10, 9, 7, 5])],
                [deque([]), deque([9, 7, 5, 10, 8])],
            ],
        ]
        for round_sequence_index, round_sequence in enumerate(data):
            player1_card_values, player2_card_values = round_sequence[0]
            for exp_player1_card_values, exp_player2_card_values in round_sequence[1:]:
                with self.subTest(
                    round_sequence_index=round_sequence_index,
                    player1_card_values=player1_card_values,
                    player2_card_values=player2_card_values,
                ):
                    self.assertEqual(
                        day_22_part_2.play_round(
                            player1_card_values, player2_card_values
                        ),
                        (exp_player1_card_values, exp_player2_card_values),
                    )
                    player1_card_values = exp_player1_card_values
                    player2_card_values = exp_player2_card_values

    def test_subgame_winner_is_player1(self):
        data = [
            [deque([9, 2, 6, 3, 1]), deque([5, 8, 4, 7, 10]), False],
            [deque([9, 8, 5, 2]), deque([10, 1, 7]), False],
            [deque([8, 1]), deque([3, 4, 10, 9, 7, 5]), False],
            [deque([8]), deque([10, 9, 7, 5]), False],
        ]
        for (
            player1_card_values,
            player2_card_values,
            exp_subgame_winner_is_player1,
        ) in data:
            with self.subTest(
                player1_card_values=player1_card_values,
                player2_card_values=player2_card_values,
            ):
                self.assertEqual(
                    day_22_part_2.subgame_winner_is_player1(
                        player1_card_values, player2_card_values
                    ),
                    exp_subgame_winner_is_player1,
                )

    def test_solution(self):
        data = [
            ["input/day_22_example.txt", 291],
            ["input/day_22.txt", 35196],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_22_part_2.solution(input_file_rel_uri), exp_solution
                )
