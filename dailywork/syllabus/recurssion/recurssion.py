
count = 0
def fun(x):
    count = 12
    # count += 10
    # while 0 < count <= 100:
    #     print(count)
    #     fun()
    # while count > 100:
    #     pass





    def inner():
        print("faskfgvasgf")
        nonlocal count
        count += 10
        while 0 < count <= 100:
            print(count)
            inner()
        while count > 100:
            break
    return inner

@fun
def exe():
     return 5

# print(fun(2))
exe()