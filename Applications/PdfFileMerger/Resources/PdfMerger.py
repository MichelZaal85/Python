import os
import sys
from PyPDF2 import PdfFileMerger


def pdf_merger(files):

    merger = PdfFileMerger()
    for pdf in files:
        print(pdf)

    # for pdf in files:
    #     merger.append(open(pdf), 'rb')

    # with open('C:/TEMP/combined_pdf.pdf', 'wb') as fout:
    #     try:
    #         merger.write(fout)
    #     except IOError as IOerr:
    #         print(IOerr)
    #         raise


if __name__ == '__main__':
    if len(sys.argv) > 1:
        pdf_merger(sys.argv[1])
    else:
        print('\nUsage:\nPython PdfMerger [location]\n')



# import os
# import sys
# from PyPDF2 import PdfFileMerger


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


# if __name__ == '__main__':
#     if len(sys.argv) < 2:
#         print('\nUsage:\nPython PdfMerger [location]\n')
#     else:
#         pdf_merger(sys.argv[1])
