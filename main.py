from random import randint

def difficulty():
    level_of_difficulty = input("What level would you like to chose? ")
    return level_of_difficulty

def bullett_chamber():
    chamber = [0,0,0,0,0,0]
    return chamber

def number_of_bulletts(level_of_difficulty, chamber):
    i = 1
    while level_of_difficulty != True:
        num = int(level_of_difficulty)
        for b in range(num):
            chamber.insert(1, i)
            i+=1
        else:
            print("That's not a number. ")
        



def intro():
    pass


level_of_difficulty = difficulty()
chamber = bullett_chamber()
number_of_bulletts(level_of_difficulty, chamber)
