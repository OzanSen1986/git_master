class TestClass:
    def __init__(self):
        pass

class RegularClass:
    pass

def add(x, y):
    pass

def subtract(x, y):
    return x - y

def multiply(x, y):
    pass

def divide(x, y):
    pass

def power(x, y) -> None:
    return x ** y

any_func = lambda x, y: x + y


def CountDown(n):
    while n > 0 :
        yield n
        n -= 1

count = CountDown(5)
for n in count:
    print(n)


objects = [add, subtract, multiply, divide, power, TestClass, RegularClass, any_func,CountDown ,str, int, float, bool, print]

# for obj in objects:
#     print(f"{obj!r:30} callable: {callable(obj)}")


operations = [
    lambda x: x + 1,
    lambda x: x * 2,
    lambda x: x ** 2,
    str
]

value = 5
for op in operations:
    result = op(value)
    print(f"{op.__name__}({value}) = {result}")   





