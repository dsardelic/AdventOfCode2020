import collections


def play_round(player1_card_values, player2_card_values):
    player1_card = player1_card_values.popleft()
    player2_card = player2_card_values.popleft()
    # assert player1_card != player2_card
    if (
        len(player1_card_values) >= player1_card
        and len(player2_card_values) >= player2_card
    ):
        if subgame_winner_is_player1(
            collections.deque(list(player1_card_values)[:player1_card]),
            collections.deque(list(player2_card_values)[:player2_card]),
        ):
            player1_card_values.extend([player1_card, player2_card])
        else:
            player2_card_values.extend([player2_card, player1_card])
    elif player1_card > player2_card:
        player1_card_values.extend([player1_card, player2_card])
    else:
        player2_card_values.extend([player2_card, player1_card])
    return player1_card_values, player2_card_values


def subgame_winner_is_player1(player1_card_values, player2_card_values):
    prev_cards_setups = set()
    while player1_card_values and player2_card_values:
        if (
            tuple(player1_card_values),
            tuple(player2_card_values),
        ) in prev_cards_setups:
            return True
        prev_cards_setups.add((tuple(player1_card_values), tuple(player2_card_values)))
        player1_card_values, player2_card_values = play_round(
            player1_card_values, player2_card_values
        )
    if player1_card_values:
        return True
    return False


def get_final_card_values(player1_card_values, player2_card_values):
    while player1_card_values and player2_card_values:
        player1_card_values, player2_card_values = play_round(
            player1_card_values, player2_card_values
        )
    if player1_card_values:
        return player1_card_values
    return player2_card_values


def score(card_values):
    return sum(
        card_index * card_value
        for card_index, card_value in enumerate(tuple(card_values)[::-1], 1)
    )


def solution(input_rel_uri):
    with open(input_rel_uri) as ifile:
        player_cards_data = ifile.read().strip().split("\n\n")
    players_card_values = [
        collections.deque(int(card) for card in player_cards_data_group.split("\n")[1:])
        for player_cards_data_group in player_cards_data
    ]
    return score(get_final_card_values(*players_card_values))


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))
