import xlwt
import xlrd
from xlutils.copy import copy
 
# load the excel file
rb = xlrd.open_workbook('d:/GitHub/testrepo/python/csalad01.xlsx')
 
# copy the contents of excel file
wb = copy(rb)
 
# open the first sheet
w_sheet = wb.get_sheet(0)
 
# row number = 0 , column number = 1
w_sheet.write(2,1,'Modified !')
 
# save the file
wb.save('d:/GitHub/testrepo/python/csalad01.xlsx')