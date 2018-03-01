import character
import weapon
import random

class Cast:
    cast = []
    arsenal = []

    def __init__(self):
        self.createArsenal()
        self.createCast()


    def createCast(self):
        print("How many combatants do you want?")
        combatants = input()
        try:
            int(combatants)
            combatants = int(combatants)
        except ValueError:
            combatants = 0
        while (combatants <= 0):
            print("The input is either not a number or smaller than 1. Please insert a number.")
            combatants = input()
            try:
                int(combatants)
                combatants = int(combatants)
            except ValueError:
                combatants = 0
        
        # Create each Cast member
        for i in range(combatants):
            print("Please insert the name of contestant number", i+1)
            contestantName = input()
            newCharacter = character.Character(contestantName)
            self.cast.append(newCharacter)
        # Insert Portraits here

    def createArsenal(self):
        #Primitive Weapons
        self.arsenal.append(weapon.Weapon("Stick", False, 1, 1, 1))
        self.arsenal.append(weapon.Weapon("Rock", False, 1, 2, 1))
        self.arsenal.append(weapon.Weapon("Sling", True, 1, 1, 1))
        self.arsenal.append(weapon.Weapon("Sharp Stick", False, 1, 1, 1))
        self.arsenal.append(weapon.Weapon("Metal Rod", False, 1, 2, 1))

        #Simple Weapons
        self.arsenal.append(weapon.Weapon("Knife", False, 3, 2, 2))
        self.arsenal.append(weapon.Weapon("Axe", False, 2, 3, 2))
        self.arsenal.append(weapon.Weapon("Hammer", False, 2, 3, 2))
        self.arsenal.append(weapon.Weapon("Sword", False, 2, 3, 2))
        self.arsenal.append(weapon.Weapon("Spear", False, 2, 3, 2))
        self.arsenal.append(weapon.Weapon("Crossbow", True, 5, 1, 2))
        self.arsenal.append(weapon.Weapon("Bow", True, 4, 2, 2))

        #Good Weapons
        self.arsenal.append(weapon.Weapon("Gun", True, 5, 2, 3))
        self.arsenal.append(weapon.Weapon("Rifle", True, 6, 2, 3))
        self.arsenal.append(weapon.Weapon("Sniper Rifle", True, 10, 3, 3))
        self.arsenal.append(weapon.Weapon("Shotgun", False, 6, 3, 3))

    def armCast(self):
        for i in range(self.cast.count):
            diceRoll = random.randint(1,100)
            if diceRoll <= 50:
                