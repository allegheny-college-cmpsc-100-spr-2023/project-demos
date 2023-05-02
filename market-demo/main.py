import json
from market import Market

from inventory import Acquire, Factory, items

def main():
    stocks = Market()
    symbol = input("Symbol: ")
    cost = stocks.status(symbol).price
    Factory(symbol, template = "templates/Share.py")
    Acquire(f"{symbol}.py")
    qty = items.list[symbol]["quantity"]
    value = qty * cost
    print(f"{symbol} {qty} @ {cost} -> {value}")

if __name__ == "__main__":
    main()