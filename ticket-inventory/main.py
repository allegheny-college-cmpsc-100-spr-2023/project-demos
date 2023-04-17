from inventory import Acquire, Factory

def main():
    for _ in range(5):
        Factory("Ticket", template = "templates/Ticket.py")
        Acquire("Ticket.py")

if __name__ == "__main__":
    main()