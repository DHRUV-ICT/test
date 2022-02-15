

#def func(x=4,y):  #we cant give second argument as a default but first can
# def func(x,y=4):
#     return x,y
# a,b = func()
# print(a,b)



# def str(a,b):
#     print(  f' 1 is  {a} , 2 is {b} ,3 is ')
#str(a=1,b)  #if want to add argument by name then all parameters has to give by name
# str('b','a')

# def fun(m=[]):
#     print(m)
# fun([1,2,3,4,5,6,7,8]) # if we pass list in function then we must be give list otherwise it change that value


# def fun():
#     pass  # it gives none type
#     return 1,2,3,4
# print(type(fun()))  # it gives class tuple

#Positional arguments
#must agree in order and number with the parameters declared in the function definition.
#funcname(1,2,3)

#Keyword arguments
#must agree with declared parameters in number, but they may be specified in arbitrary order.
#functoinname(a=1,b=2,c=3)

#Default parameters
#allow some arguments to be omitted when the function is called.
#functionname(give any one argument)

def rec(d):
    if d != 0:
        rec(d-1)
        print(d,end=' ')


rec(12)