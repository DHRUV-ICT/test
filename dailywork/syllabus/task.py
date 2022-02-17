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
def f3(l):
	c = 0
	for i in l:
		if i in b.keys():
			l1.append(i)
			l1.append(b[i])
			c += 1
			if c < len(l):
				if b[i][c] in b.keys():
					l1.append(b[c])
			else:
				break
	# for j in a:
	# 	f3(j)


	print(l1)
f3(a)