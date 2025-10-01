import sys

def gen(n):
    for i in range(n):
        yield i ** 2

lst = (i ** 2 for i in range(1000))

items = [1, 2, 3]


g = gen(1000)
print(next(g))  # Output: 0
print(sys.getsizeof(g))  # Size of the generator object
print(sys.getsizeof(lst))  # Size of the list object
print(sys.getsizeof(items))  # Size of the list object
print(next(g))























