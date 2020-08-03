import os
import sys
import telnetlib
commond = []
# hosname = sys.argv[1]
# username = sys.argv[2]
# password = sys.argv[3]
try:
    tn = telnetlib.Telnet('10.0.0.26','54277')
except:
    print('Can not open host')
# print(hosname)
tn.read_until(b'>')
commond = input(b'Commond:')

