import openpyxl
from openpyxl.styles import Font, NamedStyle
wb = openpyxl.Workbook()
sheet = wb.get_sheet_by_name('Sheet')
italic24Font = Font(size=24, italic=True, name='Arial')
styleObj = NamedStyle(name='italic', font=italic24Font)

sheet['A1'].style = styleObj
sheet['A1'] = 'Hello world!'
wb.save('UpdatedStyled.xlsx')
