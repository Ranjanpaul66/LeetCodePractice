# whether a string is Palindrome or not

# Using Slicing

string  = "nitin"

def checkPalindrome(str):
    if str == str[::-1]:
        print(str[::-1])
        return "Yes"
    else:
        return "No"

print(checkPalindrome(string))



def checkPalindrome2():
    length = len(string)
    i = 0
    while(i<=(length-1-i)):
        if string[i]!=string[length-1-i]:
            return False
        i=i+1;
    return True

print("Second ", checkPalindrome2())