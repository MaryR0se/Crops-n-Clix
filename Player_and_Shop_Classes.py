import pygame
import os
#will need to import plant and animal classes

pygame.init()

class Shop:

    shop_stock = {"carrot seed": 5, "baby pig": 10}    #KEY = unit name (i.e carrot seed, baby pig, etc)
                                                       #VALUE = how much it costs, represented as an integer

    def __init__(self):
        """
        Creates the Shop with the specified attributes.
        Args:
            None
        Returns:
            None
        """
        self.name = "Shop"

    def get_shop_stock(self, item = ""):                                    #this will only work for accessing item's
                                                                            #price once we have prices as part of plant/
                                                                            #animal classes
        """Returns a dictionary of all items in shop's stock and their 
        respective prices.
        Args:
            item(optional): (str) if specified, indicates the price
                            of the specified item only"""
        
        if item == "":
            return self.shop_stock
        
        else:
            if item not in self.shop_stock:
                print(f"{item}is not available for purchase!")

            else:
                return self.shop_stock[item]
        

    def check_if_unlocked(self):
        """Returns a boolean value indicating whether or not the 
        player has unlocked a category or individual item."""
        pass

    def check_if_enough_money(self, item, amount = 1):
        """Returns a boolean value indicating whether or not the
        player has enough money to purchase the indicated item.
        Args:
            item: (str) item whose cost the player's money will be compared to
            amount(optional): (int) amount of item the player is trying to buy"""
        
        cost = 1        #placeholder; this will be specified in plant/animal classes
        
        if Player.get_money(self) < (cost * amount):    #again, this will need to be modified once we
            enough_money = False                        #have the specific prices of everything

        else:
            enough_money = True

        return enough_money

class Player:

    def __init__(self, name):
        """
        Creates the Player with the specified attributes.
        Args:
            name = (str) the player's name
            money = (int) how much money the player has on hand
        Returns:
            None
        """
        self.name = name
        self.inventory = {}     #KEY: item      VALUE: number of that item in inventory
        self.money = 100        #start off with $100
        self.plants = True      #plants start off as unlocked
        self.animals = False    #animals start off as locked

    def __repr__(self):
        rep = "Player: " + self.name
        return rep

    def get_name(self):
        """Returns the player's name"""
        return self.name

    def set_name(self):
        """Will be used to name the character when the game starts"""
        pass

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
        """Adds the indicated number of units to player's inventory and subtracts
        the item's cost multiplied by the indicated number from player's money.
        Args:
            amount: the number of items the player is buying in a single transaction"""
        
        cost = 1            #placeholder; this will be specified in plant/animal classes

        if Shop.check_if_enough_money(self, item) == False:       #prevents player from buying more than they can afford
            print("You don't have enough money!")

        else:

            if item not in self.inventory:                  #if player doesn't have any of the item in their inventory,
                self.inventory[item] = amount               #adds item as a value in inventory dictionary

            elif item in self.inventory:
                self.inventory[item] += amount

            self.money -= (amount * cost)
            print(f"You purchased {amount} {item}(s).")
    
    def sell(self, item, amount = 1):
        """Subtracts the indicated number of units from player's inventory and adds
        the item's cost multiplied by the indicated number to player's money.
        Args:
            amount: the number of items the player is buying in a single transaction"""
        
        cost = 1            #placeholder; this will be specified in plant/animal classes

        if (item not in self.inventory) or (amount > self.inventory[item]):     #prevents player from selling more of the
            print(f"You don't have {amount} {item} to sell!")                   #item than they have

        elif self.inventory[item] >= amount:
            self.inventory[item] -= amount

        self.money += (amount * cost)
        print(f"You sold {amount} {item}(s) and made ${(amount * cost)}.")


