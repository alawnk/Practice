import os,sys,time,re
ADDRESS = input('请输入要检测的地址:')
commond = 'ping %s -t' %ADDRESS
PING = os.popen(commond)
for p in PING:
    date = time.strftime(time.strftime('%Y-%m-%d %X', time.localtime()))
    if re.search(r'来自.*',p):
        sys.stdout.write(date+' '+p)
    elif re.search(r'一般故障',p):
        sys.stdout.write(date + ' '+p)
    else:
        sys.stdout.write(p)