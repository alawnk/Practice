import os
import re

Path = 'C:/Users/alawn/Desktop/DHCP/WLC'
for dir in os.listdir(Path):
    with open(r'C:/Users/alawn/Desktop/dhcp_config_files/sz/' + dir + '.txt', 'a+') as config_file:
        config_file.seek(0, 0)
        config_file.truncate()
        for dir, sub_dir, files in os.walk(Path):
            for file_name in files:
                config_files = open(dir + '/' + file_name)
                for lines in config_files:
                    keyword = ['hostname','interface Vlan','ip address','ip helper-address']
                    pattern = re.compile('|'.join(keyword))
                    if pattern.search(lines):
                        config_file.write(lines)
    config_file.close()