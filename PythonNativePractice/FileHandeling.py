# file = open("non_existent_file.txt", "r")
# print(file.read())
# print(file.read(10))
# print(file.readline())
# print(file.readline())

# file = open("non_existent_file.txt", "a")
# print(file.write("\nBangla test"))
# file.close()
# file = open("non_existent_file.txt", "r")
# print(file.read())
# with open("non_existent_file.txt", "r") as file:
#     print("Before over write ---> ")
#     print(file.read())
# with open("non_existent_file.txt", "w") as file:
#     file.write("Over write the content")
#
# with open("non_existent_file.txt", "r") as file:
#     print(file.read())


def febnic(n):

    if n<=1:
        return n
    else:
        return (febnic(n-1)+febnic(n-2))

for i in range(5):
    print(febnic(i))