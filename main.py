from time import sleep
from random import randint, choice
from colorama import Back, Fore, Style



def print_letter_by_letter(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        sleep(delay)
    print()


def greeting():



    print_letter_by_letter("Hello There")
    print_letter_by_letter("It seems that you've decided to challenge me to a duel in russian roulette")
    comfirm_begin = input("Is that true? ")
    if comfirm_begin.lower() == "yes":
        print_letter_by_letter("Very well, let's begin")
    elif comfirm_begin.lower() == "no":
        print_letter_by_letter("You intolerate buffoon, wasting my time. Back to where you come from")
        print_letter_by_letter(Fore.RED  + "*YOU HAVE BEEN BANISHED FROM THIS WORLD*")
        quit()
    else:
        print_letter_by_letter("I don't speak this language wit thy tounge. Either say yes or no like a normal person would. You impertinent fool! ")
        print_letter_by_letter("If you fail again, I'm going to banish you from this world.")
        
        bad_greeting()
        
def bad_greeting():
    print_letter_by_letter("So, will you continue and possibly shine amongst the light, or drown within the depths of the ocean.")
    comfirm_begin = input("Are you going to battle me? ")
    if comfirm_begin.lower() == "yes":
        print_letter_by_letter("Very well, took you a while but your tiny brain got there in the end.")
    else:
        print_letter_by_letter("To the streets of hell you go.")
        print_letter_by_letter(Fore.RED  + "*YOU HAVE BEEN BANISHED FROM THIS WORLD*")
        quit()


def rules():
    print("")
    print("----------------------------------------------------------------------------------------------------------------")
    print(" ")
    print_letter_by_letter("The rules of russian roulette are ⬇️")
    print_letter_by_letter("1.You will be going against the master of russian roulette AKA me. ")
    print_letter_by_letter("2. You can either hit, meaning you can shoot me or you can stand, which makes you shoot yourself")
    print_letter_by_letter("3. We will go in turns. You will always go first as you are our guest. ")
    print_letter_by_letter("4. You and I will both have 3 lives, everytime you get shot you will lose 1 life.")
    print_letter_by_letter("5. First person to lose all their lives, loses.")
    print_letter_by_letter("   If you win, You will be held as king and I will be banished from this world. ")
    print_letter_by_letter("   If I win, you will be banished from this world and I will continue to rule over the land.")
    print("")
    print("----------------------------------------------------------------------------------------------------------------")
    
def terms_and_conditions():

    print("                                                                                             ")
    print_letter_by_letter("Here are the terms and conditions ⬇️")
    print_letter_by_letter("1. You must follow the rules of the game. Any rules not followed will result in an immediate ban. ")
    print_letter_by_letter("2. Any thing that may happen to your device internally or externally will not be our fault.")
    print_letter_by_letter("3. You must not impersonate anyone.")
    print_letter_by_letter("4. Later depending on your further choices, somethings may change to your display")
    print_letter_by_letter("5. Things may be said to you which may emotionally harm you, which could lead you to harm yourself phyically.")
    print_letter_by_letter("This will not be ou fault. And please do not harm yourself. If you need help, please call +852 2343 2255 ")
    print_letter_by_letter(" ")
    print("----------------------------------------------------------------------------------------------------------------")
    print_letter_by_letter(" ")
    print_letter_by_letter("Would you like to accept these terms of conditons? ")
    proceed = input("Please answer as yes. Anything else entered will result in you being banished ")
    if proceed.lower() == "yes":
        signature = input("Please sign here to comfirm. ")
        print_letter_by_letter(f"Very well {signature}. Let's begin.")
    else:
        print_letter_by_letter(Fore.RED  + "*YOU HAVE BEEN BANISHED FROM THIS WORLD*")
        quit()

def choose_mode():
    global mode_chosen
    
    print("")
    print_letter_by_letter("Now that you must choose a mode. Safe or Risky.")
    print("----------------------------------------------------------------------------------------------------------------")
    print_letter_by_letter("Here are the differences.")
    print("")
    sleep(0.7)
    print_letter_by_letter("Safe mode")
    print("")
    print_letter_by_letter("In safe mode, If you win, your screen will flash rainbow for a few seonds only.")
    print_letter_by_letter("But if you die. It will simply say that you've died.")
    print("----------------------------------------------------------------------------------------------------------------")
    print_letter_by_letter("Risky mode")
    print("")
    print_letter_by_letter("I won't give so much detail, but all I will say the higher the difficulty, the higher reward but also the higher concequence.")
    print("----------------------------------------------------------------------------------------------------------------")
    mode_chosen = input("So. What mode do you choose, safe or risky. ")
    if mode_chosen.lower() == "safe":
        print("")
        print_letter_by_letter("I see that you don't got the guts to play risky.")
        print_letter_by_letter("But I guess I'll understand since you're just a mortal being.")
        sleep(0.7)
        safe()
        
    elif mode_chosen.lower() == "risky":
        print("")
        print_letter_by_letter("You've got guts")
        print_letter_by_letter("And I like that.")
        sleep(0.7)
        risky()
    else:
        print_letter_by_letter("Another idiot wasting my time. ")
        print_letter_by_letter(Fore.RED  + "*YOU HAVE BEEN BANISHED FROM THIS WORLD*")
        quit()

def safe():
    print_letter_by_letter("I see that you shiver in your boots")
    print_letter_by_letter("But lets get into the game")
    print("----------------------------------------------------------------------------------------------------------------")
    sleep(0.7)

    main_game()

def risky():
    print_letter_by_letter("I see you want to face me head on.")
    print_letter_by_letter("I like that, let now continue the game.")
    print("----------------------------------------------------------------------------------------------------------------")
    sleep(0.7)
    
    main_game()
    
def main_game():
    global hit_or_stand
    global bot_lives
    global player_lives
    print_letter_by_letter("I have already told you the rules of the games. ")
    print("")
    print_letter_by_letter("Now Let's begin")
    
    
    
    bot_lives = 3
    player_lives = 3
    
    the_chamber = ["blank"] * 6
    
    while True:
        valid_input = False
        hit_or_stand = input("Do you want to hit or stand: ")
        if hit_or_stand.lower() == "hit":
            valid_input = True
            print_letter_by_letter("Wanna just play it safe, fair enough")
            break
        elif hit_or_stand.lower() == "stand":
            valid_input = True
            print_letter_by_letter("Wanna play it risky eh")
            break
        else: 
            print_letter_by_letter("Just say either 'hit' or 'stand' you idiot you buffoon")
    
    chamber_result = chamber(the_chamber)
    resolve_outcome(chamber_result)


def chamber(the_chamber):

    bullet_position = choice(range(6))
    the_chamber[bullet_position] = "full"

    print_letter_by_letter("The chamber has been loaded")
    return the_chamber[bullet_position]

def resolve_outcome(chamber_result):
    global bot_lives
    global player_lives
    global hit_or_stand
    

    if chamber_result == "full" and hit_or_stand.lower() == "hit":
        print_letter_by_letter("You shot me, that was just luck")
        bot_lives -= 1
    
    elif chamber_result == "full" and hit_or_stand.lower() == "stand":
        print_letter_by_letter("Ouch, that was just unlucky")
        bot_lives -= 1
    elif chamber_result == "blank" and hit_or_stand.lower() == "hit":
        print_letter_by_letter("You hit me, but I was lucky ... I mean skillful and didn't get shot.")
    elif chamber_result == "blank" and hit_or_stand.lower() == "stand":
        print_letter_by_letter("You stood, nothing happened, little lucky son of a biscuit.")
        
    else:
        print_letter_by_letter("Something went wrong, you idiot. You should never have come here in the first place.")
        print_letter_by_letter(Fore.RED  + "*YOU HAVE BEEN BANISHED FROM THIS WORLD*")
        quit()

    if bot_lives <= 0:
        print_letter_by_letter("You have won, you are the king of this land now.")
        if mode_chosen.lower() == "safe":
            print_letter_by_letter("Your screen will now flash rainbow for a few seconds")
            
        elif mode_chosen.lower() == "risky":
            print_letter_by_letter("You have won, you are the king of this land now.")
            print_letter_by_letter("But I will not let you go so easily, I will haunt you forever. ")
            print_letter_by_letter("You will never be able to escape me, I will always be there in your dreams. ")
        else:
            print_letter_by_letter("Something went wrong, you idiot. You should never have come here in the first place.")
            print_letter_by_letter(Fore.RED  + "*YOU HAVE BEEN BANISHED FROM THIS WORLD*")
            quit()

    
    elif player_lives <= 0:
        print_letter_by_letter("You have lost, you are a disgrace to this land.")
        if mode_chosen.lower() == "safe":
            print_letter_by_letter("Your screen will now flash red for a few seconds")
            for _ in range(5):
                sleep(0.2)
        elif mode_chosen.lower() == "risky":
            print_letter_by_letter("You have lost, you are a disgrace to this land.")
            print_letter_by_letter("I will haunt you forever, you will never be able to escape me, I will always be there in your dreams. ")
        else:
            print_letter_by_letter("Something went wrong, you idiot. You should never have come here in the first place.")
            print_letter_by_letter(Fore.RED  + "*YOU HAVE BEEN BANISHED FROM THIS WORLD*")
            quit()
    else:
        print_letter_by_letter(f"You have {player_lives} lives left, I have {bot_lives} lives left.")
        print_letter_by_letter("Now it's my turn to shoot you, let's see if you are lucky or not.")
        sleep(1)
        
        bot_turn()
def bot_turn():
    global bot_lives
    global player_lives
    global hit_or_stand
    
    the_chamber = ["blank"] * 6


    
    hit_or_stand = choice(["hit", "stand"])
    
    if hit_or_stand == "hit":
        print_letter_by_letter("I have chosen to hit you, let's see if you are lucky or not.")
    else:
        print_letter_by_letter("I have chosen to stand, let's see if you are lucky or not.")
    
    chamber_result = chamber(the_chamber)
    resolve_outcome(chamber_result)
    if bot_lives <= 0 or player_lives <= 0:
        return
    else:
        main_game()

        



























greeting()
rules()
terms_and_conditions()
choose_mode()