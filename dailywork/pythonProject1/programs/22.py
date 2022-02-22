s = 'PytHon ExerciSEs   '

l = []
for x in range(len(s)):
    if s[x].isupper():
      l.append(ord(s[x]))

print(l)
print(sum(l))



print(list(map(lambda x:x , s)))

