def minDefElemnt(arr):
    arr = sorted(arr)
    size = len(arr)
    min_diff = 9999*999

    for i in range(size-1):
        if(arr[1+i]-arr[i]<min_diff):
            min_diff = arr[i+1] - arr[i]
    return min_diff

print(minDefElemnt([5,25,45,1,8,77]))