#!/usr/bin/python3
def remove_char_at(str, n):
    # If n is out of bounds, return the original string
    if n < 0 or n >= len(str):
        return str

    # Create a new string without the character at position n
    return str[:n] + str[n + 1:]


# Example usage
result = remove_char_at("Hello, World!", 7)
print(result)  # Output: "Hello, World"
