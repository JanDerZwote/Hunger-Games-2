class Character:
    name = ""
    health = 0
    alive = True
    weapon = None
    location = None
    inventory = []

    #Constructor
    def __init__(self, p_name):
        self.setName(p_name)
        self.setHealth(10)
        self.setAlive(True)

    #Intrinsic Methods
    def testHealth(self):
        if (self.health > 0):
            return True
        else:
            return False

    def applyDamage(self, p_damage):
        self.setHealth(self.getHealth - p_damage)
        if (self.testHealth() == False):
            self.setAlive(False)

    #Getter and Setter
    def setName(self, p_name):
        self.name = p_name

    def getName(self):
        return self.name

    def setHealth(self, p_health):
        self.health = p_health

    def getHealth(self):
        return self.health

    def setAlive(self, p_alive):
        self.alive = p_alive

    def getAlive(self):
        return self.alive

    def setWeapon(self, p_weapon):
        self.weapon = p_weapon
    
    def getWeapon(self):
        return self.weapon

    def setItem(self, p_item):
        self.inventory.append(p_item)

    def getItem(self, p_index):
        return self.inventory[p_index]

    def getInventory(self):
        return self.inventory.count()

    def setLocation(self, p_location):
        self.location = p_location

    def getLocation(self):
        return self.location