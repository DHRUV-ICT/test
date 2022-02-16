l = [1,12,4,141,51,14,"dadaa",'ada',"DADADS"]
l1 =[]
def fun(x):
    if type(x) == str:
        l1.append(x)
    else:
        pass
    return l1

print(list(filter(fun,l)))


print(list(filter(lambda x:x == x.upper(),l1)))

