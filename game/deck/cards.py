from .deck import Card, CardType, Deck

cardlist = Deck(200,False)

cardlist.add(Card("rock",cardlist.cid(),CardType.ROCK,1))
cardlist.add(Card("paper",cardlist.cid(),CardType.PAPER,1))
cardlist.add(Card("scissors",cardlist.cid(),CardType.SCISSORS,1))
cardlist.add(Card("big rock",cardlist.cid(),CardType.ROCK,2))
cardlist.add(Card("big paper",cardlist.cid(),CardType.PAPER,2))
cardlist.add(Card("shears",cardlist.cid(),CardType.SCISSORS,2))
