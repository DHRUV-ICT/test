s = input()

# a = s.split(',')
# print(a)

a = []
for y in range(len(s)):
    if ',' in (s):
        a.append(s.split(','))

    elif ' ' in  (s):
         a.append(s.split(' '))
    else:
        if (y%2) != 0:
            print((s),end=' ')
print(a)

    # elif (' ' not in s[i]) and (',' not in s[i]):
    #     a = (s[i%2 == 0])
    #     if i%2 != 0 :
    #         continue

        # b.append(s[i%2!=0])

st = "hyy i am dhruv"
print(st[0])

b=[]
if ',' in (s):
    b.append(s.split(','))

elif ' ' in  (s):
    b.append(s.split(' '))
# else:
#     if (y%2) != 0:
#
#         print((s),end=' ')
print(b)