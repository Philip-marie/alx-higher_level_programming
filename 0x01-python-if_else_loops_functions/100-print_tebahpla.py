#!/usr/bin/python3
def print_reverse_alphabet():
    for i in range(25, -1, -1):  # Loop from 25 to 0
        print("{}".format(chr(122 - i) if i % 2 == 0 else chr(90 - i)), end="")


print_reverse_alphabet()
