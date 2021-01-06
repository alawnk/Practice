import os
import queue
import threading
import openpyxl
POST_FILE = '/Volumes/Mac OS DATA/EB_POST_RES/'



myq = queue.Queue()
for root, dir, files in os.walk(POST_FILE):
    for file in files:
        myq.put(file)

WORKBOOK = openpyxl.Workbook()
WORKSHEET = WORKBOOK.create_sheet('max_traffic')
WORKSHEET.append(['设备名称','端口','流量'])

def get_max_traffic():
    while True:
        try:
            info = myq.get(block=False)
            with open(POST_FILE+info) as taffic_file:
                file_dict = eval(taffic_file.read())
                traffic_data = file_dict['data']
                KEYS = traffic_data.keys()
                for key in KEYS:
                    traffic_value = traffic_data[key]
                    value_list = []
                    for value in traffic_value:
                        value_list.append(value['in_traffic'])
                    data = info,key,max(value_list)
                    WORKSHEET.append(data)
        except queue.Empty:
            break

thread_arr = []

num_thread = 20

for i in range (num_thread):
        t = threading.Thread(target = get_max_traffic,kwargs={})
        t.setDaemon(True)
        t.start()
        thread_arr.append(t)

for i in range(num_thread):
        thread_arr[i].join()

WORKBOOK.save('/Volumes/Mac OS DATA/max_traffic.xlsx')
