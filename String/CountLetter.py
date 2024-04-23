# Count no of occurance of character in a string and print each character

string = "stringhettsttad"
dic = {}


for i in string:
    if i in dic:
        dic[i]= dic[i]+1
    else:
        dic[i]=1

print(dic)