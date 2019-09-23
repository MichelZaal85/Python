# csv2txt.py
'''
Spreadsheet to Text Files

Write a program that performs the tasks of the previous program in 
reverse order: The program should open a spreadsheet and write the 
cells of column A into one text file, the cells of column B into 
another text file, and so on.
'''

# load required modules:
import openpyxl, os

# Load excel
wb = openpyxl.load_workbook('example.xlsx')
# get all the sheet_names
wb.get_sheet_names()
# get a sheet by it's name
sheet = wb.get_sheet_by_name('Sheet3')
# check type of sheet
type(sheet)
# get sheet title
sheet.title
# get active sheet
activeSheet = wb.get_active_sheet()
