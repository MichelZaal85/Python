import PyPDF2
import sys


def main(file):
    file = open(file, 'rb')
    PDFfile = PyPDF2.PdfFileReader(file)
    for i in range(0, PDFfile.numPages):
        text = PDFfile.getPage(i).extractText()
        print('\nPagenum:', i, '\n\n', text, '\n')
        answer = input('continue?').lower()
        if answer == 'no' or answer == 'n':
            break
    file.close()


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        sys.exit('Missing input [file]\n')
    main(sys.argv[1])
