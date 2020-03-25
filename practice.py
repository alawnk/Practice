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

# flo1 = 'number: %f' %99.12567
# flo2 = 'number: %.2f' %99.12567
# #打印百分比
# flo3 = 'number: %.2f%%'%99.12567
# print (flo1,flo2,flo3)

# temp1 = 'i am %(name)s, i am %(sex)s,%(age)d'%{'age':30,'sex':'male','name':'alawn'}
# print(temp)

# temp2 = 'i am {},age{},sex{}'.format('alawn',18,'male')
# temp3 = 'i am {0},age{1},sex{2}'.format('alawn',18,'male')
# temp4 = 'i am {2},age{0},sex{1}'.format('alawn',18,'male')
# print(temp1)
# print(temp2)
# print(temp3)
#
# 非字典效果==字典效果
# temp5 = 'i am {name},age {age},sex {sex}'.format(name='alawn',age=18,sex='male')
# temp6 = 'i am {name},age {age},sex {sex}'.format(**{'name':'alawn','age':18,'sex':'male'})
# print(temp1)
# print(temp2)
#
# temp7 = 'i am {:s},age {:d},sex {:f}'.format('alawn',30,13.333)
# temp8 = 'i am {:s},age {:d}'.format(*['alawn',18])
# temp9 = 'i am {name:s},age {age:d}'.format(name='alawn',age= 30)
# temp10 = 'i am {name:s},age {age:d}'.format(**{'name':'alawn','age': 30})
# temp11 = 'numbers:{:b},{:o},{:d},{:x},{:X},{:%}'.format(15,15,15,15,15,15.786,2)
# temp12 = 'numbers:{0:b},{0:o},{0:d},{0:x},{0:%}'.format(15)
# temp13 = 'numbers:{num:b},{num:o},{num:d},{num:x},{num:%}'.format(num=15)
#
# print(temp1)
# print(temp2)
# print(temp3)
# print(temp4)
# print(temp5)
# print(temp6)
# print(temp7)

# temp1 = 'i am %(name)s, i am %(sex)s,%(age)d'%{'age':30,'sex':'male','name':'alawn'}
# temp2 = 'i am {},age{},sex{}'.format('alawn',18,'male')
# temp3 = 'i am {0},age{1},sex{2}'.format('alawn',18,'male')
# temp4 = 'i am {2},age{0},sex{1}'.format('alawn',18,'male')
# temp5 = 'i am {name},age {age},sex {sex}'.format(name='alawn',age=18,sex='male')
# temp6 = 'i am {name},age {age},sex {sex}'.format(**{'name':'alawn','age':18,'sex':'male'})
# temp7 = 'i am {:s},age {:d},sex {:f}'.format('alawn',30,13.333)
# temp8 = 'i am {:s},age {:d}'.format(*['alawn',18])
# temp9 = 'i am {name:s},age {age:d}'.format(name='alawn',age= 30)
# temp10 = 'i am {name:s},age {age:d}'.format(**{'name':'alawn','age': 30})
# temp11 = 'numbers:{:b},{:o},{:d},{:x},{:X},{:%}'.format(15,15,15,15,15,15.786,2)
# temp12 = 'numbers:{0:b},{0:o},{0:d},{0:x},{0:%}'.format(15)
# temp13 = 'numbers:{num:b},{num:o},{num:d},{num:x},{num:%}'.format(num=15)

# temp6 = 'i am {name},age {age},sex {sex}'.format(**{'name':'alawn','age':18,'sex':'male'})
# dic = {'name':'alawn','age':18,'sex':'male'}
# temp7 = 'i am {name},age {age},sex {sex}'.format(**dic)
# print(temp6)
# print(temp7)

# def test(x):
#     y = 2*x+1
#     return y
# print(test)
# a = test(3)
# print(a)
#
# def test():
#     x = 3
#     y= 2*x+1
#     return y
# a= test()
# print(a)

# while True:
#     if CPU利用率>90%:
#         #发送告警邮件
#         连接邮箱服务器
#         发送邮件
#         关闭连接
#
#     if 磁盘空间>90%:
#         #发送告警邮件
#         连接邮箱服务器
#         发送邮件
#         关闭连接
#
#     if 内存占用>90%:
#         #发送告警邮件
#         连接邮箱服务器
#         发送邮件
#         关闭连接
#
# 可转换为以下方式：
#
# def 发送邮件(内容):
#     # 发送告警邮件
#     连接邮箱服务器
#     发送邮件
#     关闭连接
#
# while True:
#     if CPU利用率>90%:
#         发送邮件('CPU告警')
#     if 磁盘空间>90%:
#         发送邮件('磁盘告警')
#     if 内存占用>90%:
#         发送邮件('内存告警')


# def test1():
#     msg = 'hello world!'
#     print(msg)
#
# def test2():
#     msg = 'hello world!!'
#     print(msg)
#     return msg
#
# def test3():
#     msg = 'hello world!!!'
#     print(msg)
#     return 1,'a',True,None,[1,2,3],{'name':'alawn'},(1,'a',True)
#
# t1 = test1()
# t2 = test2()
# t3 = test3()
# print(t1)
# print(t2)
# print(t3)

# def test(x,y,z):
#     print(x,y,z)
# test(1,2,z=3)

# def test(x,**kwargs):
#     print(x)
#     print(kwargs)
# # test(1,2,3,4,5,[1,2,3],'a',{1:'2'})
# test(1,y=2)

#
# def test(x,*arge,**kwargs):
#     print(x)
#     print(arge)
#     print(kwargs)
# test(1,2,3,4,5,'a',[1,2,['x']],name1 = 'alawn',name2 = 'quiana')

 