ti = int(input())


l=[]
sum = 0
minus = 0
for x in range(ti+1):
    t = input()
    a = int(input())
    l.append(t)
    l.append(a)

for y in range(len(l)):
    if l[y] == 'd':
        sum += l[y+1]
    elif l[y] == 'w':
        minus += l[y+1]
        sum == sum-l[y+1]


print(sum-minus)
print(l)


