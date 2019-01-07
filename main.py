import time
import sys


def print_delay_text(text, delay=0.0):
    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(delay)


def print_intro():
    print("           .=    ,        =.")
    print("  _  _   /'/    )\,/,/(_   \ \ ")
    print("   `//-.|  (  ,\ )\//\)\/_  ) |")
    print("   //___\   `\ \/ \/\/ \///'  /")
    print(",-'~`-._ `'--'_   `'''`  _ \`''~-,_")
    print("\       `-.  '_`.      .'_` \ ,-'~`/")
    print(" `.__.-'`/   (-\        /-) |-.__,'")
    print("   ||   |     \O)  /^\ (O/  |")
    print("   `\  |         /   `\    /")
    print("     \  \       /      `\ /")
    print("      `\ `-.  /' .---.--.\ ")
    print("        `\/`~(, '()      ('")
    print("         /(O) \   _,.-.,_)")
    print("        //  \ `\ '`      /")
    print("       / |  ||   `''''~'`")
    print("     /'  |__||")
    print("           `o")
    print("\nWelcome to Bulls and Cows\n")
    return


def ask_player_experience():
    user_input = input("\nDo you know how to play? (y/n): \n")
    if user_input.lower() == 'y':
        print("user inputted 'yes'")  # TODO make this run the game
        return True
    elif user_input.lower() == 'n':
        return False
    else:
        print("Please enter either 'y' or 'n'")
        ask_player_experience()


def play_tutorial():
    time.sleep(1.5)
    print_delay_text("\nThat's okay. ", 2.0)
    print_delay_text("I can help you...\n\n", 2.5)
    print_delay_text("The goal of Bulls And Cows is to guess the isogram.\n", 2.6)
    print_delay_text("Isogram meaning a world with no repeating letters.\n", 3.0)
    print_delay_text("Every time you guess a letter that is inside the isogram\nand in the right place, you will get a Bull.\n", 4.0)
    print_delay_text("Every time you guess a letter that is inside the isogram\nbut in the wrong place, you will get a Cow.\n", 4.0)
    print_delay_text("Get all the letters in the right play and you win the game!\n", 2.6)
    print_delay_text("Got it?\n", 2.4)
    print_delay_text("Well then, get ready!\n\n")


print_intro()
if ask_player_experience() == True:
    print("the player knows how to play")
else:
    play_tutorial()