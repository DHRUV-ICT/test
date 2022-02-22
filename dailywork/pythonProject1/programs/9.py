l = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1]
s = set(l)
print(s)

# for i in range(len(l)-1):
    # if i != i+1 and len(s)==4:
        # print("yes")

def fun():
    return all(l[i+1]!=l[i] for i in range(len(l)-1)) and len(set(l))==4

print(fun())