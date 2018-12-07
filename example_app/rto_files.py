import pandas as pd
from . models import *

excel_file = 'RTO_Mstr.xls'
movies = pd.read_excel(excel_file)
movies_sheet1 = pd.read_excel(excel_file, sheet_name=0)

a=[]
for t in range(0,1277):
		keyword = ""
		keyword = keyword.strip().upper()
		code = movies_sheet1.iat[t,3]
		code = str(code).strip().upper()
		name = movies_sheet1.iat[t,4]
		name = str(name).strip().upper()
		state_code = movies_sheet1.iat[t,2]
		city_code = movies_sheet1.iat[t,2]
		try:
			rto=RTO.objects.get(loct_code=code,loct=name)
			rto.state_code=movies_sheet1.iat[t,1]
			rto.city_code=RTO.objects.get(loct_code=code,loct=name)
			print(rto.save())
			print(city_code)
		except:
			print(RTO.objects.create(loct_code=code,loct=name,state_code=movies_sheet1.iat[t,1],city_code=movies_sheet1.iat[t,2]))
