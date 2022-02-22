# from datetime import datetime as dt
# import datetime as dt
# date = (dt.datetime.now())
# print(date.microsecond)
# t_date = dt.datetime(2022,8,4)
#
# diff = t_date - date
# print(type(diff))
#
# print(dt.timedelta())

# l = list(range(200,1000))
# print(str(l[0])[0])
# l = [131,13,22,44,55]
# x = map(str,l)
# print(list(x))
# a = ','.join(l)
# # print(a)
#
#
# m = { 'pm': {'robert':{'mark':8,'samuel':8, 'paul':8, 'tom':8 },
#             'anne':{'chris':5, 'pratt':5, 'emma':5, 'will':5, 'smith':5}} ,
#
#       'tl':{'mark':{'leo':1, 'alex':1},
#             'samuel':8 ,
#             'paul':{'fergal':4.5},
#             'tom':{'jerry':1.5 , 'james':1.6},
#             'will': {'edge': 3, 'rayan': 3.5},
#             'smith': {'walker': 2.7, 'diana': 2.7}},
#
#       'sd': {'leo': 1, 'alex': 1, 'fergal': 4.5, 'jerry': 1.5, 'james': 1.6, 'jennifer': 3.5, 'scott': 3.8,
#              'sophie': 3.8, 'edge': 3, 'rayan': 3.5, 'walker': 2.7, 'diana': 2.7}
#       }
#             'chris':{'james':{'jennifer':3.5 , 'scott':3.8, 'sophie':3.8}},
#             'pratt':5 ,
#             'emma':5,
#
#
#
#
# def funvtion(dict):
#     for x in m['pm']:
#          if 'smith' in (m['pm'][x]):
#              del m['pm'][x]['smith']
#
#     if 'smith' in m['tl']:
#         del m['tl']['smith']
#
#     print(m['tl'])
#     print(m['pm'])

# import random
#
# print(random.sample(range(0,10),5))
# n = input()
# for i in range(0,n);
#     print(' '(n-1))

# a = ?t(type)

# #print(~10) # it gives seconf compliment
# c =122.555
# # print(c.conjugate())  it means c bar  ex. conjugate of A+B is A-B
#
#
# re = 100
# im = 25
# #print(complex(re, im))
# # print(divmod(re,im))
#
# print(abs(-12.5)
# #l=1.1+2.2
# #print(abs(l))

# l = [12,24,35,70,88,120,155]
# q = [0,4,5]
# print(list(l[x] for x in range(len(l)) if x not in q))



# s = 'hello how are you'
# pritn(s[0]

# l = [1,2,3,4,5,6,7,8,9]
# print(list(x for x in l if x%2!= 0 ))

# l = [12,24,35,24,88,120,155,88,120,155]
# a = []
# for x in l:
#     if l.count(x)>=1 and x not in a:
#         a.append(x)
# print(sorted(a))

# l1 = [1,3 ]
#
# s1 = ['i','you']
# s2 = ['love','play']
# print(list(map(lambda x,y:(x+y), s1,s2)))
# for x in s1:
#     for y in s2:
#         print(x+y,end=' ')

f = 8

# def fact(d):
#     if d<=1:
#         return 1
#     else:
#         return(d*fact(d-1))
    # if d-1 != 0:
    #     fact(d-1)
        # for x in range(d):
        #     print(d*(d-x))
# def decor1(func):
#     def inner():
#         x = func()
#         return x * x
#
#     return inner
#
# def decor(func):
#     def inner():
#         x = func()
#         return 2 * x
#
#     return inner
#
# def decor2(func):
#     def inner():
#         x = func()
#         return x + 5
#
#     return inner
#
# @decor2
# @decor1
# @decor
# def num():
#     return 10
#
#
# print(num())

# class A():
#    def method(self):
#        print ("I am from class A")

# class B(A):
#    def method(self):
#        print("I am from B")
#        super().method()
#
# class C(A):
#    def method(self):
#        print ("I am from class C")
#
# class D(B,C):
#    def method(self):
#        print ("I am from class D")
#        super().method()
#



# def fub(x=0,y=24,z=44):
#   return 1,3,5
#
#
# a,b,c = fub(x=23,z=[],y={})
# print(a,b,c)
# print(type(b))




# d = D()
#
# d.method()

# def fun(x,y)

# l = list(range('a','z',2))
#
# dict = {'a': 1, 'b': 2}
#
# # will create a new dictionary
# new_dict = {**dict,**{'c': 3}}
#
# print(dict)
# print(new_dict)

# tu = {1,2,2,3,4,'a','b'}

# tu.add('c')
# tu.add(6)
# tu.remove('c')
# print(tu)
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


print(factorial(8))

