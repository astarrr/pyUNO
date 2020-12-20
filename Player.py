class Player:
    def __init__(self, nickname, cards):
        self.nickname = nickname
        self.cards = cards

    def add_card(self, card):
        self.cards = self.cards + [card]

    def print_cards(self):
        for i, card in zip(range(1, len(self.cards) + 1), self.cards):
            print("[{}] {}".format(i, card.print()))
