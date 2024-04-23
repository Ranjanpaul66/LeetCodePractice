a = "TestTesst"
b= "PeopleTest"

def uniq(a,b):
    res = set(a.lower())
    print(res)
    res2 = set(b.lower())
    print(res2)

    return res & res2
# print(uniq(a,b))

""" How to check max no of repeated letter and repeated total no in string """

def multipleCount(a):
    dic = {}
    for i in a:
        if i in dic:
            dic[i] +=1
        else:
            dic[i] = 1
    print(dic)
    return dic

my_dict = multipleCount(a)

# my_dict = {'a': 10, 'b': 25, 'c': 15}

max_key = max(my_dict, key=my_dict.get)
max_value = my_dict[max_key]

print(f"The key with the maximum value is: {max_key}")
print(f"The maximum value is: {max_value}")
