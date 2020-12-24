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
    """ Generate, shuffle and return 112 UNO cards."""

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


def play_card(card, cards, current_player, players):
    next_player = players[players.index(current_player) + 1 % len(players)]

    if card.value == '+2':
        next_player.add_card(cards.pop())
        next_player.add_card(cards.pop())

    if card.value == '+4':
        next_player.add_card(cards.pop())
        next_player.add_card(cards.pop())
        next_player.add_card(cards.pop())
        next_player.add_card(cards.pop())

    #if discarded.value == 'turn':
    #if discarded.value == 'stop':

    if card.value == 'change color':
        color = ''

        while color not in colors:
            print("Type color: ")
            color = input()

        game_color = color


if __name__ == '__main__':
    cards = generate_cards()

    players = []

    angelo = Player('angelo', [], 0)
    players.append(angelo)

    marco = Player('marco', [], 1)
    players.append(marco)

    for _ in range(7):
        for player in players:
            player.add_card(cards.pop())

    discarded = cards.pop()
    game_color = discarded.color

    turn = 0

    current_player = players[0]

    while len(angelo.cards) > 0:
        print('Card: ', discarded.print())

        angelo.print_cards()
        print("Play your card or type [draw]: ")
        choice = input()

        if choice == "draw":
            current_player.add_card(cards.pop())
        else:
            choice = int(choice)
            played_card = angelo.cards[choice - 1]

            if is_card_playable(discarded, played_card):
                play_card(discarded, cards, current_player, players)

                angelo.cards.pop(choice - 1)
                discarded = played_card
            else:
                print("You can't play that card.")
