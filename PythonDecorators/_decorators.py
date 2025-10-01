def func(f):
    def wrapper(*args, **kwargs):
        print("Started")
        rv = f(*args, **kwargs)
        print("Finished")
        return rv
    return wrapper


@func
def func2(x, y):
    print(x)
    return y

@func
def func3(name = 'Ozan', age = 39):
    print(f"My Name is {name}, age = {age}")


x = func2(99, 1200)
print(x)

print('---->')
y = func3()
print(y)

