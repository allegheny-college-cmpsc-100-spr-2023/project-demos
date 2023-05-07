from Deck import Deck
from Hand import Hand

from random import shuffle

def main():
    while True:
        deck = Deck().cards + Deck().cards
        shuffle(deck)
        hand = Hand(deck)
        for seq in hand.sequences():
            print(f"IS MATCH: {[str(card) for card in seq]}")

if __name__ == "__main__":
    main()