i =  input()

a = i.replace(' ','')
s=''
l=[]
for x in a:
    s += x
    print(s)
    if s.count('(') == s.count(')'):
        l.append(s)
        s = ''
print(l)








s = "( ()) ((()()())) (()) ()"
s = s.replace(' ','')
de = ''
li = []
for x in s:
    # print(x,end=' ')
    de += x
    if de.count('(')== de.count(')'):
        li.append(de)
        de =''

print(li)





