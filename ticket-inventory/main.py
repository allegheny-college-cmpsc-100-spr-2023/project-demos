"""
    Imports Acquire and Factory -- two components of the inventory which:
    * Acquire: automatically "picks up" and adds item to inventory
    * Factory: creates new items from either default or designated template
"""
from inventory import Acquire, Factory

def main():
    """ Main method """
    # Generate 5
    for _ in range(5):
        # "Factory" a ticket according to template in this repo
        Factory("Ticket", template = "templates/Ticket.py")
        # "Pick up" the "factoried" ticket
        Acquire("Ticket.py")

if __name__ == "__main__":
    # Run program beginning at main method
    main()