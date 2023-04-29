import random

class Stock:

    def __init__(self, symbol: str = "", price: float = 0.0):
        self.symbol = symbol
        self.price = price
    
    def update_price(self):
        self.price = round(
            random.uniform(self.price * .30, self.price * 1.2),
            2
        )