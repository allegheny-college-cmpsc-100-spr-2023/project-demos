class Ticket(ItemSpec):

    def __init__(self):
        super().__init__(__file__)
        self.VOLUME = 0
    
    def use(self) -> None:
        print("USED 1 TICKET")