def decor1(func):
    def inner():
        x = func()
        return x * x

    return inner

def decor(func):
    def inner():
        x = func()
        return 2 * x

    return inner

def decor2(func):
    def inner():
        x = func()
        return x + 5

    return inner

@decor2
@decor1
@decor
def num():
    return 10


print(num())
