from logic import logic, clear_screen

# User Interface
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
    
    # Wait for user to start
    press_to_start()
    
    # Clear screen and start the actual game
    clear_screen()
    
    # Print The result of the game
    result = logic()
    print(result)
    
    
    
# Ask the user to start the game 
def press_to_start():
    start = input('PRESS [ENTER] TO START THE GAME: ')
    
    # Check if they pressed [Enter]
    if start == "":
        return  
    else:
        # Ask again if they didn't press [Enter]
        return press_to_start()  


# clear the screen when the game is ran
if __name__ == "__main__":
    clear_screen()
    ui()





