import xlrd
from IPy import IP
from io import StringIO
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
for n in range(1, nrows):
    t = VlanConfig()
    t.vlan = str(int((sheet.row(n)[1].value)))
    if sheet.row(n)[3].value == '':
        t.floor = 'emtpy'
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
        dict[t.floor].append(t);
        ''
    else:
        dict[t.floor] = []
        dict[t.floor].append(t)
template1 = ""
def interface_vlan():
    with open(r'D:\GITHUB\Profile_generation\template\Master-VLAN.txt', 'r+' ) as fout1:#,open(r'D:\GITHUB\Profile_generation\template\Backup-VLAN.txt', 'r+' ) as fout2:
        template1=fout1.read()
    fout1.close()
    for k in dict.keys():
        m = StringIO(k)
        print(m)
        for v in dict[k]:
            m.write(template1.replace('$vlan_num', v.vlan).replace('$master_gateway', v.master_gateway).replace('$v_gateway', v.virtual_gateway).replace('$mask',v.netmask).replace('$vlan_name',v.vlan_name))
        print(m.getvalue())
        m.close()
print (interface_vlan())

def master_config():
    with open(r'D:\GITHUB\Profile_generation\template\DOA-Master.txt', 'r+' ) as config1:
        master_config = config1.read()
    config1.close()
    for k in dict.keys():
        with open(r'D:\config_profile\master-floor-' + k + '.txt', 'a+') as nc:
            nc.seek(0, 0)
            nc.truncate()
#             for  in dict[k]:
#                 nc.write(master_config.replace('$vlan_num', m.interface_vlan()))
#         nc.close()
# print(master_config())