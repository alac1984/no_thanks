"""A module for testing all models.py methods"""

from models import Deck, Player, Game


def test_deck_number_of_cards(game):
    """Assert if a Deck object has the right number of cards"""

    assert len(game.deck.cards) == 33


def test_deck_dispense_card(game):
    """Assert if a Deck object can dispense a card"""

    game.deck.dispense_card()
    assert game.deck.dispensed_card is not None


def test_deck_dispense_card_pop(game):
    """Assert if a dispensed card is popped from its list"""

    card = game.deck.dispense_card()
    assert card not in game.deck.cards


def test_deck_dispense_card_two_dispenses(game):
    """Check if two dispense_card calls in a row erase the first self.card
    correctly"""

    game.deck.dispense_card()
    card2 = game.deck.dispense_card()
    assert game.deck.dispensed_card == card2


def test_player_get_card(game):
    """Check if get_card is getting a card and storing its value in
    player.cards"""

    game.deck.dispensed_card = 4
    game.players[0].get_card(game.deck)

    assert 4 in game.players[0].cards


def test_player_pay_card(game):
    """Check if method pay card update player.coins correctly"""

    game.deck.dispense_card()
    game.players[0].pay_card(game.deck)
    assert game.players[0].coins == 8


def test_player_pay_card_deck_coins(game):
    """Check if when a player pays for a card, deck coins increase"""
    game.deck.dispense_card()
    game.players[0].pay_card(game.deck)
    assert game.deck.coins == 1


def test_player_pay_card_without_coins(game):
    """Check that method pay_card, when invoked by a player with no coins make
    it get the card"""

    game.deck.dispense_card()
    card = game.deck.dispensed_card
    game.players[0].coins = 0
    game.players[0].pay_card(game.deck)
    assert card in game.players[0].cards


def test_player_get_or_pay_card(game):
    """Check if pay option is under 70% appearance, given sufficient coins"""

    game.deck.cards = list(range(1, 101))
    game.players[0].coins = 100
    for _ in range(1, 101):
        game.deck.dispense_card()
        game.players[0].get_or_pay_card(game.deck)
    assert len(game.players[0].cards) / 100 <= 0.30


def test_round_play_until_pay(game):
    """Check if method """  # TODO: finish docstring

    game.play_until_pay()
    assert game.number == 2


# TODO: test_game_get_coins












