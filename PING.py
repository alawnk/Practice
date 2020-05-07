import re
import subprocess
from io import StringIO
import multiprocessing
import time
import sys
from IPy import IP
def check_alive(ip):
    result = subprocess.call('ping -w 1000 -n 1 %s' %ip,stdout=subprocess.PIPE,shell=True)
    if result == 0:
        h = subprocess.getoutput('ping ' + str(ip))
        returnnum = h.split('平均 = ')[1]
        info = ('\033[32m%s\033[0m 能ping通，延迟平均值为：%s' %(ip,returnnum))
        print('\033[32m%s\033[0m 能ping通，延迟平均值为：%s' %(ip,returnnum))
        return info
    else:
        with open('C:/Users/alawn/Desktop/res.txt','a+') as f:
            f.write(str(ip)+' 可用'+'\n')
        info = ('\033[31m%s\033[0m ping 不通！' % ip)
        return info
        print('\033[31m%s\033[0m ping 不通！' % ip)
if __name__ == '__main__':
    network = input('network:')
    print("开始批量ping所有IP！")
    for ip in IP(network):
        p = multiprocessing.Process(target=check_alive, args=(ip,))
        p.start()