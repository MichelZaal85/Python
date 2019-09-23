#!/usr/bin/python3

'''
Author:
Michel Zaal

Name:
PDF File Merger (PFM.py)

Description:
Merge PDF files in to 1 to source directory.
'''

import os
import sys
try:
    from PyPDF2 import PdfFileMerger
except Exception:
    input('...Module not found...')
NAME = '/combined_pdf.pdf'


def checkType(arg):
    if os.path.isdir(arg[1]):
        arg = str(arg[1])
        pdf_files = [os.path.join(arg, f) for f in os.listdir(arg) if f.endswith('pdf')]
        src_loc = arg
        return pdf_files, src_loc
    src_loc = os.path.split(sys.argv[1])[0]
    pdf_files = sys.argv[1:]
    return pdf_files, src_loc


def pdfMerger(args):
    files = args[0]
    loc = args[1]
    merger = PdfFileMerger(strict=False)

    for pdf in files:
        try:
            merger.append(open(pdf, 'rb'))
        except Exception as E:
            open(loc + '/errorLog.txt', 'w').write(str(E))
            sys.exit(E)
    with open(loc + NAME, 'wb') as pdf_out:
        merger.write(pdf_out)


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        sys.exit()
    pdfMerger(checkType(sys.argv))
