import sys
import os
from PyPDF2 import PdfFileMerger


def pdfMerger(files, loc):
    merger = PdfFileMerger()
    for pdf in files:
        try:
            merger.append(open(pdf, 'rb'))
        except Exception as E:
            input(E)
    with open(loc + '/combined_pdf.pdf', 'wb') as pdf_out:
        merger.write(pdf_out)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        pdfMerger(sys.argv, os.path.split(sys.argv[1])[0])




# def pdf_merger(loc):
#     pdfs = [p for p in os.listdir(loc)]

#     merger = PdfFileMerger()

#     for pdf in pdfs:
#         merger.append(open(os.path.join(loc, pdf), 'rb'))

#     with open(loc + '/combined_pdf.pdf', 'wb') as fout:
#         try:
#             merger.write(fout)
#         except IOError as IOerr:
#             print(IOerr)
#             raise
