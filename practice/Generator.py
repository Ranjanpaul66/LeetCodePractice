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


def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()

print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3

# The generator is now exhausted
try:
    print(next(gen))  # Raises StopIteration
except StopIteration:
    print("Generator exhausted")


# Attempting to iterate again will not work
for value in gen:
    print(value)  # Nothing will be printed
