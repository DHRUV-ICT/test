li = ['sfs','aa','adfsgf']

def function(list):

    e = []
    for x in range(len(list)):
        e.append(len(list[x]))
        if len(list[x]) == max(e):

            print(list[x])
    print(e)



function(li)
