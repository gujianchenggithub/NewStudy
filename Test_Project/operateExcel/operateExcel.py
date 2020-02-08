import xlrd
import json
from xlutils.copy import copy
import os

# 读取excel中的数据
file='test.xls'
workbook=xlrd.open_workbook(filename=file)  #文件的路径  默认当前路径
worksheet1=workbook.sheet_by_name('学生')   #读取哪一个sheet页
cellData=worksheet1.cell(3,3).value        #读取这个sheet页的单元格
data=json.loads(cellData)      #将字符串转换为json格式，否则不能接口会发送失败
print(data)


# 写入excel中数据
import xlwt
# rb=xlrd.open_workbook(file)
# wb=copy(rb)
# sheet=wb.get_sheet(0)
# sheet.write(8,0,'xc')
# sheet.write(9,0,'xc')
# sheet.write(10,0,'xc')
# sheet.write(11,0,'xc')
# sheet.write(12,0,'xc')
# os.remove(file)
# wb.save(file)