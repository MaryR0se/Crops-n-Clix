import pygame

class Purchaseable:

    def __init__(self, name, buy, sell):
        """
        Creates an item that can be bought and sold.
        Args:
            None
        Returns:
            None
        """
        self.name = name
        self.buy = buy
        self.sell = sell

    def __repr__(self):
        return self.name

    def get_name(self):
        """Returns name of purchaseable item"""
        return self.name
    
    def get_cost(self):
        """Returns cost of purchaseable item"""
        return self.buy
    
    def get_sell_price(self):
        """Returns sell price of purchaseable item"""
        return self.sell

class Animal(Purchaseable):

    def __init__(self, name, buy, sell):    #currently identical to Purchasable class
        """
        Creates an Animal purchaseable.
        Args:
            None
        Returns:
            None
        """
        self.mature = None                  #this is currently necessary to differentiate
        super().__init__(name, buy, sell)   #Plant object from Animal objects; see "read_purchaseable(f)"

class Plant(Purchaseable):

    def __init__(self, name, buy, sell, mature):
        """
        Creates a Plant purchaseable.
        Args:
            None
        Returns:
            None
        """
        self.mature = mature
        super().__init__(name, buy, sell)

class Building(Purchaseable):                #we don't have any buildings yet, but it's here
                                             #if we have time to implement them
    def __init__(self, name, buy, sell):
        """
        Creates a Building purchaseable.
        Args:
            None
        Returns:
            None
        """
        super().__init__(name, buy, sell)


def read_purchaseable(f):
    """
    Reads the next object from the file, returning None at the end.
    Args:
        f (file handle): the file handle of the opened text file
    Returns:
        (Purchaseable object or None): a Purchaseable object or None if at end of the file
    """
    
    name = f.readline().rstrip() 
    if name == "":    
        return None

    buy = f.readline().rstrip()
    if buy == "":
        return None
        
    sell = f.readline().rstrip()
    if sell == "":
        return None
    
    nextline = f.readline().rstrip()
    if nextline == "":                      #Animals don't have a fourth line indicating maturation
        return Animal(name, buy, sell)      #period, this is currently the only thing determining whether
                                            #it gets sorted into the Plant class or the Animal class
    else:
        mature = f.readline().rstrip()
        return Plant(name, buy, sell, mature)
    
        
def categorize_purchaseable(purchaseable):  
    """
    Organizes purchaseables into lists indicating which class
    they belong to.
    Args:
        purchasable: (Purchaseable object) the Purchaseable being organized
    """
    
    purchaseables = []
    animals = []
    plants = []
    buildings = []

    purchaseables.append(purchaseable)

    if purchaseable.mature == None:
        animals.append(purchaseable)

    else:
        plants.append(purchaseable)


"""print(purchaseables)     #testing stuff
print(plants)
print(animals)"""

