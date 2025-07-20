from secret_code import secret_code
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

# Main Logic
def logic():
    # Secret code
    code = secret_code()

    # Data set to put history of guesses and their feedback
    attempts_history = {}

    # Number of attempts to win
    attempts = 10
    
    while attempts > 0:
        # Clear screen only if not a winning guess
        clear_screen()

        # Instruction for the user
        print("The Secret Code has been Generated...")
        print("Instructions: Enter 4 digits between 0-7 with no spaces\n")

        # Show attempts history and their feedback
        if attempts_history:
            print("" + "="*55)
            print("History of Guesses and their feedback".center(50))
            print("="*75)

            for prev_guess, feedback in attempts_history.items():
                print(f"Your Guess: {prev_guess} -> Feedback: {feedback}")
            print("="*75 + "\n")

        # Display number of attempts left
        print(f"Attempt: {attempts}")
        
        # Ensure that the user inputs EXACTLY 4 numbers between 0 - 7 with no spaces
        while True:
            user_input = input("Enter your guess: ")
            
            if (' ' in user_input or
                len(user_input) != 4 or
                not user_input.isdigit() or
                not all(0 <= int(digit) <= 7 for digit in user_input)):
                print("Invalid! Enter exactly 4 digits (0-7) with no spaces.")
                continue
            
            # Convert user input to a list of integers
            user_guess = [int(x) for x in user_input]
            break
        
        # Logic

        # Data to hold the correct numbers and correct positions
        correct_number = 0
        correct_location = 0

        # Check for correct positions
        for i in range(4):
            code_num = code[i]
            user_num = user_guess[i]
            
            if code_num == user_num:
                correct_location += 1
        
        # Check for correct numbers
        copy_code = code[:]
        for num in user_guess:
            if num in copy_code:
                correct_number += 1
                copy_code.remove(num)

        # Check if won
        if correct_location == 4:
            return f"\nYou Win!!! The Secret Code was {''.join(map(str, code))}\n"
        
        # Store feedback in history
        prev_guess = ''.join(map(str, user_guess))
        feedback = f"{correct_number} correct number(s), {correct_location} correct location(s) {code}"
        attempts_history[prev_guess] = feedback

        # Decrease attempts if the guess is incorrect(Keep looping)
        attempts -= 1
    
    return f'\nGame Over!\nYou have failed to guess the combination in 10 attempts!\nThe Secret Code was {''.join(map(str, code))}\n'


if __name__ == "__main__":
    clear_screen()
    print(logic())