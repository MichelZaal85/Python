# txt2cvs.py

'''
Text Files to Spreadsheet

Write a program to read in the contents of several text files 
(you can make the text files yourself) and insert those contents 
into a spreadsheet, with one line of text per row. The lines of 
the first text file will be in the cells of column A, the lines 
of the second text file will be in the cells of column B, and so on.

Use the readlines() File object method to return a list of strings, 
one string per line in the file. For the first file, output the first 
line to column 1, row 1. The second line should be written to 
column 1, row 2, and so on. The next file that is read with readlines() 
will be written to column 2, the next file to column 3, and so on.
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
