i = "The dance, held in the school gym, ended at midnight."


# print(i.split())

coma = i.count(',')
spaces = i.count(' ')
coma_list = list(','*coma)
spaces_list = list(' '*spaces)

separtors_list = (coma_list +  spaces_list)

i = i.replace(',','')
# print(i)
word_list = (i.split())

print(word_list ,',', separtors_list)