"""This presents all the models for  No Thanks Simulator"""

import random
from typing import List
from enum import Enum


def get_coins(num_players):
    """Function that determine the number of coins each player will have based
    on the number of players"""

    if num_players == 7:
        return 7
    elif num_players == 6:
        return 9
    else:
        return 11


class Status(Enum):
    """
    Enum of game status

    ROUND_BEGIN: A card was dispensed from the deck into table 
    PAID: Players are paying to avoid cards
    CARD_GOT: A player got a card
    """
    ROUND_BEGIN = 1
    PAID = 2
    CARD_GOT = 3


class Deck:
    """Class that represents a deck of cards in the game"""

    def __init__(self):
        self.cards = list(range(3, 36))
        self.dispensed_card = None
        self.coins = 0  # Number of coins in self.dispensed_card

    def dispense_card(self) -> int:
        """Dispense a card to be used in a round of the game"""
        random.shuffle(self.cards)
        popped = self.cards.pop(0)
        self.dispensed_card = popped

        # Returns the popped card to save calls to self.dispensed_card
        return popped

    def __repr__(self):
        return f"Deck(cards={self.cards})"


class Player:
    """Class that represents a player in the game"""

    def __init__(self, name: str):
        self.name = name
        self.coins = 0
        self.cards = []

    def get_card(self, deck: Deck) -> int:
        """Get a card instead of paying it"""
        self.cards.append(deck.dispensed_card)

        return Status.CARD_GOT

    def pay_card(self, deck: Deck) -> int:
        """Pay a card for not getting it"""

        # If no coins, player will get the card
        if self.coins == 0:
            self.get_card(deck)

        self.coins -= 1
        deck.coins += 1

        return Status.PAID

    def get_or_pay_card(self, deck: Deck) -> None:
        """A method that invoke get_card 30% of the time and pay_card
        otherwise, given the necessary quantity of coins"""
        choices = list(range(1, 10))
        choice = random.choice(choices)

        # 70% of the time try to pay, otherwise get the card
        status = self.pay_card(deck) if choice <= 7 else self.get_card(deck)

        return status

    def __repr__(self):
        return f"Player(name={self.name}, coins={self.coins})"


class Game:
    """Class that represents a game"""

    def __init__(self, deck: Deck, players: List[Player]):
        self.deck = deck
        self.players = players
        self.number = 1
        self.status = Status.ROUND_BEGIN
        self.get_coins()

    def play_until_pay(self):
        """Make players deal with a card until one of them pay for it"""

        for player in self.players:
            self.status = player.get_or_pay_card(self.deck)
            if self.status == Status.CARD_GOT:
                # New round
                self.number += 1
                self.status = Status.CARD_GOT
                break

    def get_coins(self) -> None:
        """Initialize self.coins for every player based on the number of
        players"""
        num_players = len(self.players)
        for player in self.players:
            player.coins = get_coins(num_players)
