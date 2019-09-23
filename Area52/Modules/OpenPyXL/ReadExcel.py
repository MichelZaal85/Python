# readCensusExcel.py -- Tabulates population and number of census tract for each county
import openpyxl, pprint

excelFile = 'ExampleExcel.xlsx'

print('Opening workbook...')
try:
	wb = openpyxl.load_workbook(excelFile)
except:
	print('failed to open', excelFile)

sheet = wb.get_sheet_by_name('Population by Census Tract')
countyData = {}

print('Reading rows...')
for row in range(2, sheet.max_row + 1):
	# earch row in the spreadsheet has data for one census tract.
	state = sheet['B' + str(row)].value
	county = sheet['C' + str(row)].value
	pop = sheet['D' + str(row)].value

	# making sure the key for this state exists.
	countyData.setdefault(state, {})
	# makeing sure that the key for this county exists.
	countyData[state].setdefault(county, {'tracts':0, 'pop': 0})

	# Each row represents one census tract, so increment by 1.
	countyData[state][county]['tracts'] += 1
	# Increase the county pop by the pop in this census tract.
	countyData[state][county]['pop'] += int(pop)

print('Writing results...')
resultFile = open(excelFile + ' ' + str(2018), 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('All Done')
