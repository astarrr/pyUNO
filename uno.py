import random
from Card import Card
from Player import Player

colors = ["green", "yellow", "red", "blue"]


def is_card_playable(deck_card, player_card):
    if player_card.color == 'black':
        return True
    if deck_card.value == player_card.value:
        return True
    if deck_card.color == player_card.color:
        return True
    return False


def generate_cards():
    """ Generates, shuffles and return 112 UNO cards."""

    cards = []

    for color in colors:
        # 0 to 9
        for _ in range(2):
            for i in range(10):
                cards.append(Card(i, color))

        for _ in range(2):
            cards.append(Card("stop", color))

        for _ in range(2):
            cards.append(Card("turn", color))

        for _ in range(2):
            cards.append(Card("+2", color))

    for _ in range(4):
        cards.append(Card("change color", "black"))

    for _ in range(4):
        cards.append(Card("+4", "black"))

    random.shuffle(cards)

    return cards
