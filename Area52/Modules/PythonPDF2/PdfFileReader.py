# PdfFileReader
import PyPDF2

pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# get num of pages
pdfReader.numPages


# Extract text from 1st page
pageObj = pdfReader.getPage(0)
pageObj.extractText()

# Check if pdf document is encrypted:
pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
pdfReader.isEncrypted()
# excepted output: True

# decrypt pdfReader object
pdfReader.decrypt('rosebud')
pageObj = pdfReader.getPage(0)


def readPDF(file):
    pdfReader = PyPDF2.PdfFileReader(file)
    pdfFile = open(file, 'rb')
    for page in pdfFile:
        pdfReader.extractText()


def searchPDF(file):
    file = open(file, 'rb')
    PDFfile = PyPDF2.PdfFileReader(file)
    for i in range(0, PDFfile.numPages):
        text = PDFfile.getPage(i).extractText()
        print('\nPagenum:', i, '\n\n', text, '\n')
        answer = input('continue?').lower()
        if answer == 'no' or answer == 'n':
            break
    file.close()
