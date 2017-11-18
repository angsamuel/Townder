from Character import *
from Building import *
from Town import *
import json
import os
import pickle
#https://twitter.com/drewtoothpaste/status/931569797418115072

def buildCharacter():
	name = raw_input("Enter your character's name> ")
	gender = raw_input("Enter your character's gender> ")
	age = raw_input("Enter your character's age> ")
	title = raw_input("Enter your title> ")
	playerCharacter = Character(name, age, gender, title)
	confirmCharacter(playerCharacter)

def confirmCharacter(c):
	print "Do you want to play as {} {}, AGE {}  GENDER {}?".format(c.title, c.name, c.age, c.gender)
	choice = raw_input("(y/n)> ")
	if choice == "y":
		#save character
		if not os.path.exists("save_data/" + c.name):
			os.makedirs("save_data/" + c.name)
		pickle_out = open("save_data/" + c.name + "/character.pickle", "wb")
		pickle.dump(c, pickle_out)
		pickle_out.close()
		buildTown(c.name)
	elif choice == "n":
		print("Okay, let's try again...")
		buildCharacter()
	else:
		print("please type (y/n)")
		confirmCharacter(c)

def buildTown(filename):
	townName = raw_input("What will the name of your town be?> ")
	houseName = raw_input("What will the name of your house be?> ")
	playerTown = Town(townName)
	playerHouse = House(houseName)
	playerTown.addBuilding(playerHouse)
	confirmTown(playerTown, filename)

def confirmTown(town, filename):
	print "So you will be living in your home {} in your newly founded town of {}?".format(town.name, town.buildings[0].name)
	choice = raw_input("(y/n)> ")
	if choice == "y":
		#save town
		pickle_out = open("save_data/" + filename + "/town.pickle", "wb")
		pickle.dump(town, pickle_out)
		pickle_out.close()
	elif choice == "n":
		print("Okay, let's try again...")
		buildTown()
	else:
		print("please type (y/n)")
		confirmTown(town)


print "\n\n\n"
print "Welcome to Townder!"
print "---Start New Game: N"
print "---Load Game: L"
choice = raw_input(">")


if choice.upper() == "N":
	print "alright, a new game it is"
	buildCharacter()
#Save Game


#myTest = Test("Dan")
#print myTest.name
