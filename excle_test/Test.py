import os
import openpyxl



file_name = os.path.join(os.path.dirname(os.path.dirname(__file__)), "excel.xlsx")
print(os.path.dirname(os.path.dirname(__file__)))
print(file_name)

wb = openpyxl.load_workbook(file_name)
names = wb.get_sheet_names
print(names)
wb_login_ = wb['login']

value = wb_login_.cell(2, 2).value
print(value)