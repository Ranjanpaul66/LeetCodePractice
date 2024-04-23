from array import *

a = array("i", [1,2,6])
print(type(a))
print(a)

for x in a:
    print(x)

print("----")
for i in range(3):
    print(i)

print("--indexing---");

for j in range(3):
    print(a[j])

i=0
print("--while loop--")
while(i<len(a)):
    print(a[i])
    i+=1;

# append(), count(), extend(), fromlist(), index(), insert(), pop(), remove(), reverse(), tolist()

print("--append--")

a.append(45)
print(a)

print("--Count--")
# how many times 45 has in array
print(a.count(45))

print("--index--")

print(a.index(45))

print("--pop--")
# pop last element from the array
print(a.pop())
print(a)

# Can pop by index value
print(a.pop(1))

