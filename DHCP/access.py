import shutil
import xlrd
from IPy import IP

workbook = xlrd.open_workbook('C:/Users/alawn/Desktop/35F.xlsx')
sheet = workbook.sheet_by_index(2)
nrows = sheet.nrows
for n in range (1,nrows):
    ipaddr = sheet.row(n)[0].value
    netmask = sheet.row(n)[1].value
    hostname = sheet.row(n)[2].value
    network_number = (IP(ipaddr).make_net(netmask).int())
    print(type(network_number))
    gateway1 = network_number + 1
    gateway = IP(gateway1).strNormal()
    master_device = sheet.row(n)[3].value
    master_port = sheet.row(n)[4].value
    backup_device = sheet.row(n)[5].value
    backup_port = sheet.row(n)[6].value
    DES_1 = master_device+'-'+master_port
    DES_2 = backup_device+'-'+backup_port
    if 'XOA' in hostname:
        config_file = ('XOA.txt')
    elif 'EVP' in hostname:
        config_file = ('EVP.txt')
    elif 'EWL' in hostname:
        config_file = ('EWL.txt')
    new_file = ('C:\\Users\\alawnwang\\Desktop\\configuration-file\\config\\' + hostname + '.txt')
    shutil.copy(config_file, new_file)
    with open(config_file, 'r+', encoding='UTF-8') as fin:
	    with open(new_file, 'r+', encoding='UTF-8') as fout:
		    for line in fin:
			    fout.write(line.replace('$devicename', hostname).replace('$ipaddr', ipaddr).replace('$GW', gateway).replace('$mask',netmask).replace('$DES-1',DES_1).replace('$DES-2',DES_2))
	    fout.close()
    fin.close()