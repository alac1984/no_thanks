"""This is the main.py of No Thanks Simulator"""

from models import Deck, Player, Game


def main():
    """Runs the program"""
    deck = Deck()
    players = [
        Player(name="André"),
        Player(name="Monalise"),
        Player(name="Sansão"),
        Player(name="Gleiciane")
    ]

    game = Game(deck, players)
    game.run_game()


if __name__ == "__main__":
    main()
