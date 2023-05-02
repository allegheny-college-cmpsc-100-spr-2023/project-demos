import json
from market import Market

from inventory import Acquire, Factory, items

def main():
    stocks = Market()
    symbol = input("Symbol: ")
    print(stocks.status(symbol).price)
    Factory(symbol, template = "templates/Share.py")
    Acquire(f"{symbol}.py")

if __name__ == "__main__":
    main()