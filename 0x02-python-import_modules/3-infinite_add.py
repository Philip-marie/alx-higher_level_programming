#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    total = 0

    # Loop through all arguments (starting from the first argument, excluding the script name)
    for i in range(1, len(argv)):
        total += int(argv[i])

    # Print the result followed by a new line
    print(total)
