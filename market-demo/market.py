import json
import random
from time import sleep

class Market:

    def __init__(self):
        self.companies = ["AAA", "BBB", "CCC"]
        with open("market.json", "r") as fh:
            self.ticker = json.load(fh)

    def __write(self):
        with open("market.json", "w") as fh:
            json.dump(self.ticker, fh)

    def status(self, company: str = "") -> dict:
        return self.ticker[company]

    def update(self) -> None:
        company = random.choice(self.companies)
        try:
            price = self.ticker[company]["price"]
        except:
            self.ticker[company] = {"price": 10}
        price = self.ticker[company]["price"]
        price -= random.randint(1,10)
        self.ticker[company]["price"] = price
        self.__write()

def main():
    market = Market()
    while True:
        market.update()
        sleep(20)

if __name__ == "__main__":
    main()