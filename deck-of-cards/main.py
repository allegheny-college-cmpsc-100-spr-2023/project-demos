from Deck import Deck
from Hand import Hand
from Card import Card

from random import shuffle

def main():
    #while True:
    deck = Deck().cards + Deck().cards
    shuffle(deck)
    #hand = Hand(deck)
    hand = Hand([
        Card("6","♦︎"),
        Card("8","♦︎"),
        Card("JK","♠︎♣︎♥︎♦︎")
    ])
    for seq in hand.sequences():
        print(f"IS MATCH: {[str(card) for card in seq]}")
    hand = Hand([
        Card("8","♦︎"),
        Card("JK","♠︎♣︎♥︎♦︎"),
        Card("8","♦︎")
    ])
    for match in hand.matches():
        print(f"IS MATCH: {[str(card) for card in match]}")

if __name__ == "__main__":
    main()