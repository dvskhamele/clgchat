import xlrd
import pandas as pd
import numpy
from pyexcel_ods import save_data
file="C:/Users/aman\chatinsure\django_app\example_app\Model_mstr.xlsx"
#code=xlrd.open_workbook(file)

#code=testing_xls.ReadSpreadsheet(file)

code=pd.read_excel(file)
#print(code[0:1] )

vehical_code=code['VEHICLEMODELCODE']
print(vehical_code)

model_list=code['MANUFACTURER']
print(model_list)

#for model in vehical_code:
 ##   model=(vehical_code)
  ##  usertext=input("Enter a Model:")
   # if usertext == model:
   #     print(vehical_code[])
    

from xlrd import open_workbook
book = open_workbook(workbookName)
for sheet in code.sheets():
    for rowidx in range(sheet.nrows):
        row = sheet.row(rowidx)
        for colidx, cell in enumerate(row):
            if cell.value == "particularString" :
                print (sheet.name())
                print (colidx)
                print (rowidx)
                
#for row in range(sh.nrows):
 #   for column in range(sh.ncols):
  #      if s == sh.cell(row, column).value:  
   #         return (row, column)
#



#my_data=(code[3:1])
#print(my_data)
#code.head()

#data = OrderedDict()
