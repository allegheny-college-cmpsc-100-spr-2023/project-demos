from Card import Card
from typing import Generator

class Hand:

    def __init__(self, deck: list = []):
        self.cards = self.__auto_sort(deck[:14])
        self.min_matches = 3

    def __auto_sort(self, cards: list) -> list:
        """ Sort on demand by suit, then rank """
        cards = sorted(
            cards,
            key = lambda card: (card.suit, card.rank)
        )
        return cards

    def __is_suit(self, cards: list) -> bool:
        """ Return true if all suits match """
        return all(card.suit in cards[0].suit for card in cards)

    def __is_value(self, cards: list) -> bool:
        """ Return if all have the same value """
        return all(card.rank in [cards[0].rank] for card in cards)

    def __is_ascending(self, cards: list) -> bool:
        """ Check if values ascend """
        cards = self.__auto_sort(cards)
        for i in range(1, len(cards)):
            if cards[i].rank < cards[i - 1].rank:
                return False
        return True
    
    def __is_sequential(self, cards: list) -> bool:
        """ Check if values are in sequence """
        cards = self.__auto_sort(cards)
        for i in range(1, len(cards)):
            if cards[i].rank - cards[i - 1].rank != 1:
                return False
        return True

    def __assign_wilds(self, cards: list) -> list:
        suits = {"S":"♠︎", "C":"♣︎", "H":"♥︎", "D":"♦︎"}
        for card in cards:
            if card.rank == 51:
                idx = cards.index(card)
                rank = input("ENTER JOKER RANK [2-A]: ")
                for suit in suits:
                    print(f"{suit}. {suits[suit]}")
                suit = input("ENTER SUIT: ")
                cards[idx] = Card(rank.upper(), suits[suit.upper()])
        return self.__auto_sort(cards)

    def __auto_assign_wilds(self, cards: list) -> list:
        value = [card for card in cards if card.rank != 51]
        for card in cards:
            if card.rank == 51:
                idx = cards.index(card)
                cards[idx] = Card(value[0].rank, "♠︎♣︎♥︎♦︎")
        return self.__auto_sort(cards)

    def sequences(self, cards: list = list()) -> Generator[list, list, None]:
        """ Determine all sequences matching rules """
        start = 0
        finish = 1
        # If no list provided as parameter, default to dealt hand
        if not cards:
            cards = self.cards
        cards = self.__assign_wilds(cards)
        # Iterate through cards using index values
        for i in range(len(cards)):
            # While suits match, keep going
            while self.__is_suit(cards[start : finish]):
                # Increment to next card
                finish += 1
                # If we've reached the end, break
                if finish > len(cards):
                    break
            # Here, this is a potential match
            poss_match = cards[start : finish]
            # If at least min_matches long...
            if len(poss_match) >= self.min_matches:
                # _And_ if ascending _and_ sequential
                if self.__is_ascending(poss_match) and self.__is_sequential(poss_match):
                    # Send a match immediately (see main.py for handling)
                    yield poss_match
            # Start where we ended?
            start = i + 1
            # Next card after new start
            finish = i + 2

    def matches(self, cards: list = list()) -> Generator[list, list, None]:
        """ Return three-of-a-kinds """
        start = 0
        finish = 1
        if not cards:
            cards = self.cards
        # Auto assign to the first non-Joker value
        cards = self.__auto_assign_wilds(cards)
        for i in range(len(cards)):
            while self.__is_value(cards[start : finish]):
                finish += 1
                if finish > len(cards):
                    break
            poss_match = cards[start : finish]
            if len(poss_match) >= self.min_matches:
                yield(poss_match)
            start = i + 1
            finish = i + 2