#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    arg_count = len(argv) - 1

    # Print the number of arguments
    if arg_count == 0:
        print("0 arguments.")
    elif arg_count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg_count))

    # Loop through arguments and print them with their position
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
