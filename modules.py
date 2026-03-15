import os 
import math

cwd= os.getcwd()
print(f"Current working directory: {cwd}")

num= int(input("Enter an integer: "))

log= math.log2(num)

print(f"Log base 2 of {num} is: {log}")


floor = math.floor(log)
ceil = math.ceil (log)

print(f"Floor: {floor}")
print(f"Ceiling: {ceil}")