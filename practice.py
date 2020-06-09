# # name = '  alawn  '
# # eg1 = name.strip()
# # print(eg1)
# # eg2 = eg1.startswith('al')
# # eg3 = eg1.endswith('n')
# # print(eg2,eg3)
# # eg4 = eg1.replace('l','q')
# # print(eg4)
# # eg5 = eg1.split('l')
# # print(eg5)
# # for i in range (len(eg1)):
# #     print(eg1[1],eg1[0:3],eg1[3:5])#如何去最后两个
# #     break
# # for i in range (len(eg1)):
# #     if eg1[i] == 'w':
# #         print(i)
# #     else:
# #         continue
# #
# # while True:
# #     count = 1
# #     while count < 6:
# #         print('COUNT:',count)
# #         def check_code():
# #             import random
# #             checkcode = ''
# #             for i in range (10):
# #                 current  = random.randrange(0,10)
# #                 if current != i:
# #                     temp = chr(random.randint(65,90))
# #                 else:
# #                     temp = random.randint(0,9)
# #                 checkcode += str(temp)
# #             return checkcode
# #         code = check_code()
# #         print('Verification_code:',code)
# #         Verification_code = input('Please input Verification_code:')
# #         if Verification_code != code:
# #             print("Sorry, you're not a legal user!")
# #         else:
# #             print('Welcome to login,have a nice day!')
# #             break
# #         count += 1
# #     break
#
# # List = [1,2,3,4,5,6,'alawn','quiana',[1,2,3,'qweqwe']]
# # #print(List,type(List),List[1],type(List[1]),List[1:5],type(List[1:5]))
# # List[1] = 789
# # print(List)
# # #删除元素
# # del List[1]
# # print(List)
#
# # list = [1,2,3,4]
# # list.append(5)
# # print(list)
#
#
# # info = {
# #     'k1':18,
# #     'k2':True,
# #     'k3':[
# #         11,
# #         [],
# #         (),
# #         22,
# #         33,
# #         {
# #             'kk1':'vv1',
# #             'kk2':'vv2',
# #             'kk3':(11,22),
# #         }
# #     ],
# #     'k4':(11,22,33,44,)
# # }
# # # print(info['k3'][5]['kk3'][0])
# # # del (info['k3'][5]['kk1'])
# #
# # for k in info.keys():
# #     print(k)
# #
# # for v in info.values():
# #     print(v)
# #
# # for k,v in info.items():
# #     print(k,v)
# # dic = {'k1':'v1','k2':'v2','k3':'v3'}
# # v1 = dic.get('k1')
# # v2 = dic.get('k4')
# # v3 = dic.get('k4','no k4')
# # v4 = dic.pop('k1')
# # v5 = dic.pop('k4','no k4')
# # v6 = dic.popitem()
# # print(v1)
# # print(v2)
# # print(v3)
# # print(dic)
# # print(v4)
# # print(v5)
# # print(v6)
# # dic = {'k1':'v1','k2':'v2','k3':'v3'}
# # # v1 = dic.update({'k1':'123'})
# # # v2 = dic.update({'k4':'v4'})
# # dic.update(k1=123,k4='v4')
# # print(dic)
# #
# #
# # P_S = {1,2,3,4}
# # L_S = {1,2,3,5}
# # P_S.update(L_S)
# # print(P_S)
#
# # flo1 = 'number: %f' %99.12567
# # flo2 = 'number: %.2f' %99.12567
# # #打印百分比
# # flo3 = 'number: %.2f%%'%99.12567
# # print (flo1,flo2,flo3)
#
# # temp1 = 'i am %(name)s, i am %(sex)s,%(age)d'%{'age':30,'sex':'male','name':'alawn'}
# # print(temp)
#
# # temp2 = 'i am {},age{},sex{}'.format('alawn',18,'male')
# # temp3 = 'i am {0},age{1},sex{2}'.format('alawn',18,'male')
# # temp4 = 'i am {2},age{0},sex{1}'.format('alawn',18,'male')
# # print(temp1)
# # print(temp2)
# # print(temp3)
# #
# # 非字典效果==字典效果
# # temp5 = 'i am {name},age {age},sex {sex}'.format(name='alawn',age=18,sex='male')
# # temp6 = 'i am {name},age {age},sex {sex}'.format(**{'name':'alawn','age':18,'sex':'male'})
# # print(temp1)
# # print(temp2)
# #
# # temp7 = 'i am {:s},age {:d},sex {:f}'.format('alawn',30,13.333)
# # temp8 = 'i am {:s},age {:d}'.format(*['alawn',18])
# # temp9 = 'i am {name:s},age {age:d}'.format(name='alawn',age= 30)
# # temp10 = 'i am {name:s},age {age:d}'.format(**{'name':'alawn','age': 30})
# # temp11 = 'numbers:{:b},{:o},{:d},{:x},{:X},{:%}'.format(15,15,15,15,15,15.786,2)
# # temp12 = 'numbers:{0:b},{0:o},{0:d},{0:x},{0:%}'.format(15)
# # temp13 = 'numbers:{num:b},{num:o},{num:d},{num:x},{num:%}'.format(num=15)
# #
# # print(temp1)
# # print(temp2)
# # print(temp3)
# # print(temp4)
# # print(temp5)
# # print(temp6)
# # print(temp7)
#
# # temp1 = 'i am %(name)s, i am %(sex)s,%(age)d'%{'age':30,'sex':'male','name':'alawn'}
# # temp2 = 'i am {},age{},sex{}'.format('alawn',18,'male')
# # temp3 = 'i am {0},age{1},sex{2}'.format('alawn',18,'male')
# # temp4 = 'i am {2},age{0},sex{1}'.format('alawn',18,'male')
# # temp5 = 'i am {name},age {age},sex {sex}'.format(name='alawn',age=18,sex='male')
# # temp6 = 'i am {name},age {age},sex {sex}'.format(**{'name':'alawn','age':18,'sex':'male'})
# # temp7 = 'i am {:s},age {:d},sex {:f}'.format('alawn',30,13.333)
# # temp8 = 'i am {:s},age {:d}'.format(*['alawn',18])
# # temp9 = 'i am {name:s},age {age:d}'.format(name='alawn',age= 30)
# # temp10 = 'i am {name:s},age {age:d}'.format(**{'name':'alawn','age': 30})
# # temp11 = 'numbers:{:b},{:o},{:d},{:x},{:X},{:%}'.format(15,15,15,15,15,15.786,2)
# # temp12 = 'numbers:{0:b},{0:o},{0:d},{0:x},{0:%}'.format(15)
# # temp13 = 'numbers:{num:b},{num:o},{num:d},{num:x},{num:%}'.format(num=15)
#
# # temp6 = 'i am {name},age {age},sex {sex}'.format(**{'name':'alawn','age':18,'sex':'male'})
# # dic = {'name':'alawn','age':18,'sex':'male'}
# # temp7 = 'i am {name},age {age},sex {sex}'.format(**dic)
# # print(temp6)
# # print(temp7)
#
# # def test(x):
# #     y = 2*x+1
# #     return y
# # print(test)
# # a = test(3)
# # print(a)
# #
# # def test():
# #     x = 3
# #     y= 2*x+1
# #     return y
# # a= test()
# # print(a)
#
# # while True:
# #     if CPU利用率>90%:
# #         #发送告警邮件
# #         连接邮箱服务器
# #         发送邮件
# #         关闭连接
# #
# #     if 磁盘空间>90%:
# #         #发送告警邮件
# #         连接邮箱服务器
# #         发送邮件
# #         关闭连接
# #
# #     if 内存占用>90%:
# #         #发送告警邮件
# #         连接邮箱服务器
# #         发送邮件
# #         关闭连接
# #
# # 可转换为以下方式：
# #
# # def 发送邮件(内容):
# #     # 发送告警邮件
# #     连接邮箱服务器
# #     发送邮件
# #     关闭连接
# #
# # while True:
# #     if CPU利用率>90%:
# #         发送邮件('CPU告警')
# #     if 磁盘空间>90%:
# #         发送邮件('磁盘告警')
# #     if 内存占用>90%:
# #         发送邮件('内存告警')
#
#
# # def test1():
# #     msg = 'hello world!'
# #     print(msg)
# #
# # def test2():
# #     msg = 'hello world!!'
# #     print(msg)
# #     return msg
# #
# # def test3():
# #     msg = 'hello world!!!'
# #     print(msg)
# #     return 1,'a',True,None,[1,2,3],{'name':'alawn'},(1,'a',True)
# #
# # t1 = test1()
# # t2 = test2()
# # t3 = test3()
# # print(t1)
# # print(t2)
# # print(t3)
#
# # def test(x,y,z):
# #     print(x,y,z)
# # test(1,2,z=3)
#
# # def test(x,**kwargs):
# #     print(x)
# #     print(kwargs)
# # # test(1,2,3,4,5,[1,2,3],'a',{1:'2'})
# # test(1,y=2)
#
# #
# # def test(x,*arge,**kwargs):
# #     print(x)
# #     print(arge)
# #     print(kwargs)
# # test(1,2,3,4,5,'a',[1,2,['x']],name1 = 'alawn',name2 = 'quiana')
#
# # def aaa():
# #      print('alawn')
# #      bbb()
# # def bbb():
# #      print('quiana')
# # aaa()
# #
# # def calc(n):
# #      print(n)
# #      if int(n/2 == 0):
# #           return n
# #      return calc(int(n/2))
# # calc(10)
# #
# #
# # person_list = ['quiana','kevin','jimmy','alawn']
# # def ask_way(person_list):
# #      print('-'*60)
# #      if len(person_list) == 0:
# #           return 'nobody knows'
# #      person = person_list.pop(0)
# #      if person == 'alawn':
# #           return '%s knows'%(person)
# #      print('HI,%s,can you tell me'%person)
# #      print("%s say:sorry,i don't know,I can help you to ask %s" %(person,person_list))
# #      print('--%s--tell me,%s knows'%(person,person_list))
# #      res = ask_way(person_list)
# #      print('%s say: %s' %(person,res))
# #      return res
# # RES = ask_way(person_list)
# # print(RES)
#
#
# #作用域
# # def test1():
# #     print('in the test1')
# # def test():
# #     print('int the test')
# #     return test1
# # res = test()
# # print(res())
#
# # name = 'alawn'
# # def foo():
# #     name = 'jimmy'
# #     def bar():
# #         name = 'quiana'
# #         def tt():
# #             print(name)
# #         return tt
# #     return bar
# # foo()()()
#
#
# # lambda x:x+1
# # calc = lambda x:x+1
# # print(calc(10))
#
# # name = 'alawn'
# # def change_name(X):
# #     return name + '_king'
# # res = change_name(name)
# # print(res)
#
# # name = 'alawn'
# # change_name = lambda x:x+'_king'
# # print(change_name(name))
#
# # name = ['alawn','quiana','kevin','jimmy']
# # for info in name:
# #     res = lambda x:x+'_king'
# #     print(res(info))
# #     print(info)
#
# # def handel():
# #     print('from handel')
# #     return handel
# # handel()
#
# # def bar(n):
# #     return n
# # def foo(x):
# #     return bar(x)
#
# # def calc(seq):
# #     if len(seq) == 1:
# #         return seq[0]
# #     head,*tail=seq
# #     return head+calc(tail)
# # print(calc(range(100)))
#
#
# # def calc(l):
# #     print(l)
# #     if len(l) == 1:
# #          return l[0]
# #     first,second,*args=l
# #     l[0]=first+second
# #     l.pop(l)
# #     return calc(l)
# #
# # x = calc([i for i in range(10)])
# # print(x)
#
# # num = [1,3,2,4,7,5,8,6]
# # new = []
# # for i in num:
# #     new.append(i**2)
# # print(new)
# # num_list = [1,3,2,4,7,5,8,6]
# # def fuc_addition_one(x):
# #     return x+1
# # def fuc_subtraction_one(x):
# #     return x-1
# # def fuc_square(x):
# #     return x**2
# #
# # def new_list(func,array):
# #     new = []
# #     for i in array:
# #         res = func(i)
# #         new.append(res)
# #     return new
# #
# # print(new_list(fuc_addition_one,num_list))
# # print(new_list(lambda x:x+1,num_list))
# #
# # print(new_list(fuc_subtraction_one,num_list))
# # print(new_list(lambda x:x-1,num_list))
# #
# # print(new_list(fuc_square,num_list))
# # print(new_list(lambda x:x**2,num_list))
# #
# # res = map(lambda x:x+1,num_list)
# # print(list(res))
#
# # from functools import reduce
# # num_list = [1,2,3,4,5,6,7,8]
# # # res = 0
# # # for num in num_list:
# # #     res+=num
# # # print(res)
# # # def addition(fuc,array,init=None):
# # #     if init is None:
# # #         res = array.pop(0)
# # #     else:
# # #         res = init
# # #     for num in array:
# # #         res = fuc(res,num)
# # #     return res
# # # print(addition(lambda x,y:x+y,num_list,100))
# # print(reduce(lambda x,y:x+y,num_list,100))
#
# # name = '你好'
# # print(bytes(name,encoding = 'utf-8').decode('utf-8'))
#
# # dic_str = "{'name':'alawn'}"
# # print(type(dic_str))
# # print(type(eval(dic_str)))
#
# # print(list(zip(('a','b','c'),(1,2,3))))
# # print(list(zip(('a','b','c'),(1,2,3,4))))
# # print(list(zip(('a','b','c','d'),(1,2,3))))
# # print(list(zip(('abcd'),('1,2,3'))))
#
# # age_list = {'2':60,'4':20,'1':100,'3':30}
# # print(max(zip(age_list.values(),age_list.keys())))
# #
# # string = 'abcd1234'
# # s1 = slice(2,6)
# # s2 = slice(2,6,3)
# # print(string[s1])
# # print(string[s2])
#
# # list = ['a','1','asd','4e','=']
# # print(sorted(list))
#
# # price = {
# #     'alawn':30000,
# #     'jimmy':1500,
# #     'keivn':800
# # }
# # key = lambda key:price[key]
# # print (list(key))rr
#
# # src_file = open('practice.txt')
# # data = src_file.readlines()
# # src_file.close()
# # dst_file = open('new_practice.txt','w')
# # dst_file.writelines(data[0])
# # dst_file.close()
#
# # with open('pracrice.txt','r') as src_file,\
# #         open('new_practice.txt','w') as dst_file:
#
#
# # f1 = open('a.txt','r+')
# # f1.write('abab')
# # # f1.seek(3)
# # # f1.write('cdcd')
# # # print(f1.tell())
# # print(f1.truncate(6))
# # f1.close()
# #
# # list = [1,2,3,4,5,6]
# # iter_list = list.__iter__()
# # print(iter_list.__next__())
#
# # name = 'alawn'
# # name = 'KK'
# # # res = 'King' if name == 'alawn' else 'SB'
# # # print(res)
#
#
# # egg_list = []
# # for i in range (1,11):
# #     egg_list.append('鸡蛋%s'%i)
# # print(egg_list)
# #
# # egg_list = ['鸡蛋%s' %i for i in range (1,11)]
# # print(egg_list)
# #
# # egg_list = ['鸡蛋%s' %i for i in range (1,11) if i > 5] #后面不能加else
# # print(egg_list)
# #
# # egg_list1 = ('鸡蛋%s' %i for i in range (1,11)) #生成器表达式，节省内存
# # print(next(egg_list1))
# # print(next(egg_list1))
# # print(next(egg_list1))
# # print(next(egg_list1))
# #
# # def egg_list():
# #     egg_list1 = ('鸡蛋%s' % i for i in range(1, 11))
# #     yield egg_list1.__next__()
# #     yield egg_list1.__next__()
# #     yield egg_list1.__next__()
# #     yield egg_list1.__next__()
# #     yield egg_list1.__next__()
# #     yield egg_list1.__next__()
# # res = egg_list()
# # print(res.__next__())
# # print(res.__next__())
# # print(res.__next__())
# #
# #
# #
# # def shengchanbaozi():
# # 	ret=[]
# # 	for i in range (1,10001):
# # 		ret.append('baozi%s'%i)
# # 	return ret
# #
# # def chibaozi(res):
# # 	for sn,baozi in enumerate(res):
# # 		print('第%s个人吃了%s'%(sn,baozi))
# #
# # chibaozi(shengchanbaozi())
#
#
# def test():
#     print('start:')
#     first = yield
#     print('first one',first)
#     yield 2
#     print('second one')
# t= test()
# res = t.__next__()
# print(res)
# res= t.send(None)
# print(res)
#
#
# def func(start,end):
#     list =[]
#     for i in range (start,end):
#         if i%3 == 0 and i%7 == 0 :
#             list.append(i)
#         else:
#             pass
#     print(len(list))
#     print(sum(list))
# func(1,2000)
#
# def func (*y,**z):
# 	print(y,z)
# func(*[1,2,3,4,5])

# def produce():
#     ret = []
#     for i in range (10000):
#         ret.append('包子%s'%i)
#     return ret
#
# def consumer(res):
#     for index,baozi in enumerate(res):
#         print('第%s个人，吃了%s' %(index,baozi))
#
# res = produce()
# consumer(res)

#yield相当于return ,控制函数的返回值
#send参数可以给yield赋值，并在yield结束的地方继续执行
# def test():
#     print('start:')
#     first = yield 1
#     print('first:',first)
#     second = yield 2
#     print('second:',second)
#     third = yield 3
# t = test()
# res = t.__next__()
# print(res)
# res = t.send('第一次')
# print(res)
# res = t.send('第二次')
# print(res)


# 生产者消费模型(并发执行)

# import time
# def timer(func):
#     def wapper(*args,**kwargs):
#         start_time = time.time()
#         res = func(*args,**kwargs)
#         stop_time = time.time()
#         print('函数运行时间是%s'%(stop_time-start_time))
#         return  res
#     return wapper
#
# @timer
# def cal(l):
#     res = 0
#     for i in l:
#         time.sleep(0.01)
#         res += i
#     print(res)
#     return '函数运行完毕'
# print(cal(range(1000)))

# import time
#
# def foo():
#     time.sleep(3)
#     print(' from foo')
# foo()
#
# def timer(func):
#     start_time = time.time()
#     timer(foo)
#     stop_time = time.time()
#     print('函数运行时间:%s'%(stop_time-start_time))
#     return func


#函数嵌套
# def father(name):
#     print('from father %s'%name)
#     def son():
#         print('from son')
#         def grandson():
#             print('from grandson')
#         grandson()
#     son()
# father('alawn')
#
# #装饰框架
# def timmer(funcv):
#     def wrapper()
#         print(func)
#         func()
#     return wrapper
#
# usr = {'username':None,'login':False}
# def login(func):
#     def wrapper(*args,**kwargs):
#         if usr['username'] and usr['login']:
#             res = func(*args,**kwargs)
#             return res
#         username = input('用户名：').strip()
#         passwd = input('密码：').strip()
#         if username == 'alawn' and passwd == 'xcsdwe':
#             usr['username'] = username
#             usr['login'] = True
#             res = func(*args,**kwargs)
#             return res
#         else:
#             print('sorry')
#     return wrapper
# @login
# def index():
#     print('mall')
# @login
# def home(name):
#     print('%s,home'%name)
# @login
# def shopping_car():
#     print('shopping_car')
# @login
# def order():
#     print('order')
# index()
# home('alawn')
# shopping_car()
# order()


# TAG = True
# while TAG:
#     print('level 1')
#     data = input('level 1=:').strip()
#     if data == 'quit':break
#     if data == 'quit_all':TAG = False
#     while TAG:
#         print('level 2:')
#         data = input('level 2=:').strip()
#         if data =='quit':break
#         if data =='quit_all':TAG = False
#         while TAG:
#             print('level 3:')
#             data = input('level 3=:').strip()
#             if data == 'quit':break
#             if data == 'quit_all':TAG = False

def fetch(data):
    print('正在使用查询功能')
    print('要查询的数据是:',data)
    vlandata = 'interface Vlan%s' %data
    with open('C:/Users/alawn/Desktop/interface_vlan.txt','r') as config_file:
        tag = False
        ret = []
        for line in config_file:
            if line.strip() == vlandata:
                tag = True
                print(vlandata)
                continue
            if tag and line.startswith('interface'):
                break
            if tag:
                print(line.strip('\n'))
                ret.append(line)
        return ret



def add():
    pass

def change():
    print('正在使用修改功能')
    print('请输入需要修改的配置:')

def delete():
    pass

if __name__ == '__main__':
    msg='''
    1.查询
    2.添加
    3.修改
    4.删除
    5.退出
    '''
    msg_dic = {
        '1':fetch,
        '2':add,
        '3':change,
        '4':delete
               }
    while True:
        print(msg)
        choice = input('请输入功能选项:').strip()
        if not choice:continue
        if choice == '5':break

        data = input('请输入要查询的内容:').strip()
        print(msg_dic[choice](data))