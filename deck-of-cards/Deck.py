from Card import Card

class Deck:

    def __init__(self):
        self.cards = []
        suits = ["♠︎", "♣︎", "♥︎", "♦︎"]
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        for suit in suits:
            for rank in ranks:
                card = Card(rank = rank, suit = suit)
                self.cards.append(card)