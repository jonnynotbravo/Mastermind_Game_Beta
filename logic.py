from secret_code import secret_code

def logic():    

    # We need to ensure that the user inputs EXACTLY 4 numbers

    # code = secret_code() 
    code = [0, 1, 3, 5]
    users_guess = [0, 2, 4, 6]
    correct_position = 0
    correct_number = 0

    for i in range(4):
        code_num = code[i]
        user_num = users_guess[i]

        if code_num == user_num:
            correct_position+=1

    copy_code = code[:]

    for num in users_guess:
        if num in copy_code:
            correct_number += 1
            copy_code.remove(num)

    

    return f'secret_code: {code}, user_guess: {users_guess}, correct_number: {correct_number}, correct_pos: {correct_position}'
























print(logic())