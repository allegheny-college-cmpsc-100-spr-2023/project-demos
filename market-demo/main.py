import json
from market import Market

from inventory import Acquire, Factory, items

def main():
    stocks = Market()
    print(stocks.status("AAA").price)
    Factory("AAA", template = "templates/Share.py")
    Acquire("AAA.py")

if __name__ == "__main__":
    main()