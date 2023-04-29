import json
from market import Market

def main():
    stocks = Market()
    print(stocks.status("AAA").price)

if __name__ == "__main__":
    main()