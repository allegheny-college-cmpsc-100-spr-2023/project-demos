"""
    Imports Acquire and Factory -- two components of the inventory which:
    * Acquire: automatically "picks up" and adds item to inventory
    * Factory: creates new items from either default or designated template
"""
from inventory import Acquire, Factory, items

def award(amount: int = 0) -> None:
    """ Reward user with n tickets """
    # Generate 5
    for _ in range(amount):
        # "Factory" a ticket according to template in this repo
        Factory("Ticket", template = "templates/Ticket.py")
        # "Pick up" the "factoried" ticket
        Acquire("Ticket.py")

def spend(cost: int = 0) -> bool:
    tickets = items.list["Ticket"]["quantity"]
    if tickets < cost:
        return False
    return True

def main():
    """ Main method """
    print("""
1. Get tickets
2. Spend tickets
""")
    choice = int(input("Choose: "))
    if choice == 1:
        award(5)
    else:
        price = int(input("Cost: "))
        print(f"Can spend tickets: {spend(price)}")

if __name__ == "__main__":
    # Run program beginning at main method
    main()