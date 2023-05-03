import pygame
from Purchasables import *
import os

pygame.init()

class Shop:

    def __init__(self):
        """
        Creates the Shop with the specified attributes.
        Args:
            None
        Returns:
            None
        """
        self.name = "Shop"
        self.stock = []

    def set_shop_stock(self):
        """
        Reads all purchaseable items from PurchasableObjects.txt into the appropriate
        objects (Plant, Animal, or Building) and adds them to shop.stock list.
        """

        with open("PurchaseableObjects.txt") as f:
            finished = False

            while not finished:
                purchaseable = read_purchaseable(f)
        
                if purchaseable == None:
                    finished = True

                else:
                    self.stock.append(purchaseable)


    def get_shop_stock(self):
        """
        Returns a list of all items in shop's stock and their 
        respective prices.
        """
        return self.stock
        

    def check_if_unlocked(self):            #doesn't work yet
        """
        Returns a boolean value indicating whether or not the 
        player has unlocked a category or individual item.
        """
        pass


class Player:

    def __init__(self, name):
        """
        Creates the Player with the specified attributes.
        Args:
            name = (str) the player's name
        Returns:
            None
        """
        self.name = name
        self.inventory = []
        self.money = 100        #start off with $100
        self.plants = True      #plants start off as unlocked
        self.animals = False    #animals start off as locked

    def __repr__(self):
        rep = "Player: " + self.name
        return rep

    def get_name(self):
        """Returns the player's name"""
        return self.name

    def set_farm_name(self):                        #haven't tested this yet
        """Allows player to name their farm"""

        farm_name = input("Name your farm:")
        while farm_name == "":
            print("Please name your farm.")
            farm_name = input("Name your farm:")

    def are_animals_unlocked(self):
        """Returns a boolean value indicating whether the player has unlocked animals"""
        return self.animals
    
    def unlock_animals(self):
        """Sets self.animals to True, indicating that animals have been unlocked"""
        self.animals = True

    def get_money(self):
        """Returns the amount of money the player has on hand"""
        return self.money
    
    def get_inventory(self):
        """Returns a dictionary of items in player's inventory"""
        return self.inventory
    
    def buy(self, item, amount = 1):
        """
        Adds the indicated number of items to player's inventory and subtracts
        the item's cost multiplied by the indicated number from player's money.
        Args:
            amount: (int) the number of items the player is buying in a single transaction
        """
        
        for i in shop.stock:

            if i.get_name() == item:
                cost = int(i.get_cost())

                if (cost * amount) <= self.get_money():

                    for j in range(amount):
                        self.inventory.append(i)

                    self.money -= (cost * amount)
                    print(f"You purchased {amount} {item}(s).")

                else:
                    print("You don't have enough money!")

    
    def sell(self, item, amount = 1):
        """
        Subtracts the indicated number of items from player's inventory and adds
        the item's sell price multiplied by the indicated number to player's money.
        Args:
            amount: (int) the number of items the player is selling in a single transaction
        """
    
        for i in shop.stock:

            if i.get_name() == item:
                sell_price = int(i.get_sell_price())
                number_in_inventory = 0

                for j in self.inventory:

                    if j.get_name() == item:
                        number_in_inventory += 1

                if number_in_inventory >= amount:

                    for k in range(amount):             #removes desired number of item from inventory
                        self.inventory.remove(i)

                    self.money += (sell_price * amount)
                    print(f"You sold {amount} {item}(s) and made ${(amount * sell_price)}.")

                else:
                    print(f"You don't have {amount} {item}(s) to sell!")


shop = Shop()                       #testing stuff
shop.set_shop_stock()
print(shop.get_shop_stock())

Spike = Player("Spike")

print(Spike.get_inventory())
print(Spike.get_money())

Spike.buy("chicken", 10)
print(Spike.get_inventory())
print(Spike.get_money())

Spike.buy("tomato", 5)
print(Spike.get_inventory())
print(Spike.get_money())

Spike.sell("tomato", 8)
print(Spike.get_inventory())
print(Spike.get_money())

Spike.sell("chicken", 6)
print(Spike.get_inventory())
print(Spike.get_money())