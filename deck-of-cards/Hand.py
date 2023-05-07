class Hand:

    def __init__(self, deck: list = []):
        self.cards = self.__auto_sort(deck[:14])
        self.min_matches = 3

    def __auto_sort(self, cards: list) -> list:
        """ Sort on demand by suit, then rank """
        sorted(
            cards,
            key = lambda card: (card.suit, int(card.rank))
        )
        return cards

    def __is_suit(self, cards: list) -> bool:
        """ Return true if all suits match """
        return all(card.suit == cards[0].suit for card in cards)

    def __is_value(self, cards: list) -> bool:
        """ Return if all have the same value """
        return all(card.rank == cards[0].rank for card in cards)

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

    def sequences(self) -> list:
        """ Determine all sequences matching rules """
        start = 0
        finish = 1
        # Iterate through cards using index values
        for i in range(len(self.cards)):
            # While suits match, keep going
            while self.__is_suit(self.cards[start : finish]):
                # If we've reached the end, break
                if finish > len(self.cards):
                    break
                # Otherwise, increment to next card
                finish += 1
            # Here, this is a potential match
            poss_match = self.cards[start : finish - 1]
            # If at least min_matches long...
            if len(poss_match) >= self.min_matches:
                # _And_ if ascending _and_ sequential
                if self.__is_ascending(poss_match) and self.__is_sequential(poss_match):
                    # Send a match immediately (see main.py for handling)
                    yield poss_match
            # Start where we ended?
            start = i
            # Next card after new start
            finish = i + 1

    def matches(self) -> list:
        """ Return three-of-a-kinds: IS UNTESTED """
        start = 0
        finish = 1
        for i in range(self.cards):
            while self.__is_value(self.cards[start : finish]):
                if finish > len(self.cards):
                    break
                finish += 1
            poss_match = self.cards[start : finish -1]
            if len(poss_match) >= self.min_matches:
                yield(poss_match)
            start = i
            finish = i + 1
        matches = []