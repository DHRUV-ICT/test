s= input("Enter string:")

def f1(fun):
    def inner():
        print("f2")
        s = str(fun())  # here f2 execute
        print("f1")
        if s.isnumeric():
            print('it is a num')
        else:
            print("no one")
    return inner

@f1
def f2():
    if s.islower():
        print(s)
    elif s.isupper():
        print('it is upper')
    else:
        return s

f2()


# greet(shout)   this is also method to decorate functions
# greet(whisper)




# def f1(fun):
#     def inner():
#         print('before')
#         fun()      #  here f2 run very important
#         print('after')
#         print("f1")
#     return inner
#
# def f2():
#     print('f2')