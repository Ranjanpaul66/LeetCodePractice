def reverse_string(string):
    reversed_string = ''
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string

# Example usage:
original_string = "hello"
reversed_string = reverse_string(original_string)
print(reversed_string)  # Output: olleh

print(original_string[::-1])