d1 = {1:'a' , 2:'b', 3:'c' , 4:'e' }
d2 = {3:'c' , 4:'e'}
x={'x': 60, 'y': 50, 'a': 10, 'b': 23}
y = {'x': 60, 'y': 50, 'a': 10, 'b': 23 , 1:'a' , 2:'b', 3:'c' , 4:'e'}

print((zip(d1.values(),d2.values())))

# print(d1.items())  # list of tuples ( [()] )
# print(d1.keys())   # list            ( [] )
# print(d1.values()) # list            ( [] )

# print(sorted(d1,key=lambda x:x==1))  #error key accept function

# print(max(x))   # max print maximum of all even alphabates
# print(min(y)) #cant support between int and str


# print(list(i for i in d1 if i%2==0))



# l=[{'x': 20, 'y': 50, 'a': 10, 'b': 23}
#     ,{'o': 20, 'g': 90, 'f': 10, 'e': 23},{'k': 80, 'h': 60}]

# (map(dict(x),d1))
