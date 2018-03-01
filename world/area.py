import random as rnd

class Area:
    name = ""
    neighbours = []

    #Constructor
    def __init__(self, p_name):
        self.setName(p_name)

    #Intrinsic Methods
    def chooseRandomNeighbour(self):
        randomNeighbour = (rnd.randint(1, self.neighbours.count())) - 1
        return self.getNeighbour(randomNeighbour)

    #Getter and Setter
    def setName(self, p_name):
        self.name = p_name

    def getName(self):
        return self.name

    def setAddNeighbour(self, p_neighbour):
        self.neighbours.append(p_neighbour)

    def getNeighbour(self, p_index):
        return self.neighbours[p_index]