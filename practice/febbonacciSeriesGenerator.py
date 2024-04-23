def fact():
    a, b = 0, 1
    while True:
        yield a
        a, b =b, a+b

f1 = fact()
print(f1.__next__())  # next(f1)
print(f1.__next__())
print(f1.__next__())
print(f1.__next__())
print(type(f1.__next__()))


def gen(n):
    count = 0
    while count<=n:
        yield count
        count+=1

ge = gen(5)

for i in ge:
    print(i)


iter_list = iter(['A', 'B', 'C'])
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))


