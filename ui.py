import os
import platform

# Clearing CLI for the user
def clear_screen():
    # For Windows
    if platform.system() == "Windows":
        os.system("cls")
    # For other OS
    else:
        os.system("clear")


def ui():
    # Welcome 
    width=50
    print("=".center(width,"="))
    print("WELCOME TO MASTERMIND GAME".center(width))
    print("=".center(width, "="))

    # Instructions
    print("\nHOW TO PLAY:\n")
    print('- A Secret Code has been picked by the computer: 4 numbers between 0 and 7')
    print('- Your mission is to guess the correct combination')
    print('- Numbers may be repeated (Duplicates are allowed)')
    print('- You have 10 attempts to find the correct combination')
    print('- Goodluck!\n\n')
    start_game()
    clear_screen()



# Press Enter to start the game
def start_game():
    start = input('PRESS[ENTER] OR [SPACE] TO START THE GAME')

    while True:
        if start == '' or start == ' ':
            break


    



if __name__ == "__main__":
    clear_screen()
    ui()  



