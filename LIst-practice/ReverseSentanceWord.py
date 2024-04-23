def reverse(str_r):
    str_r = str_r[::-1]
    return str_r


# print(reverse("Netsetos is excellent"))


""" Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc" """


def reverseWords(s: str) -> str:
    list = s.split()
    res = ""
    for i in list:
        res = res + i[::-1]
        # if (len(list) - 1 != i):
        res += " "
    return res[:-1]


word = "s'teL ekat edoCteeL tsetnoc"
print("hel: ", reverseWords(word))


def reverseWords2(s: str) -> str:
    words = s.split()  # split the string into a list of words
    reversed_words = [word[::-1] for word in words]  # reverse each word using list comprehension
    return ' '.join(reversed_words)


print("reverseWords2 : ", reverseWords2("s'teL ekat edoCteeL tsetnoc"))


def reverseOptimize(str):
    s = list(str)
    l = 0
    for r in range(len(s)):
        if s[r] == " " or r == len(s) - 1:
            temp_l, temp_r = l, r - 1
            if r == len(s) - 1:
                temp_r = r
            while temp_l < temp_r:
                s[temp_l], s[temp_r] = s[temp_r], s[temp_l]
                temp_l += 1
                temp_r -=1

            l = r+1
    return "".join(s)

print("reverseOptimize: " , reverseOptimize("s'teL ekat edoCteeL tsetnoc"))
