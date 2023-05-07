class Hand:

    def __init__(self, deck: list = []):
        # Automagically sort hand every time by suit, 
        # _then_ sort by value
        self.cards = self.__auto_sort(deck[:14])
        self.min_matches = 3

    def __auto_sort(self, cards: list) -> list:
        sorted(
            cards,
            key = lambda card: (card.suit, int(card.rank))
        )
        return cards

    def __is_suit(self, cards: list) -> bool:
        return all(card.suit == cards[0].suit for card in cards)

    def __is_value(self, cards: list) -> bool:
        pass

    def __is_ascending(self, cards: list) -> bool:
        cards = self.__auto_sort(cards)
        for i in range(1, len(cards)):
            if cards[i].rank < cards[i - 1].rank:
                return False
        return True
    
    def __is_sequential(self, cards: list) -> bool:
        cards = self.__auto_sort(cards)
        for i in range(1, len(cards)):
            if cards[i].rank - cards[i - 1].rank != 1:
                return False
        return True

    def sequences(self) -> list:
        start = 0
        finish = 1
        for i in range(len(self.cards)):
            while self.__is_suit(self.cards[start:finish]):
                if finish > len(self.cards):
                    break
                finish += 1
            poss_match = self.cards[start : finish - 1]
            if len(poss_match) >= self.min_matches:
                if self.__is_ascending(poss_match) and self.__is_sequential(poss_match):
                    yield poss_match
            start = i
            finish = i + 1

    def matches(self) -> list:
        matches = []