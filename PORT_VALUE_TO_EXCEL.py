import os
import pandas as pd
PATH = 'C:/Users/alawn/Desktop/DZ_Traffice/'
NEW_PATH = 'C:/Users/alawn/Desktop/DZ_TEST/'
def write_excel():
    for root,dir,files in os.walk(PATH):                                                       #遍历获取数据txt文件
        for file in files:                                                                    #获取单个文件
            WRITE_EXCEL = pd.ExcelWriter(NEW_PATH+file+'.xlsx')                               #定义要写入的excel文件
            with open(PATH+file) as F:                                                        #打开txt文件
                FILE_CONTENT = eval(F.read())                                                 #提取数据类型
                PORT_VALUE_LIST = FILE_CONTENT['data']                                        #根据key获取数据
                KEYS = PORT_VALUE_LIST.keys()                                                 #获取key列表
                sheet_num = []                                                                #定义文件名称
                for n  in range (1,len(KEYS)+1):
                    sheet_num.append(n)
                for key in KEYS:                                                              #遍历key列表
                    if sheet_num != []:                                                       #检查文件名列表是否为空
                        port = pd.DataFrame(PORT_VALUE_LIST[key])
                        port.insert(loc=0,column='Port',value=key)                            #excel表格中插入PORT字段
                        port.to_excel(WRITE_EXCEL,sheet_name=('port'+str(sheet_num.pop(0))),index=None)   #写入excel文件
                    else:
                        pass
            WRITE_EXCEL.save()
write_excel()