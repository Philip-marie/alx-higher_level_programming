#!/usr/bin/python3

def print_last_digit(number):
    """Prints the last digit of a number and returns it."""
    if number < 0:
        number = -number  # Make number positive if it's negative
    last_digit = number % 10
    print(last_digit)
    return last_digit
