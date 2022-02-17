def arg(*i):
    if len(i)==2:
        print("this is" ,i[0],"this is",i[1] )
    else:
        print('error')
arg('aa','bb')
arg('bb')

a = {1:'a',2:'b',3:{4:'c'},5:'d'}
arg(*a.items())  # if we want to pass list/tuple/dict than * must be there

print(*a.items()) #it gives tuples of dict items

a1 = {'a':1,'b':2,'c':3,'d':4}
def kwar(**k):
    for x,y in k.items():
        print(x,y)

kwar(**a1)

