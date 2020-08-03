import os
import re

Path = r'C:/Users/alawn/Desktop/DHCP/LK/'
for dir, sub_dir, files in os.walk(Path):
    for sub_dir_name in sub_dir:
        with open(r'C:/Users/alawn/Desktop/dhcp_config/' + sub_dir_name + '.txt', 'a+') as config_file:
            config_file.seek(0, 0)
            config_file.truncate()
            for dir, sub_dir, files in os.walk(Path):
                for file_name in files:
                    config_files = open(dir + '/' + file_name)
                    for lines in config_files.readlines():
                        keyword = ['interface Vlan', 'ip helper-address']
                        pattern = re.compile('|'.join(keyword))
                        if pattern.search(lines):
                            config_file.write(lines)
        config_file.close()







