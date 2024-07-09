from .deck import Card,CardType
from enum import Enum

class BattleResult(Enum):
    DRAW = 0
    PLAYER1 = 1
    PLAYER2 = 2

class Battle:
    # rock has 3x against Sissors
    # Paper has 3x against Rock
    # Sissors has 3x against Paper
    def __init__(self):
        self.data = 0
        self.result = BattleResult.DRAW

    def fight(self, card1: Card, card2: Card):
        if card1.card_type == CardType.ROCK:
            if card2.card_type == CardType.PAPER:
                self.result = BattleResult.PLAYER2
                return BattleResult.PLAYER2
            if card2.card_type == CardType.SCISSORS:
                self.result = BattleResult.PLAYER1
                return BattleResult.PLAYER1
        elif card1.card_type == CardType.PAPER:
            if card2.card_type == CardType.ROCK:
                self.result = BattleResult.PLAYER1
                return BattleResult.PLAYER1
            if card2.card_type == CardType.SCISSORS:
                self.result = BattleResult.PLAYER2
                return BattleResult.PLAYER2
        elif card1.card_type == CardType.SCISSORS:
            if card2.card_type == CardType.ROCK:
                self.result = BattleResult.PLAYER2
                return BattleResult.PLAYER2
            if card2.card_type == CardType.PAPER:
                self.result = BattleResult.PLAYER1
                return BattleResult.PLAYER1
        self.result = BattleResult.DRAW
        return BattleResult.DRAW

    def results(self):
        return self.result
