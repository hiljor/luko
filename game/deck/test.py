from deck import Deck
from battle import Battle, BattleResult
from cards import cardlist

battle = Battle()

player_deck = Deck(52)
hand = Deck(3)

for i in range(52):
    player_deck.add(cardlist.find(1))

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
