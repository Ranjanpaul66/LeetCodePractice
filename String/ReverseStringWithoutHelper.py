def reverse_string(string):
    reversed_str = ''
    for char in string:
        reversed_str = char + reversed_str
    return reversed_str

# Example usage:
original_string = "Hello, world!"
reversed_string = reverse_string(original_string)
# print(reversed_string)


def reverse(str):
    rev_str = ""
    for i in str:
        rev_str = i + rev_str
    return rev_str

print(reverse("tomk amr khub"))