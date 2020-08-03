import xlrd,os
from IPy import IP
class VlanConfig:
    vlan =""
    floor=""
    ipaddr=""
    netmask=""
    network_number=""
    virtual_gateway=""
    master_gateway=""
    backup_gateway=""
workbook = xlrd.open_workbook('C:\\Users\\alawn\\Desktop\\configuration-file\\Manage-IP.xlsx')
sheet = workbook.sheet_by_name('IP-Planing')
nrows = sheet.nrows
dict = {}
for n in range (1,nrows):
    t = VlanConfig()
    t.vlan = str(int((sheet.row(n)[1].value)))
    if sheet.row(n)[3].value =='':
        t.floor='emtpy'
    else:
        t.floor = str(int((sheet.row(n)[3].value)))
    t.ipaddr = IP(sheet.row(n)[0].value)
    t.netmask = str(t.ipaddr.netmask())
    t.network_number = IP(t.ipaddr.strNormal(0)).int()
    t.virtual_gateway = IP(t.network_number + 1).strNormal(0)
    t.master_gateway = IP(t.network_number + 2).strNormal(0)
    t.backup_gateway = IP(t.network_number + 3).strNormal(0)
    if t.floor in dict:
        dict[t.floor].append(t);''
    else:
        dict[t.floor]=[]
        dict[t.floor].append(t)
for k in dict.keys()
    os.makedirs('for k in dict.keys()')