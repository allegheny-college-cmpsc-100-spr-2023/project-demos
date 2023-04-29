import json
import random
from stock import Stock
from time import sleep

class Market:

    def __init__(self):
        self.companies = []
        with open("market.json", "r") as fh:
            self.listings = json.load(fh)
        for company in self.listings:
            self.companies.append(
                Stock(
                    company,
                    self.listings[company]["price"]
                )
            )

    def __write(self):
        with open("market.json", "w") as fh:
            json.dump(self.listings, fh)

    def status(self, company: str = "") -> Stock:
        for stock in self.companies:
            if stock.symbol == company:
                return stock

    def update(self) -> None:
        company = random.choice(self.companies)
        company.update_price()
        self.listings[company.symbol]["price"] = company.price
        self.__write()

def main():
    market = Market()
    while True:
        market.update()
        sleep(5)

if __name__ == "__main__":
    main()
