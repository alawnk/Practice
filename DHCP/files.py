import os
Path = r'C:/Users/alawn/Desktop/DHCP/LK/'
for dir, sub_dir, files in os.walk(Path):
    for file_name in files:
        config_files = open(dir + '/' + file_name)
        done = 0
        while not done:
            configfile = config_files.readlines()
            if (configfile != ''):
                print(configfile)
            else:
                done = 1
            configfile.close()
            # done = 0
            # while not done:
            #
            # print(configfile)
            # done = 0
            # while not done:
            #
            # if aLine != '':
            #     print(aLine)
            # else:
            #     done = 1
            # file.close()
                #                 config = open (config_files)
        #                 for lines in config:
        #                     keyword = ['interface Vlan', 'ip helper-address']
        #                     pattern = re.compile('|'.join(keyword))
        #                     if pattern.search(lines):
        #                         config_file.write(lines)
        # config_file.close()


