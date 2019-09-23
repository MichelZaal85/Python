import openpyxl

wb = openpyxl.Workbook()
sheet = wb.get_active_sheet()

sheet.freeze_panes = 'A2' # Row 1
sheet.freeze_panes = 'B1' # Column A
sheet.freeze_panes = 'C1' # Columns A & B
sheet.freeze_panes = 'A1' # No frozen
sheet.freeze_panes = None # panes

wb = openpyxl.load_workbook('examples/produceSales.xlsx')
sheet = wb.get_active_sheet()
sheet.freeze_panes = 'A2'
wb.save('freezeExample.xlsx')