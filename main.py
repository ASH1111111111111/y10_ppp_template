from time import sleep
from random import randint


def greeting():
    print("Hello There")
    print("It seems that you've decided to challange me to a duel in russian roulete")
    comfirm_begin = input("Is that true? ")
    if comfirm_begin.lower() == "yes":
        print("Very well, let's begin")
    elif comfirm_begin.lower() == "no":
        print("You intolerate bufoon, wasting my time. Back to where you come from")
    else:
        print("I don't speak this language wit thy tounge. Either say yes or no like a normal person would. You impertinent fool! ")
        print("If you fail again, I'm going to banish you from this world.")
        
        bad_greeting()
        
def bad_greeting():
    print("So, will you continue and possibly shine amongst the light, or drown within the depths of the ocean.")
    comfirm_begin = input("Are you going to battle me? ")
    if comfirm_begin.lower() == "yes":
        print("Very well, took you a while but your tiny brain got there in the end.")
    else:
        print("To the streets of hell you go.")
        print("*YOU HAVE BEEN BANISHED FROM THIS WORLD*")
        quit()


def rules():
    print("The rules of russian roulete is ⬇️")
    print("1.You will be going against the master of russian roulete AKA me. ")
    print("2. So hit, meaning you can shoot me or you can stand, which makes you shoot yourself")
    print("3. We will go in turns. You will always go first as you are our guest. ")
    print("4. You and I will both have 3 lives, everytime you get shot you will lose 1 life.")
    print("5. First person to lose all their lives, loses.")
    
def terms_and_conditions():
    print("                                                                                             ")
    print("                                                                                             ")
    print("Here are the terms and conditions ⬇️")
    print("1. You must follow the rules of the game. Any rules not followed will result in an immediate ban. ")
    print("2. Any thing that may happen to your device internally or externally will not be our fault.")
    print("3. You must not impersonate anyone.")
    print("4. Later depending on your further choices, somethings may change to your display")
    print("5. Things may be said to you which may emotionally harm you, which could lead you to harm yourself phyically.")
    print("This will not be ou fault. And please do not harm yourself. If you need help, please call +852 2343 2255 ")
    print(" ")
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print(" ")
    print("Would you like to accept these terms of conditons? ")
    proceed = input("Please answer as yes. Anything else entered will result in you being banished")
    if proceed.lower() == "yes":
        signature = input("Please sign here to comfirm. ")
        print(f"Very well {signature}. Let's begin.")
    else:
        print("*YOU HAVE BEEN BANISHED FROM THIS WORLD*")
        quit()

def choose_mode():
    global mode_chosen
    
    print("Now that you must choose a mode. Safe or Risky.")
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("Here are the differences.")
    print("Safe mode")
    print("In safe mode, If you win, your screen will flash rainbow for a few seonds only.")
    print("But if you die. It will simply say that you've died.")
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("Risky mode")
    print("I won't give so much detail, but all I will say the higher the difficulty, the higher reward but also the higher concequence.")
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    mode_chosen = input("So. What mode do you choose, safe or risky. ")
    if mode_chosen.lower() == "safe":
        print("I see that you don't got the guts to play risky.")
        print("But I guess I'll understand since you're just a mortal being.")
        sleep(0.7)
        safe()
        
    elif mode_chosen.lower() == "risky":
        print("You've got guts")
        print("And I like that.")
        sleep(0.7)
        risky()
    else:
        print("Another idiot wasting my time. ")
        print("*YOU HAVE BEEN BANISHED FROM THIS WORLD*")
        quit()

def safe():
    print("I see that you shiver in your boots")
    print("But lets get into the game")
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    sleep(0.7)

    main_game()

def risky():
    print("I see you want to face me head on.")
    print("I like that, let now continue the game.")
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    sleep(0.7)
    
    main_game()
    
def main_game():
    print("I have already told you the rules of the games. ")
    print("Now Let's begin")
    
    
    
    bot_lives = 3
    player_lives = 3
    
    chamber = 6
    
    valid_input = False
    hit_or_stand = input("Do you want to hit or stand")
    if hit_or_stand.lower() == "hit":
        valid_input = True
        print("Wanna just play it safe, fair enough")
    elif hit_or_stand.lower() == "stand":
        valid_input = True
        print("Wanna play it risky eh")
    else: 
        while valid_input == False:
            print("Just say either 'hit' or 'stand' you idiot you bufoon")
            hit_or_stand = input("Do you want to hit or stand")


            
    for randit in range(1):
        chamber = 1
     
    
    
































greeting()
rules()
terms_and_conditions()
choose_mode()