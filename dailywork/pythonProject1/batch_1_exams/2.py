l = ['Hyy','my','Name','123','is12','dhruv','Add']
e = []
for i in l:
    if i.isalpha() and i[0].isupper():
        if i[0] not in ['a','e','i','o','u','A','E','I','O','U']:
            e.append(i)
print(e)