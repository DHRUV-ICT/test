s = [ 'ca',('cat', 'car', 'fear', 'center')]

for x in range(len(s[1])):
    if s[1][x][:2] == s[0]:
        print(s[1][x])

#print(s[1][0][1])

se = set()

for i in range(len(s[1])):
    if s[0] in  s[1][i]:
        se.add(s[1][i])

print(se)