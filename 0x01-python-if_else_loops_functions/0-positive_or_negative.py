#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print(number)
if (number > 0):
	print("The number is positive")
	print("\n")
elif (number == 0):
	print("The number is zero")
	print("\n")
else: 
	print("the number is negative")
	print("\n")
