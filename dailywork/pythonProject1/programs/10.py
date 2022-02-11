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