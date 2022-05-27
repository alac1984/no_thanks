class Error(Exception):
    # TODO: docstring

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class WrongNumberOfPlayers(Error):

    def __init__(self):
        self.message = "This game can be player only by 3 to 7 players"
        super().__init__(self.message)


class DeckOutOfCards(Error):
    def __init__(self):
        self.message = "This deck is empty"
        super().__init__(self.message)
     
