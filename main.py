import time
import sys


#global variables

#TODO constructor
win_state = 0 # TODO change to enum


def print_delay_text(text, delay=0.0):
    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(delay)


def print_intro():
    print("           .=    ,        =."        )
    print("  _  _   /'/    )\,/,/(_   \ \ "     )
    print("   `//-.|  (  ,\ )\//\)\/_  ) |"     )
    print("   //___\   `\ \/ \/\/ \///'  /"     )
    print(",-'~`-._ `'--'_   `'''`  _ \`''~-,_" )
    print("\       `-.  '_`.      .'_` \ ,-'~`/")
    print(" `.__.-'`/   (-\        /-) |-.__,'" )
    print("   ||   |     \O)  /^\ (O/  |"       )
    print("   `\  |         /   `\    /"        )
    print("     \  \       /      `\ /"         )
    print("      `\ `-.  /' .---.--.\ "         )
    print("        `\/`~(, '()      ('"         )
    print("         /(O) \   _,.-.,_)"          )
    print("        //  \ `\ '`      /"          )
    print("       / |  ||   `''''~'`"           )
    print("     /'  |__||"                      )
    print("           `o"                       )
    print("\nWelcome to Bulls and Cows\n")
    return


def does_player_know_how_to_play():
    user_input = input("\nDo you know how to play? (y/n): \n")
    if user_input.lower() == 'y':
        return True
    elif user_input.lower() == 'n':
        return False
    else:
        print("Please enter either 'y' or 'n'")
        does_player_know_how_to_play()


def play_tutorial():
    time.sleep(1.5)
    print_delay_text("\nThat's okay. ", 2.0)
    print_delay_text("I can help you...\n\n", 2.5)
    print_delay_text("The goal of Bulls And Cows is to guess the isogram.\n", 2.6)
    print_delay_text("Isogram meaning a world with no repeating letters.\n", 3.0)
    print_delay_text("Every time you guess a letter that is inside the isogram\nand in the right place, you will get a Bull.\n", 4.0)
    print_delay_text("Every time you guess a letter that is inside the isogram\nbut in the wrong place, you will get a Cow.\n", 4.0)
    print_delay_text("Get all the letters in the right place and you win the game!\n", 2.6)
    print_delay_text("Got it?\n", 2.4)
    print_delay_text("Well then, get ready!\n\n", 1.8)


def play_game():
    if input("does the player win??: ") == 'y':
        return True # TODO change to enum
    else:
        return False


def print_summary():
    if win_state == True:
        print("you win")
    else:
        print("you lose")


def ask_to_play_again():
    if input("do you want to play again: ").lower() == 'y':
        return True
    else:
        return False


print_intro()
while True:
    if does_player_know_how_to_play() == True:
        win_state = play_game()
    else:
        play_tutorial()
        win_state = play_game()
    print_summary()
    play_again = ask_to_play_again()
    if play_again == False:
        break