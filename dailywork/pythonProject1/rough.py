# d = []
# def deco(x):
#     def inner():
#         nu = x()
#         if nu <= 1:
#             return 1
#             d.apppend(nu)
#         else:
#             return (nu*deco(nu-1))
#             d.apppend(nu)
#
#     return inner
# print(d)
#
# @deco
# def ans():
#     return 4
#
# print(ans())
#
def f1(func):
    print(func)
    print("f1")
    return func
@f1
def f2():
    print("f2")
print(f2())
