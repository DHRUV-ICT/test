l1 = [1,2,3]
l2 = [4,5,2]
l3 = [6]
d1 = {1:'a' , 2:'b' }
d2 = {3:'c' , 4:'e'}

# print(list(zip(l1,l2,l3)))

for x in zip(l1,l2,l3):
    print(x)

for i in zip(d1,d2.values()):   # in dictionary keys are zipped
    print(i)



