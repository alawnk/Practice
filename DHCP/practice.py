# name = '  alawn  '
# eg1 = name.strip()
# print(eg1)
# eg2 = eg1.startswith('al')
# eg3 = eg1.endswith('n')
# print(eg2,eg3)
# eg4 = eg1.replace('l','q')
# print(eg4)
# eg5 = eg1.split('l')
# print(eg5)
# for i in range (len(eg1)):
#     print(eg1[1],eg1[0:3],eg1[3:5])#如何去最后两个
#     break
# for i in range (len(eg1)):
#     if eg1[i] == 'w':
#         print(i)
#     else:
#         continue
#
#
# while True:
#     count = 1
#     while count < 6:
#         print('COUNT:',count)
#         def check_code():
#             import random
#             checkcode = ''
#             for i in range (10):
#                 current  = random.randrange(0,10)
#                 if current != i:
#                     temp = chr(random.randint(65,90))
#                 else:
#                     temp = random.randint(0,9)
#                 checkcode += str(temp)
#             return checkcode
#         code = check_code()
#         print('Verification_code:',code)
#         Verification_code = input('Please input Verification_code:')
#         if Verification_code != code:
#             print("Sorry, you're not a legal user!")
#         else:
#             print('Welcome to login,have a nice day!')
#             break
#         count += 1
#     break

# List = [1,2,3,4,5,6,'alawn','quiana',[1,2,3,'qweqwe']]
# #print(List,type(List),List[1],type(List[1]),List[1:5],type(List[1:5]))
# List[1] = 789
# print(List)
# #删除元素
# del List[1]
# print(List)

# list = [1,2,3,4]
# list.append(5)
# print(list)


# info = {
#     'k1':18,
#     'k2':True,
#     'k3':[
#         11,
#         [],
#         (),
#         22,
#         33,
#         {
#             'kk1':'vv1',
#             'kk2':'vv2',
#             'kk3':(11,22),
#         }
#     ],
#     'k4':(11,22,33,44,)
# }
# # print(info['k3'][5]['kk3'][0])
# # del (info['k3'][5]['kk1'])
#
# for k in info.keys():
#     print(k)
#
# for v in info.values():
#     print(v)
#
# for k,v in info.items():
#     print(k,v)
# v1 = dic.get('k1')
# v2 = dic.get('k4')
# v3 = dic.get('k4','no k4')
# v4 = dic.pop('k1')
# v5 = dic.pop('k4','no k4')
# v6 = dic.popitem()
# print(v1)
# print(v2)
# print(v3)
# print(dic)
# print(v4)
# print(v5)
# print(v6)
# dic = {'k1':'v1','k2':'v2','k3':'v3'}
# # v1 = dic.update({'k1':'123'})
# # v2 = dic.update({'k4':'v4'})
# dic.update(k1=123,k4='v4')
# print(dic)
#
#
# P_S = {1,2,3,4}
# L_S = {1,2,3,5}
# P_S.update(L_S)
# print(P_S)

flo = 'number: %f' %99.12567
flo2 = 'number: %.2f' %99.12567
print (flo,flo2)





