s = input()

# a = s.split(',')
# print(a)
b =  []
a = []
for y in range(len(s)):
    if ',' in (s[y]):
        a.append(s.split(','))

    elif ' ' in  (s[y]):
         a.append(s.split(' '))
    else:
        if (y%2) != 0:
            print((s[y]),end=' ')

print(a)
    # elif (' ' not in s[i]) and (',' not in s[i]):
    #     a = (s[i%2 == 0])
    #     if i%2 != 0 :
    #         continue

        # b.append(s[i%2!=0])

