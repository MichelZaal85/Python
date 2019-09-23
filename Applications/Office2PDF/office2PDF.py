#!/usr/bin/python3

'''
Author:      Michel Zaal
Name:        office2PDF.py
Description: Convert docx | xlsx document to PDF
'''
import sys
import os
import time
try:
    import comtypes.client
    from win32com import client
except ImportError:
    input('....')


def checkType(input_file):
    file_ext = os.path.splitext(input_file)[1]
    if file_ext.lower() == '.xlsx':
        excel2PDF(input_file)
    else:
        word2PDF(input_file)


def word2PDF(arg):
    print('Thank you for using, office2PDF.py')
    print(f'Converting {os.path.basename(arg)} to PDF')
    WDFORMATPDF = 17

    in_file = os.path.abspath(sys.argv[1])
    out_file = os.path.splitext(sys.argv[1])[0] + '.pdf'

    word = comtypes.client.CreateObject('Word.Application')
    doc = word.Documents.Open(in_file)
    doc.SaveAs(out_file, FileFormat=WDFORMATPDF)
    doc.Close()
    word.Quit()


def excel2PDF(xls):
    print('Thank you for using, office2PDF.py')
    print(f'converting {os.path.basename(xls)} to PDF')
    excel = client.DispatchEx("Excel.Application")
    excel.Visible = 0

    wb = excel.Workbooks.Open(xls)

    try:
        xls = sys.argv[1][:-4] + 'pdf'
        xls = os.path.abspath(xls)
        wb.SaveAs(xls, FileFormat=57)
        print('File conversion succesful')
        time.sleep(3)
    except Exception as e:
        print("Failed to convert")
        print(str(e))
        time.sleep(5)
    finally:
        wb.Close()
        excel.Quit()
        print('exiting office2PDF.py')
        time.sleep(5)


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        input('no arguments')
        sys.exit('No Arguments')
    checkType(sys.argv[1])
