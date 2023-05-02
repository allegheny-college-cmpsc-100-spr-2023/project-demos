class Share(ItemSpec):

    def __init__(self):
        """ Constructor """
        # term-world standard for inheriting ItemSpec
        super().__init__(__file__)
        # Overriding the inventory system volume, set to 0
        self.VOLUME = 0
    
    def use(self) -> None:
        """ Functionality executed when used """
        print("GENERATIONAL WEALTH!")
