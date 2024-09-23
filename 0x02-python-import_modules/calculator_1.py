#!/usr/bin/python3
def add(a, b):
    """Return the addition of a and b."""
    return a + b

def sub(a, b):
    """Return the subtraction of b from a."""
    return a - b

def mul(a, b):
    """Return the multiplication of a and b."""
    return a * b

def div(a, b):
    """Return the division of a by b."""
    if b == 0:
        return "Division by zero is undefined"
    return a / b
