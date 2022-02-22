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
    return 5


print(num())

# def plus_one(number):
#      # def add_one(x):
#     #     return x + 1
#     #     return number + x
#     return number + 4
#
# result = plus_one
#
# print(plus_one(4))