import os,openpyxl
def io_value_new():
    port_value_new = 'C:/Users/alawn/Desktop/result_new/'
    for root,dir,files in os.walk(port_value_new):
        for file_name in files:
            workbook = openpyxl.load_workbook(port_value_new + file_name)
            sheets = workbook.sheetnames
            for i in range(len(sheets)):
                sheet = workbook[sheets[i]]
                row = sheet.max_row
                input=[]
                output=[]
                for n in range (2,row):
                    port_num = sheet.cell(row=n,column=1).value
                    input_value = sheet.cell(row=n, column=3).value
                    input.append(input_value)
                    output_value = sheet.cell(row=n, column=4).value
                    output.append(output_value)
                print(file_name,port_num,max(input),max(output))
io_value_new()
    #
    # io_value_new = []
    # port_value_new = openpyxl.load_workbook('C:/Users/alawn/Desktop/result_new')
