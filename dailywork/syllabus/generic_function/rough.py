# # a = {'a':1,'b':2,'c':3,'d':4}
# # a1 = {1:'a',2:'b',3:{4:'c'},5:'d'}
# a1 = [{'a':1,'b':2,'e':6},{'c':3,'d':4},{1:'a',2:'b'}]
# #
# #
# f = list(map(lambda x:x,a1))
# # print(dict(f))
# #
# # for i in a1:
# #     print(i)
# #
# # print(*a1)
#
# l=[{'x': 20, 'y': 50, 'a': 10, 'b': 23},
#    {'o': 20, 'g': 90, 'f': 10, 'e': 23},
#    {'k': 80, 'h': 60}]
#
# def re_tu(di1,di):
#     di = dict(di1.items())
#     return di
# di={}
# print(*l)
# s=[]
# for i in range(len(l)):
#     s.append([*l[i].items()])
# print(s)
#
# def fun(li,tu,di):
#     tu = tuple(li)
#     di = dict(tu)
#     return di
#
#
# fun()
#
#
# # print(set(map(lambda x:x.items(),*l)))
# # print(ld)
# # print(re_tu(ld,di))


a = [1,2,3]
b = {
	1: [4,5,6],
	2: [7,8],
	3: [9, 10],
	4: [11, 12, 13],
	9: [14, 15],
	10: [16],
	13: [19, 20],
	19: [21]
}
map
li = []
# i == 1,2,3
# j == values
# k == keys
# def ans():
for i in a:
    li.append(i)
    li.append(b[i])


    for j in b[i]:

        # def j1(j):
        if j in b.keys():
            li.append(b[j])
        else:
            pass
            # j1(j+1)
        # return j1

print(li)
        # def j1(j):
        #     for j in b[i]:
        #     # print(j)
        #         for k in b.keys():
        #             if j==k:
        #                 li.append(k)
        #                 li.append(b[k])
        #             else:
        #                 j1(j+


# print(ans())
# def num():
#     return 5


# print(num())

# @ans(a,b)
# def main(a,b):
#     return 4
#
# main(a,b)


        # if j in b.keys():
        #     print(j.valus())
        # print(b[i])


# #def f3(list):   			#                                    a = [1,2,3]
# 	for i in list:
# 		if i in b.keys():
# 			l1.append(i)
# 			for j in b[i]:
# 				l1.append(j)
# 				if j in b.keys():
# 					l1.append(b[j])
# 					for z in b[j]:
# 						if z in b.keys():
# 							l1.append(b[z])