class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def print(self):
        return "{} {}".format(self.value, self.color)
