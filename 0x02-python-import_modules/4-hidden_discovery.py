#!/usr/bin/python3
import sys
import hidden_4

if __name__ == "__main__":
    # Get all names from the module
    names = dir(hidden_4)

    # Filter names that do not start with '__'
    filtered_names = [name for name in names if not name.startswith('__')]

    # Sort the names alphabetically
    filtered_names.sort()

    # Print each name on a new line
    for name in filtered_names:
        print(name)
