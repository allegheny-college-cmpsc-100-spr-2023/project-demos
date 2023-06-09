"""
    Imports Acquire and Factory -- two components of the inventory which:
    * Acquire: automatically "picks up" and adds item to inventory
    * Factory: creates new items from either default or designated template
    * items: an object which contains a user's inventory
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
    """ Spend n user tickets """
    # Get the tickets in user's inventory
    tickets = items.list["Ticket"]["quantity"]
    # Evaluate if the tickets can spend
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
        can_spend = spend(price)
        if can_spend:
            for _ in range(price):
                items.use("Ticket")

if __name__ == "__main__":
    # Run program beginning at main method
    main()