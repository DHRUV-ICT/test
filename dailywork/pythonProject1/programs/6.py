l = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160]


count = 0
for i in range(len(l)-1):
    if ((l[i+1]-l[i]) == 10):
        count += 1

print(count)
print(len(l))
if count >= len(l)-1:
    print("yes")