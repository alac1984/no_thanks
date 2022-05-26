from pytest import fixture
from models import Deck, Player, Game


@fixture
def game():
    deck = Deck()
    p1 = Player("John")
    p2 = Player("Mary")
    p3 = Player("Anny")
    p4 = Player("Pops")
    p5 = Player("Jayna")
    p6 = Player("Ali")
    players = [p1, p2, p3, p4, p5, p6]
    game = Game(deck, players)
    yield game
