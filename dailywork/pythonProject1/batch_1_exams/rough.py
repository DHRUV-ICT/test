nested_lst2 = [{"camera":2, "phone":1}, {"car":1, "van":0}]

# print([*nested_lst2[0]])
di = {"camera":2, "phone":1,"car":1, "van":0}

print(*di.items())

nested_lst3 = [{"camera":{"color": "black", "res": 16}, "phone":1},
               {"car":{"amount": 1, "year": 2017, "color": "red"}, "van":0}]

print(nested_lst3[1]["car"]["color"])


nested_lst4 = {"items":{"camera":{"color": "black", "res": 16}, "phone":1},
               "assets": {"car":{"amount": 1, "year": 2017, "color": "red"},
                          "van":0}}

print(nested_lst4["assets"])

lst = ['a','b','A','B']

print(min(lst))
print(sorted(lst))


di = {'a':1,'b':21,'c':43,'d':424,'e':23,'f':634,'g':4214,'h':10}

print(sorted(di.items(),key=lambda x:(x[1])))