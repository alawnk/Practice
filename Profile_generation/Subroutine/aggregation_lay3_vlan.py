import xlrd
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

workbook = xlrd.open_workbook(r'D:\GITHUB\Profile_generation\Manage-IP.xlsx')
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
    t.vlan_name = str(sheet.row(n)[2].value)
    t.virtual_gateway = IP(t.network_number + 1).strNormal(0)
    t.master_gateway = IP(t.network_number + 2).strNormal(0)
    t.backup_gateway = IP(t.network_number + 3).strNormal(0)
    if t.floor in dict:
        dict[t.floor].append(t);''
    else:
        dict[t.floor]=[]
        dict[t.floor].append(t)
        print(t.floor)
with open(r'D:\GITHUB\Profile_generation\template\Master-Vlan.txt', 'r+' ) as fout1,open(r'D:\GITHUB\Profile_generation\template\Backup-VLAN.txt', 'r+' ) as fout2:
    template1=fout1.read()
    template2=fout2.read()
fout1.close()
fout2.close()
for k in dict.keys():
    with open (r'D:\config_profile\master-floor-'+k+'.txt','a+') as m:
        m.seek(0,0)
        m.truncate()
        for v in dict[k]:
            m.write(template1.replace('$vlan_num', v.vlan).replace('$master_gateway', v.master_gateway).replace('$v_gateway', v.virtual_gateway).replace('$mask',v.netmask).replace('$vlan_name',v.vlan_name))
    m.close()
    with open (r'D:\config_profile\backup-floor-'+k+'.txt','a+') as b:
        for v in dict[k]:
            b.write(template2.replace('$vlan_num', v.vlan).replace('$backup_gateway', v.backup_gateway).replace('$v_gateway', v.virtual_gateway).replace('$mask',v.netmask).replace('$vlan_name',v.vlan_name))
    b.close()


# master = open('C:\\Users\\alawnwang\\Desktop\\configuration-file\\master.txt','r')
# try:
#     master_config = master.read()
# finally:
#     master.close()
# print(master_config)
# backup = open ('C:\\Users\\alawnwang\\Desktop\\configuration-file\\backup.txt','r')
# try:
#     backup_config = backup.read()
# finally:
#     backup.close()
# print(backup_config)
