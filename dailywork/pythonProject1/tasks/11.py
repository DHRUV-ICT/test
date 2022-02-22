import random
total_number = 5
l = []
for x in range(total_number):
    r = random.randint(0,total_number)
    l.append(r)
print(l[0::])

print(random.sample(range(10),5))
print(random.randint(0,4))


