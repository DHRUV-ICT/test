a = [1,2,3]
b = {
	1: [4,5,6],
	2: [7,8],
	3: [9, 10],
	4: [11, 12, 13],
	9: [14, 15],
	10: [16],
	13: [19, 20],
	19: [21]}
l = []
# def f1(d):
# 	for i in a:
# 		if i in b.keys():
# 			l.append(i)
# 			l.append(b[i])
#
# 		for j in b[i]:
# 			print(j)
# 			def f2():
# 				print("f2")
# 				if j in b.keys():
# 					l.append(b[j])
# 				f2(d+1)
# 			# return f2
#
# 	print(l)
#
# @f1
# def num():
# 	return 4
l1 = []
def f3(f):   			#                                    a = [1,2,3]
	for i in a:
		if i in b.keys():
			l1.append(i)
			for j in b[i]:
				if j in b[i]:
					l1.append(j)
			f3(b[i])
		# l1.append(b[i])
		# f3(b[i])
	print(l1)

@f3
def num():
	return 3
