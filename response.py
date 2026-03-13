def input_response (secret_number, user_input):

    if user_input == secret_number:
        return "correct"
    elif user_input < secret_number:
        return "low"
    else :
        return "high"