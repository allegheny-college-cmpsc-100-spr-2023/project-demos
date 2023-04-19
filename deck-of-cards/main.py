from Deck import Deck

def main():
    deck = Deck().cards + Deck().cards
    print(len(deck))

if __name__ == "__main__":
    main()