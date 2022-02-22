l = [0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]

a= []
# for i in range(len(l)-1):
#     if l[i]<l[i+1]:
#         a.append(l[i])
#         a.append(l[i+1])
#     else:
#         a.append(l[i])
#

def fun(i):
    i = min(l)
    a.append(i)
    for x in l:
        if x>i :
            a.append(x)
            i = x
        elif x==i:
            pass
        else:
            a.append(i)

fun(1)
print(a)

#[0, 0, 3, 8, 8, 9, 9, 14, 14, 14, 14, 14, 14, 17, 41, 41, 41, 41, 41, 41]


def test(nums):
    return [max(nums[:i]) for i in range(len(nums)-1)]

print(test(l))
