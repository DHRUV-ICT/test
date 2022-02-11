import random
total_number = int(input())
l = []
for x in range(total_number):
    r = random.randint(0,total_number)
    l.append(r)
print(l[0::2])

# random.sample(range(),numbers we want)


