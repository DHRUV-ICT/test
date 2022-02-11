l = [1,2,5,4,9,7,634,6]

# for x in l:
#     if (x+1 - x) >0 :
#         print('increasing')
#     elif (x - x+1) < 0:
#         print('decresing')
#     #else :
#         print('afbhzasyvfgskjdis')

def function(list):
    a = []
    count = 0
    for x in range(len(list)-1):
        if (((list[x + 1] - list[x]) > 0)):
            #print('increasing')
            count += 1
            a.append('increasing')
        elif (((list[x+1] - list[x]) < 0)):
            a.append('decreasing')
            #print('decreasing')
            count = 0
        elif ((list[x+1] - list[x]) ==  0) :
            a.append('afbhzasyvfgskjdis')


    if a.count('increasing') == len(list)-1:
        print('increasing')
    elif a.count('decreasing') == len(list)-1:
        print('decresing')
    else:
        print('non monotoonic')

function(l)