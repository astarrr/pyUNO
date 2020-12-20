import requests
from Player import Player

import socketio

sio = socketio.Client()


def generate_players():
    players = []

    angelo = Player("Angelo", [])
    corrado = Player("Corrado", [])

    players.append(angelo)
    players.append(corrado)

    return players


def on_connection_response(nickname):
    print(nickname + " connected.")


if __name__ == '__main__':
    print("Insert your nickname: ")

    # nickname = str(input())
    nickname = "Angelo"

    # player = Player(nickname, [])

    sio.connect("http://localhost:5000", namespaces=["/chat"])

    data = {
        "nickname": nickname,
        "room": "test",
    }
    sio.emit("join", data, namespace="/chat")


    sio.wait()

    # for i in range(7):
    #     for player in players:
    #         player.add_card(cards.pop())
    #
    # deck = [cards.pop()]
    #
    # print(deck[0].print())
    # print()
    #
    # players[0].print_cards()
    #
    # print("Select [card] to play or [draw] a card: ")
    # input = int(input())
    #
    # if is_card_playable(deck[0], players[0].cards[input - 1]):
    #     print("ok")
    # else:
    #     print("no")
