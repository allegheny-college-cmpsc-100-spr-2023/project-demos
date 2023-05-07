class Card:

    # List of conversions for "royal" values
    ROYALS = {
        "JK": 51,
        "A": 14,
        "J": 11,
        "Q": 12,
        "K": 13,
    }

    def __init__(self, rank: str = "", suit: str = ""):
        # Handle case where it's helpful to rank cards by int value
        try:
            self.rank = int(self.ROYALS[rank])
        except KeyError:
            # In the event that there's no corresponding key...
            self.rank = int(rank) 
        # Suit is as suit does
        self.suit = suit

    def __str__(self) -> str:
        # Define rank
        rank = self.rank
        # If it's a "ROYAL", though...
        if self.rank in self.ROYALS.values():
            # Find key by value in dictionary
            rank = list(
                self.ROYALS.keys()
            )[list(self.ROYALS.values()).index(self.rank)]
        # Print text version of key, keeping underlying int value
        return f"{rank}{self.suit}"