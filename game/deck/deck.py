#Deck
from enum import Enum
import random

# Basic Concept
# you have rock paper and sissor Cards
# so we need to have an Deck
#   -> deck.add(item)
#   -> deck.remove(cardNumber)
#   -> deck.pop()
#   -> deck.shuffle

# if item does not exist break
# if deck number does not exist break

class CardType(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

class Card:
    def __init__(self, name: str, id: int, card_type: CardType, bigness: int):
        self.name = name
        self.id = id
        self.card_type = card_type
        self.bigness = bigness
        #self.level =
        #self.damage = 
        #self.speed =
        #self.health =

class Deck:
    def __init__(self, max: int, duplicate: bool = True):
        self.stack = []
        self.max = max
        self.allow_duplicates = duplicate

    def total(self):
        return self.max

    def count(self):
        return len(self.stack)

    def add(self, card: Card):
        if self.allow_duplicates == False and card in self.stack:
            return
        if len(self.stack) >= (self.max):
            return
        self.stack.append(card)
        return 0
    def pop(self, index=0):
        card = self.stack[index]
        self.stack.pop(index)
        return card
    def view(self, index=0):

        return self.stack[index]
    def shuffle(self):
        random.shuffle(self.stack)
    def find(self, card_id: int, start: int =0):
        for i in range(start, len(self.stack)):
            if self.stack[i].id == card_id:
                return self.stack[i]
        return False
