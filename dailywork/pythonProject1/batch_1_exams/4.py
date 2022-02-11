m = { 'pm': {'robert':{'mark':8,'samuel':8, 'paul':8, 'tom':8 },
            'anne':{'chris':5, 'pratt':5, 'emma':5, 'will':5, 'smith':5}} ,

      'tl':{'mark':{'leo':1, 'alex':1},
            'samuel':8 ,
            'paul':{'fergal':4.5},
            'tom':{'jerry':1.5 , 'james':1.6},

            'chris':{'james':{'jennifer':3.5 , 'scott':3.8, 'sophie':3.8}},
            'pratt':5 ,
            'emma':5,
            'will':{'edge':3 , 'rayan':3.5},
            'smith':{'walker':2.7, 'diana':2.7}},

      'sd': {'leo':1, 'alex':1, 'fergal':4.5, 'jerry':1.5, 'james':1.6, 'jennifer':3.5, 'scott':3.8,
             'sophie':3.8, 'edge':3, 'rayan':3.5, 'walker':2.7, 'diana':2.7 }
    }
# #1
# x = input()
# print(m['pm'][x].keys())

# #2
# def function(d):
#     for x in (m['pm']):
#         for y in m['pm'][x]:
#              if (m['pm'][x][y]) >= 4:
#                  print(y)
#
#     for x in (m['sd']):
#          if (m['sd'][x]) >= 4:
#              print(x)
#
# function(m)

#3
# def function(d):
#     for x in (m['pm']):
#         for y in m['pm'][x]:
#              if (m['pm'][x][y]) >= 3.5 and (m['pm'][x][y]) <= 4.5:
#                  (m['pm'][x][y]) = 4.6
#                  print(y)
#
#     for x in (m['sd']):
#          if (m['sd'][x]) >= 3.5 and (m['sd'][x]) <= 4.5:
#              (m['sd'][x]) = 4.6
#              print(x)
#
# function(m)


#4
# for x in m['tl']:
#     if (m['tl'][x]) in [0,1,2,3,4,5,6,7,8,9]:
#         print(x,m['tl'][x])
#     else:
#         print(x,'N/A')

#4 right way
# for x in m['pm']:
#     print(m['pm'][x])

#5
# def function(dict):
#     for x in m['pm']:
#          if 'smith' in (m['pm'][x]):
#              del m['pm'][x]['smith']
#
#     if 'smith' in m['tl']:
#         del m['tl']['smith']
#
#     print(m['tl'])
#     print(m['pm'])

# print(m['tl']['smith'])
# m['sd']['rayan'] = m['tl']['smith']
# print(m['sd']['rayan'])

#6
# def function(dict):
#     a = []
#     for x in m['pm']:
#         for y in m['pm'][x]:
#             if m['pm'][x][y] < 2 and  m['pm'][x] not in a:
#                 a.append(m['pm'][x])
#
#     for z in m['sd']:
#         if (m['sd'][z] < 2) and (m['sd'] not in a):
#             a.append(z)
#             a.append(m['sd'][z])
#
#     print(a)

# function(m)

# #7
# def function(dict):
#
#     if 'edge' in m['tl'].keys():
#         print('yes')
#     else:
#         print('no')
#         m['tl']['edge'] = 3
#         print(m['tl'])
#
# function(m)