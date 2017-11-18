class Town:
    def __init__(self, name):
        self.name = name
        self.buildings = []
    def addBuilding(self, b):
        self.buildings.append(b)
    def getName(self):
        return self.name

class Town2:
    def __init__(self, name):
        self.name = name
        self.buildings = []
    def addBuilding(self, b):
        self.buildings.append(b)
    def getName(self):
        return self.name