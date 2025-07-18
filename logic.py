from secret_code import secret_code

def logic():    

    # We need to ensure that the user inputs EXACTLY 4 numbers

    code = secret_code()
    users_guess = [1,2,0,4]
    correct_position = 0
    correct_number = 0

    for i in range(4):
        code_num = code[i]
        user_num = users_guess[i]

        if code_num == user_num:
            correct_position+=1

    for num in users_guess:
        if num in code:
            correct_number += 1

    correct_number = correct_number - correct_position

    return f'secret_code: {code}, user_guess: {users_guess}, correct_number: {correct_number}, correct_pos: {correct_position}'
























print(logic())