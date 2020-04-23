import os
import shutil
import openpyxl
PATH = 'C:/Users/alawn/Desktop/txt/'
# NEW_excel = openpyxl.Workbook()
# worksheet = NEW_excel.active
# worksheet.title = version
# i = 1
# r = 1
def move_file(PATH):
    subdir=os.listdir(PATH)
    for dir_name in subdir:
        path=os.path.join(PATH,dir_name)
        if os.path.isdir(path):
            end_dir=os.listdir(path)
            for files_name in end_dir:
                if files_name=='show version.txt':
                    os.rename(os.path.join(path,files_name),PATH+dir_name+'.txt')
                elif os.path.isdir(PATH+dir_name):
                    shutil.rmtree(PATH+dir_name)

def get_version(PATH):
    vi_list= []
    for root,dir,files in os.walk(PATH):
        for file in files:
            with open(PATH+file) as ver_file:
                ver_info = ver_file.readlines()
                for vi in ver_info:
                    if vi.startswith('*'):
                        vi_list.append(vi)
    new_list = list(set(vi_list))
    for version in new_list:
        print(version)
move_file(PATH)
get_version(PATH)

