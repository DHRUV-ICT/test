l = [1,1,1,1,1,1]


if len(l) == sum(l):
    print('yooo')
else:
    print('noppp')


for i in range(len(l)):
    if sum(l[:i+1]) == i:
        print(i)
        print("yes")
    else:
        print(i)
        print("no")


def test(nums):
    an = all([sum(nums[:i]) == i for i in range(len(nums))])
    if an == True:
        print("yes")

test(l)