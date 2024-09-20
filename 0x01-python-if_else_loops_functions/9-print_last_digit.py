#!/usr/bin/python3
def print_last_digit(number):
    # Get the last digit by taking the modulus of the absolute value
    last_digit = abs(number) % 10
    print(last_digit)  # Print the last digit
    return last_digit  # Return the last digit
