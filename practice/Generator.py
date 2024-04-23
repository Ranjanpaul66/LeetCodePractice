def fib(n):

    a, b = 0,1
    i = 1
    while(i<=n):
        yield a
        a,b = b, a+b
        i += 1

# there are tow way to iterate

for i in fib(10):
    print(i)


# this way to we can get StopIteration exception
test = fib(2)
print(test.__next__())
print(test.__next__())
# print(test.__next__())