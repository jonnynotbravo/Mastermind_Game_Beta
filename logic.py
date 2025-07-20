import os
import platform

from secret_code import secret_code


# Clearing CLI for the user
def clear_screen():
    # For Windows
    if platform.system() == "Windows":
        os.system("cls")
    # For other OS
    else:
        os.system("clear")



def logic():
    # Secret code
    code = secret_code()
    
    history = {}
    # User has 10 attempts to win
    attempts = 10
    
    while attempts > 0:
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
            
            user_guess = [int(x) for x in user_input]
            clear_screen()
            break
        
        # Logic
        correct_location = 0
        correct_number = 0
        
        # Check for correct positions
        for i in range(4):
            code_num = code[i]
            user_num = user_guess[i]
            
            if code_num == user_num:
                correct_location += 1
        
        # Check for correct numbers (including correct positions)
        copy_code = code[:]
        for num in user_guess:
            if num in copy_code:
                correct_number += 1
                copy_code.remove(num)
        
        # Store feedback in history
        prev_guess = ''.join(map(str, user_guess))
        feedback = f"{correct_number} correct number(s), {correct_location} correct location(s)"
        history[prev_guess] = feedback
        
        # Show guess history
        if history:
            print("\n" + "="*55)
            print("History of Guesses and their feedback".center(50))
            print("="*55)
  
            for prev_guess, feedback in history.items():
                print(f"Guess: {prev_guess} -> Feedback: {feedback}")
            print("="*70 + "\n")
        
        # print(f"\nCurrent Guess Result: {correct_number} correct number and {correct_location} correct location")
        
        # Check if won
        if correct_location == 4:
            return 'You Win!!!'
        
        # Decrease attempts AFTER processing the guess
        attempts -= 1
    
    return 'Game Over'

print(logic())