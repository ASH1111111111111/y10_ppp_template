import os # 
import platform
from time import sleep
from random import randint, choice
from colorama import Fore, Back, Style, init

init()
## flashes rainbow colours in the terminal when you win
def flash_rainbow():
    #list of all colours that will flash in the rainbow.
    rainbow_colours = [
        Back.RED,
        Back.YELLOW,
        Back.GREEN,
        Back.CYAN,
        Back.BLUE,
        Back.MAGENTA,
    ]
    # loop that will flash the colours in the terminal
    for i in range(1000):
        for colour in rainbow_colours:
            print(colour + " " * 10000, end='\r' )
            sleep(0.1)
            print(Style.RESET_ALL)

# funcion that shuts down computer when the user loses in risky mode
def forced_shutdown():
    print_letter_by_letter(Fore.RED + "YOU HAVE LOST. YOUR COMPUTER IS SHUTTING DOWN IN 5 SECONDS")
    sleep(3)
    last_request = input("Do you accept this like a True man? Click Enter if you accept, otherwise type anything to cancel it.")
    if last_request == "":
        if platform.system() == "Windows": # Checks if your os system is windows
            os.system("shutdown /s /t 1") # shuts down your computer for windows
        elif platform.system() == "Darwin":# checks if your os system is Mac OS
            os.system("sudo shutdown -h now")
        else:
            print_letter_by_letter("I was testing you like a true man. But if you really want to have the full expierence, run this code in the MAC OS terminal or the Command prompt on WINDOWS OS")
    else:
        print("You are a coward you dissapointment")
        quit()

def print_letter_by_letter(text, delay=0.000005):
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
    print_letter_by_letter("Any Data lost will not be our fault")
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
    print_letter_by_letter("Now you must choose a mode. Safe or Risky.")
    print("----------------------------------------------------------------------------------------------------------------")
    print_letter_by_letter("Here are the differences.")
    print("")
    sleep(0.7)
    print_letter_by_letter(Fore.GREEN + "Safe mode")
    print("")
    print_letter_by_letter(Fore.GREEN + "In safe mode, If you win, your screen will flash rainbow for a few seonds only.")
    print_letter_by_letter(Fore.GREEN + "But if you die. It will simply say that you've died.")
    print("----------------------------------------------------------------------------------------------------------------")
    print_letter_by_letter(Fore.LIGHTRED_EX + "Risky mode")
    print("")
    print_letter_by_letter(Fore.LIGHTRED_EX + "I won't give so much detail, but all I will say the higher the difficulty, the higher reward but also the higher concequence.")
    print(Fore.RESET + "----------------------------------------------------------------------------------------------------------------")
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
    
    while player_lives > 0 and bot_lives > 0:
        player_turn()
        if bot_lives <= 0:
            break
        bot_turn()
    if bot_lives <= 0:
        print_letter_by_letter("You have won, you are the king of this land now.")
        if mode_chosen.lower() == "safe":
            sleep(0.1)
            flash_rainbow()
            
        elif mode_chosen.lower() == "risky":
            print_letter_by_letter("You have won, you are the king of this land now.")
            print_letter_by_letter("But I will not let you go so easily, I will haunt you forever. ")
            print_letter_by_letter("You will never be able to escape me, I will always be there in your dreams. ")
            flash_rainbow()
            sleep(0.3)
    elif player_lives <= 0:
        print_letter_by_letter("You have lost, you are a disgrace to this land.")
        if mode_chosen.lower() == "safe":
            red_flash = [Back.RED]
            for i in range(1000):
                for colour in red_flash:
                    print(colour + " " * 1000, end='\r' )
                    sleep(0.1)
                    print(Style.RESET_ALL)

            for _ in range(5):
                sleep(0.2)
        elif mode_chosen.lower() == "risky":
            print_letter_by_letter("You have lost, you are a disgrace to this land.")
            print_letter_by_letter("I will haunt you forever, you will never be able to escape me, I will always be there in your dreams. ")
            forced_shutdown()
          
        

def chamber():

    return choice(["full", "blank"])

def resolve_outcome(chamber_result, action, is_player_turn):
    global bot_lives
    global player_lives

    
    if is_player_turn:
        if chamber_result == "full" and action == "hit":
            print_letter_by_letter("You shot me, that was just luck")
            bot_lives -= 1
        elif chamber_result == "full" and action == "stand":
            print_letter_by_letter("Ha Ha, I new it, you silly little mortal")
            player_lives -= 1
        elif chamber_result == "blank" and action == "hit":
            print_letter_by_letter("You really tried? I was lucky ... I mean skillful and didn't get shot.")
        elif chamber_result == "blank" and action == "stand":
            print_letter_by_letter("You stood, nothing happened, little lucky son of a biscuit.")
            
        else:
            print_letter_by_letter("Something went wrong, you idiot. You should never have come here in the first place.")
            print_letter_by_letter(Fore.RED  + "*YOU HAVE BEEN BANISHED FROM THIS WORLD*")
            quit()

        print_letter_by_letter(f"You have {player_lives} lives left, I have {bot_lives} lives left.")

    else:
        if chamber_result == "full" and action == "hit":
            print_letter_by_letter("Aha, I've shot you, that was all skill")
            player_lives -= 1
        elif chamber_result == "full" and action == "stand":
            print_letter_by_letter("Ow, I shot myself, well that was on purporse because I'm just better")
            bot_lives -= 1
        elif chamber_result == "blank" and action == "hit":
            print_letter_by_letter("That gun is rigged you know")
        elif chamber_result == "blank" and action == "stand":
            print_letter_by_letter("I shot my self, and nothing happened. I'm so sigma.")
            
        else:
            print_letter_by_letter("Something went wrong, you idiot. You should never have come here in the first place.")
            print_letter_by_letter(Fore.RED  + "*YOU HAVE BEEN BANISHED FROM THIS WORLD*")
            quit()

        print_letter_by_letter(f"You have {player_lives} lives left, I have {bot_lives} lives left.")
    
        

def player_turn():
    valid_input = False
    while not valid_input:
        hit_or_stand = input("Do you want to hit or stand: ")
        if hit_or_stand.lower() in ["hit", "stand"]:
            valid_input = True
            chamber_result = chamber()
            resolve_outcome(chamber_result, hit_or_stand.lower(), True)
        else:
            print_letter_by_letter("Just say hit or stand you idiot")



def bot_turn():

    hit_or_stand = choice(["hit", "stand"])
    if hit_or_stand == "hit":
        print_letter_by_letter("I have decided to hit, Lets see if fate is on your side")
    else:
        print_letter_by_letter("I have choosen to stand, I know I'm safe")
    
    chamber_result = chamber()
    resolve_outcome(chamber_result, hit_or_stand, False)
   

        



























greeting()
rules()
terms_and_conditions()
choose_mode()