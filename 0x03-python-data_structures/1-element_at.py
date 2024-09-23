#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Replace an element in a list at a specific position."""
    # Check if the index is valid
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return my_list

# Example usage
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    
    # Valid replacement
    print(replace_in_list(my_list, 2, 99))  # Output: [1, 2, 99, 4, 5]

    # Negative index (no modification)
    print(replace_in_list(my_list, -1, 100))  # Output: [1, 2, 99, 4, 5]

    # Out of range index (no modification)
    print(replace_in_list(my_list, 5, 100))  # Output: [1, 2, 99, 4, 5]

    # Valid replacement at start
    print(replace_in_list(my_list, 0, 100))  # Output: [100, 2, 99, 4, 5]
