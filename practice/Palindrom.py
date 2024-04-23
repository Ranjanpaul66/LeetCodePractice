def is_palindrome(number):
    if number < 0:
        return False  # Negative numbers cannot be palindromes

    # Count the number of digits in the number
    num_digits = 0
    temp = number
    while temp > 0:
        num_digits += 1
        temp //= 10

    # Compare digits from the left and right ends
    left, right = number, 0
    for i in range(num_digits // 2):
        right_digit = left % 10
        left //= 10

        # Construct the number with digits reversed
        right = right * 10 + right_digit

    # If the number of digits is odd, we need to adjust 'left' to skip the middle digit
    if num_digits % 2 != 0:
        left //= 10

    return left == right


# Example usage:
number = 123321
print(is_palindrome(number))  # Output: True


# number = 12345
# print(is_palindrome(number))  # Output: False


def palindrome(n):
    temp = n
    rev_n = 0
    while (temp > 0):
        digit = temp % 10
        rev_n = rev_n * 10 + digit
        temp = temp // 10
    if n == rev_n:
        return True
    else:
        return False


print(palindrome(7894987))


# By using while loop

def palindromWhile(s):
    n = len(s)
    first = 0
    last = n - 1

    while (first < last):
        if s[first] == s[last]:
            first += 1
            last -= 1
        else:
            return False
    return True
