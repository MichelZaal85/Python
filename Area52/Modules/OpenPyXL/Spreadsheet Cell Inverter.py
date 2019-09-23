# Spreadsheet Cell Inverter.py
# Invert Row-Cel values. 

'''
You can write this program by using nested for loops to read in the spreadsheet’s data 
into a list of lists data structure. This data structure could have sheetData[x][y] for 
the cell at column x and row y. Then, when writing out the new spreadsheet, use 
sheetData[y][x] for the cell at column x and row y.
'''

# import required modules:
import openpyxl, os

# Load excel
wb = openpyxl.load_workbook('example.xlsx')
# get sheet title
sheet.title
# get active sheet
activeSheet = wb.get_active_sheet()
