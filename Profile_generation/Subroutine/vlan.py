import xlrd
from IPy import IP
class Vlandes:
    vlan =""
    Function=""

workbook = xlrd.open_workbook(r'D:\GITHUB\Profile_generation\Manage-IP.xlsx')
sheet = workbook.sheet_by_name('IP-Planing')
nrows = sheet.nrows
Vdict = {}
for n in range (1,nrows):
    v = Vlandes()
    v.vlan = str(int((sheet.row(n)[1].value)))
    if sheet.row(n)[3].value =='':
        v.floor='emtpy'
    else:
        v.floor = str(int((sheet.row(n)[3].value)))
    v.function = sheet.row(n)[2].value
    if v.floor in Vdict:
        Vdict[v.floor].append(v);''
    else:
        Vdict[v.floor]=[]
        Vdict[v.floor].append(v)
        print(v.floor)
with open(r'D:\GITHUB\Profile_generation\template\vlan.txt', 'r+' ) as fout1:#open(r'D:\GITHUB\Profile_generation\template\Backup-VLAN.txt', 'r+' ) as fout2:
    template1=fout1.read()
#    template2=fout2.read()
fout1.close()
#fout2.close()
for vn in Vdict.keys():
    with open (r'D:\config_profile\master-floor-'+vn+'.txt','a+') as m:
        m.seek(0,0)
        m.truncate()
        for y in Vdict[vn]:
            m.write(template1.replace('$vlan-num', y.vlan).replace('$vlan-name', y.function))
    m.close()