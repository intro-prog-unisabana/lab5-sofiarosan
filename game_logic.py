
from secret_number import generate_secret_numbers
from response  import input_response

print("Enter a seed number: ")
seed = int(input())

secret_number = generate_secret_numbers(seed)

i=0 
while True:
    print("What is your guess: ")
    user_input = int(input())
    i+=1

    result= input_response(secret_number, user_input)

    if result == "correct":
        print ("Correct! You guessed the number!")
        break
    elif result == "low":
        print ("Too low! Try a higher number.")
        continue
    else:
        print ("Too high! Try a lower number.")

print(f"It took you {i} tries!")