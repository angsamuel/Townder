from Town import *
class Test:
    def __init__(self, name):
        self.name = name
        self.buildings = []
    def addBuilding(self, b):
        self.buildings.append(b)
    def getName(self):
        return self.name

test = Test("wow")
print test.name

town = Town("wowee")
print town.name