from utils import *

mensaje= input("Please type your message\n")

men_invertido = flip(mensaje)

cant_a = count_letters(mensaje, 'a')

codificado= men_invertido + str(cant_a)

print(f"Your encoded message is: {codificado}")