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
        if level_of_difficulty == '1':
            chamber.append(i, 1)
        elif level_of_difficulty == '2':
            for b in range(2):
                chamber.append(i, 1)
                i+=1
        elif level_of_difficulty == '3':
            for b in range(3):
                chamber.append(i, 1)
                i+=1
        elif level_of_difficulty == '4':
            for b in range(4):
                chamber.append(i, 1)
                i+=1
        elif level_of_difficulty == '5':
            for b in range(5):
                chamber.append(i, 1)
                i+=1
        else:
            print("That's not a number. ")
            level_of_difficulty == False
        



def intro():
    pass


level_of_difficulty = difficulty()
chamber = bullett_chamber()
number_of_bulletts(level_of_difficulty, chamber)
