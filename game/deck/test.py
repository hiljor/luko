from deck import Card, CardType, Deck
from battle import Battle, BattleResult

rock = Card("rock",CardType.ROCK,1)
paper = Card("paper",CardType.PAPER,1)
scissors = Card("scissors",CardType.SCISSORS,1)

battle = Battle()

all_cards = Deck(200,False)
player_deck = Deck(52)
hand = Deck(3)

print(all_cards.add(rock))
print(all_cards.add(rock))
print(all_cards.add(rock))
print(all_cards.add(rock))
print(all_cards.add(paper))

player_deck.add(rock)
player_deck.add(rock)
player_deck.add(rock)
player_deck.add(paper)
player_deck.add(paper)
player_deck.add(paper)
player_deck.add(scissors)
player_deck.add(scissors)
player_deck.add(scissors)
player_deck.add(scissors)

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
enemy_card = all_cards.view()
print("enemy picked: " + enemy_card.name)
all_cards.shuffle()
result = battle.fight(user_card, enemy_card)
print(result)
