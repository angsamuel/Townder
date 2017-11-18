import pickle
from Town import *
from Building import *

#example_dict = {1: "6", 2: "2", 3: "f"}
#pickle_out = open("dict.pickle","wb")
#pickle.dump(example_dict, pickle_out)
#pickle_out.close()

#pickle_in = open("dict.pickle", "rb")
#example_dict = pickle.load(pickle_in)
#print(example_dict)

t = Town("MyTown")
h = House("MyHouse")
t.addBuilding(h)

pickle_out = open("town.pickle", "wb")
pickle.dump(t, pickle_out)
pickle_out.close()

pickle_in = open("town.pickle", "rb")
lt = pickle.load(pickle_in)
print lt.buildings[0].name
