# pdfFileWriter -- limited to copying, rotating, overlaying, encrypting. Cannot Create PDF from text
import PyPDF2

pdf1File = open('meetingminutes.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
pdfWriter = PyPDF2.PdfFileWriter()

# PyPDF2 can only append pages!
# for page in pdf file, read and add
for pageNum in range(pdf1Reader.numPages):
	pageObj = pdf1Reader.getPage(pageNum)
	pdfWriter.addPage(pageObj)

for pageNum in range(pdf2Reader.numPages):
	pageObj = pdf2Reader.getPage(pageNum)
	pdfWriter.addPage(pageObj)

# output will be created if none exists

pdfOutputFile = open('combinedminutes.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()
