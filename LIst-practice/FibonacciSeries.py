# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
def feb(num):

    ls = [0,1]
    i=2

    if(num <=1):
        return num

    while(i<=num-1):
       newElement = ls[i-2] + ls[len(ls)-1]
       ls.append(newElement)
       i+=1

    return ls

print(feb(10))


# with recursion

def febRecursion(num):
    if(num<0):
        return "Invalid"
    if (num<=1):
        return num
    else:
        return febRecursion(num-1)+ febRecursion(num-2)

increment = 0
num =10
while(increment<=num-1):
    print(febRecursion(increment), end=" ")
    increment+=1
