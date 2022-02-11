l = [1000,2015,2014,111,1,0,13212,12,3015,]
a = []
#print(list(l))
b = map(str,l)

for i in l:
    if len(str(i)) == 4:
        if i%3 == 0 or i%7 == 0:
            if int((str(i)[0]))%2 != 0 and int((str(i)[-1]))%2 == 0 :
                a.append(i)

print(a)