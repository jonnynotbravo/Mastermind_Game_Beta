from secret_code import secret_code

def logic():    

    # Ensure that the user inputs EXACTLY 4 numbers betweem 0 - 7 with no spaces
    while True:
        user_input = input("Enter your guess: ")
        
        if (' ' in user_input or 
            len(user_input) != 4 or 
            not user_input.isdigit() or 
            not all(0 <= int(digit) <= 7 for digit in user_input)):
            print("Invalid! Enter exactly 4 digits (0-7) with no spaces.")
            continue
        
        user_guess = [int(x) for x in user_input]
        break
    
    # Secret code
    code = secret_code() 


    # Logic
    correct_location = 0
    correct_number = 0

    for i in range(4):
        code_num = code[i]
        user_num = user_guess[i]

        if code_num == user_num:
            correct_location+=1

    copy_code = code[:]

    for num in user_guess:
        if num in copy_code:
            correct_number += 1
            copy_code.remove(num)

    

    return f'secret_code: {code}, user_guess: {user_guess}, correct_number: {correct_number}, correct_pos: {correct_location}'
























print(logic())