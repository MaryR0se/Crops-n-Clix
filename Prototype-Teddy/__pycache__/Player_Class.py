import pygame
import os
pygame.init()

plants = {}                     #will rework these as needed when i get more info
animals = {}                    #about the plants/animals classes
inventory = [plants, animals]

class Player:

    def __init__(self, name, plants, animals, inventory, money):
        """
        Creates the Player with the specified attributes.
        Args:
            name = the player's name
            plants = the plants the player has in their inventory
            animals = the animals the player has in their inventory
            inventory = all items the player has in their inventory
            money = how much money the player has on hand
        Returns:
            None
        """
        self.name = name
        self.plants = plants
        self.animals = animals
        self.inventory = inventory
        self.money = money

    def __repr__(self):
        rep = "Player: " + self.name
        return rep

    def get_name(self):
        """Returns the player's name"""
        return self.name

    def set_name(self):
        """Will be used to name the character when the game starts"""
        pass

    def are_plants_unlocked(self):
        """Returns a boolean value indicating whether the player has unlocked plants
        NOTE: Plants should be unlocked as soon as the game starts"""
        return self.plants
    
    def unlock_plants(self):
        """Sets self.plants to True, indicating that plants have been unlocked"""
        self.plants = True

    def are_animals_unlocked(self):
        """Returns a boolean value indicating whether the player has unlocked animals"""
        return self.animals
    
    def unlock_animals(self):
        """Sets self.animals to True, indicating that animals have been unlocked"""
        self.animals = True

    def get_money(self):
        """Returns the amount of money the player has on hand"""
        return "$" + str(self.money)
    
    def get_inventory(self):
        """Returns a list of items in player's inventory"""
        return self.inventory
    
    def buy(self, amount):
        """Adds the indicated number of units to player's inventory and subtracts
        the item's cost multiplied by the indicated number from player's money"""
        self.amount = amount
        cost = 1
        units = 1
        self.inventory += (amount * units)
        self.money -= (amount * cost)
    
    def sell(self, amount):
        """Subtracts the indicated number of units from player's inventory and adds
        the item's cost multiplied by the indicated number to player's money"""
        self.amount = amount
        cost = 1
        units = 1
        self.inventory -= (amount * units)
        self.money += (amount * cost)

