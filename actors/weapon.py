import random as rnd

class Weapon:
    name = ""
    ranged = False
    damage = 0
    durability = 1
    rarity = 1

    #Constructor
    def __init__(self, p_name, p_ranged, p_damage, p_durability, p_rarity):
        self.setName(p_name)
        self.setRanged(p_ranged)
        self.setDamage(p_damage)
        self.setDurability(p_durability)
        self.setRarity(p_rarity)

    #Intrinsic methods
    def durabilityTest(self):
        if (self.getDurability > 0):
            return True
        else:
            return False
    
    def durabilityDecline(self):
        diceRole = rnd.randint(0,100)
        if (diceRole <= 25):
            self.setDurability(self.getDurability - 1)

    #Getter and Setter
    def setName(self, p_name):
        self.name = p_name
    
    def getName(self):
        return self.name

    def setRanged(self, p_ranged):
        self.ranged = p_ranged

    def getRanged(self):
        return self.ranged

    def setDamage(self, p_damage):
        self.damage = p_damage

    def getDamage(self, p_damage):
        return self.damage

    def setDurability(self, p_durability):
        self.durability = p_durability

    def getDurability(self):
        return self.durability

    def setRarity(self, p_rarity):
        self.rarity = p_rarity

    def getRarity(self):
        return self.rarity