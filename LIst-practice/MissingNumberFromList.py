# This list is n Number. where list elements are ordered
def get_missing_summation(a):

    n = a[-1]
    sum1 = sum(a)
    total = n*(n+1)//2
    return total-sum1

print(get_missing_summation([1,2,3,4,5,6,7,9]))
