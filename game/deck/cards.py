from .deck import Card, CardType, Deck

cardlist = Deck(200,False)

def cid(id):
    id += 1
    return id

cardlist.add(Card("rock",cid(id),CardType.ROCK,1))
cardlist.add(Card("paper",cid(id),CardType.PAPER,1))
cardlist.add(Card("scissors",cid(id),CardType.SCISSORS,1))
cardlist.add(Card("big rock",cid(id),CardType.ROCK,2))
cardlist.add(Card("big paper",cid(id),CardType.PAPER,2))
cardlist.add(Card("shears",cid(id),CardType.SCISSORS,2))
