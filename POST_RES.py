import requests
import openpyxl
url = "URL"
path = 'C:/Users/alawnwang/Desktop/netdevice.xlsx'
txt_path = 'C:/Users/alawnwang/Desktop/post_res/'
wb = openpyxl.load_workbook(path)
ws = wb.active
row = ws.max_row
def get_post_res():
    post_res = []
    for n in range(1,row+1):
        device_id = ws.cell(row=n,column=1).value
        device_name = ws.cell(row=n,column=2).value
        payload =  "{\r\n    \"method\": \"snmp.get_snmp_data\",\r\n    \"systemid\":\"SYSID\",\r\n    \"params\": {\r\n        \"start_date\":\"2020-07-27 00:00:00\",\r\n        \"end_date\":\"2020-07-31 24:00:00\",\r\n        \"devid\":%s,\r\n        \"attr\":[\"in_traffic\"]\r\n    }\r\n}" %device_id
        headers = {'Content-Type': 'text/plain'}
        res = open(txt_path+device_name,'w')
        response = requests.request("POST", url, headers=headers, data = payload)
        post_res.append(response.text.encode('utf8'))
    return post_res
get_post_res()

for content in get_post_res():
    post_dict = eval(content)
    port_value_list = post_dict['data']
