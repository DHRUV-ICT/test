l = [[1, 3, 2, 32, 19], [19, 2, 48, 19], [], [9, 35, 4], [3, 19],19]
a = l[-1]
# r = []
# f = []
# print(l.index(19))

# for x in range(len(l)):
#     if (a in l[x]) or (a == l[x]):
#         print(x)
#         print(l[x].index(a))
#         #r.append(x)
#         #f.append(l[x].index(a))
#     else:
#         continue

#print(list(enumerate(l)))
for i,row in enumerate(l[0:-1]):

     for j,n in enumerate(row):
         #print(n)
         if a == n:
             print([i,j])