import PyPDF2
pdfFile = 'meetingminutes.pdf'
pdfFileObj = open(pdfFile, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
# excepted output:
# 19

pageObj = pdfReader.getPage(0)
print(pageObj.extractText())
input('\nPress \'Enter\' to continue')

# excepted output:
'''
	'OOFFFFIICCIIAALL BBOOAARRDD MMIINNUUTTEESS Meeting of March 7, 2015
	\n The Board of Elementary and Secondary Education shall provide leadership
	and create policies for education that expand opportunities for children,
	empower families and communities, and advance Louisiana in an increasingly
	competitive global market. BOARD of ELEMENTARY and SECONDARY EDUCATION '
'''


import PyPDF2
pdfFile = ''
pdfFileObj = open('pdfFile', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage(0)
print(pageObj.extractText())
input('\nPress \'Enter\' to continue')
