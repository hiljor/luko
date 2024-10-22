from game.deck.deck import Deck
from game.deck.battle import Battle, BattleResult
from game.deck.cards import cardlist
import random

battle = Battle()

player_deck = Deck(52)
hand = Deck(3)

for i in range(12):
    card = cardlist.find(random.randrange(3))
    if card == False:
        print("Card does not exist")
    else:
        player_deck.add(card)
for i in range(5):
    card = cardlist.find(i)
    print("gg")
    if card != False:
            print(card.id)
    else:
        print("false")

for i in range(len(cardlist.stack)):
    print(i)
    print(cardlist.stack[i].id)

player_deck.shuffle()
for i in range(hand.total()):
    hand_add = hand.add(player_deck.pop())
    if (hand_add != 0):
        print("Hand Failed")
        print(hand_add)
        exit()
print("Test Hand\n")
print("Your Hand:")
for i in range(hand.count()):
    print("(" + i.__repr__() + ") " + hand.view(i).name)

userinput = int(input("Select the number of the card: "))
user_card = hand.pop(userinput)
print("\n")
cardlist.shuffle()
enemy_card = cardlist.view(0)
print("enemy picked: " + enemy_card.name)
result = battle.fight(user_card, enemy_card)
print(result)
