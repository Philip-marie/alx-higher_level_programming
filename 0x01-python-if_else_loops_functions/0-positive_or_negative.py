#!/usr/bin/python3
import random

number = random.randint(-10, 10)  # This line is provided

# Complete the code below
print(number, end=" ")
if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")
