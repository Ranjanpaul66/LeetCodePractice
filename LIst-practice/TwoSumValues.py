def twoSum(arr, target):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while (left <= right):
        if (arr[left] + arr[right] > target):
            right = right - 1
        elif (arr[left] + arr[right] < target):
            left = left + 1
        else:
            print("left is: ", left, " right is ", right)
            right = right - 1
            left = left + 1


twoSum([5, 7, 4, 3, 9, 8, 19, 21], 17)


def againTwoSum(arr, target):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while (left <= right):
        if (arr[left] + arr[right] > target):
            right = right - 1
        elif (arr[left] + arr[right] < target):
            left = left + 1
        else:
            return "left :", left, " right : ", right


result = againTwoSum([5, 7, 4, 3, 9, 8, 19, 21], 17)

print(result)
