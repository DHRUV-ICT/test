l = [100,(0,12,14,12,145,12,1256,11,12458,111)]
a = l[0]
for x in range(len(l[1])):
    if l[1][x] < a:
        print(x)

print(list(enumerate(l[1])))

