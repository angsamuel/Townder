from enum import Enum

class BuildingType(Enum):
    MISC = 0
    HOUSE = 1

class Building:
    def __init__(self, name, type):
		self.name = name
		self.type = BuildingType.MISC

class House(Building):
    def __init__(self, name):
        self.name = name
        self.type = BuildingType.HOUSE