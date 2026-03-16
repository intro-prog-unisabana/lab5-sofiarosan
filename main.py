from utils import *


while True:
    operation= input("Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):").strip().lower()

    if operation=="exit":
        break
    
    if operation not in ["add" , "subtract", "multiply", "divide", "exponent", "modulo", "floor_divide", "absolute",]:
        print("Invalid option!")
        continue
    if  operation =="absolute":
         num= float(input("Enter the number:"))
         result = absolute(num)
         print ("The result is:", result)
         continue
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))

    if operation=="add":
        result= add(num1, num2)
    elif operation== "subtract":
        result= subtract(num1, num2)
    elif operation == "multiply":
        result = multiply(num1, num2)
    elif operation == "divide":
        result = divide(num1, num2)
    elif operation== "exponent":
        result = exponent(num1, num2)
    elif operation == "modulo" :
        result = modulo(num1, num2)
    elif operation == "floor_divide" :
        result == floor_divide(num1, num2)
    
    if isinstance (result, str):
        print(result)
    else:
        print("The result is:", result)