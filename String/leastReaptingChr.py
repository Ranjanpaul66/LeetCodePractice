#least repeating charecter in String

# Best Practice
def leastRepeatChar(s):

    dic = {}
    for i in s:
        if i in dic:
            dic[i] = dic[i] + 1
        else:
            dic[i] = 1
    # print(dic)
    result = min(dic, key=dic.get)
    return result


s = "testbbanngladeshx"
# print(leastRepeatChar(s))


#using inbuilt funtion

from collections import Counter
str = "aabccdeessddw"
ch = Counter(str)
print("ch: ", ch)
result = min(ch, key=ch.get)
# print(result)


# without using count/ Using dict

def SpecifecChar(s, ch):
    dic = {}
    for i in s:
        if i in dic:
            dic[i] = dic[i] + 1
        else:
            dic[i] = 1

    return dic.get(ch)

print(SpecifecChar("aabbccddeeeffffg", "f"))