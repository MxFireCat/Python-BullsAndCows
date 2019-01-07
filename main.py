import time
import sys


def print_delay_text(text, delay=0.0):
    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(delay)


def print_intro():
    print("          .=     ,        =.")
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
        print("user inputted 'no'")  # TODO make this run the tutorial
        return False
    else:
        print("Please enter either 'y' or 'n'")
        ask_player_experience()


def play_tutorial():
    time.sleep(1.5)
    print_delay_text("That's okay. ", 1.0)
    print_delay_text("I can help you\n")


print_intro()
if ask_player_experience() == True:
    print("the player knows how to play")
else:
    play_tutorial()