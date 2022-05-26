"""This is the main.py of No Thanks Simulator"""

from models import Deck, Player, Game
from errors import WrongNumberOfPlayers
from typing import List



class GameManager:
    """A class that runs the game"""

    def __init__(self, deck: Deck, players: List[Player]):
        # Check if number of players is correct
        if len(players) > 7 or len(players) < 3:
            raise WrongNumberOfPlayers(len(players))
        self.game = Game(deck, players)

    def play(self):
        """Starts the game"""

        # TODO: create play method


def main():
    """Runs the program"""
    deck = Deck()
    players = [
        Player(name="André"),
        Player(name="Monalise"),
        Player(name="Sansão"),
        Player(name="Gleiciane")
    ]

    gamemanager = GameManager(deck, players)
    gamemanager.get_coins()
    gamemanager.play()


if __name__ == "__main__":
    main()
