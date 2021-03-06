import sys
import os
try:
    import comtypes.client
    from win32com import client
except ImportError:
    input('....')


def checkType(input_file):
    file_ext = os.path.splitext(input_file)[1]
    if file_ext == '.xlsx':
        excel2PDF(input_file)
    else:
        word2PDF(input_file)


def word2PDF(arg):
    WDFORMATPDF = 17

    in_file = os.path.abspath(sys.argv[1])
    out_file = os.path.splitext(sys.argv[1])[0] + '.pdf'

    word = comtypes.client.CreateObject('Word.Application')
    doc = word.Documents.Open(in_file)
    doc.SaveAs(out_file, FileFormat=WDFORMATPDF)
    doc.Close()
    word.Quit()


def excel2PDF(doc):
    excel = client.DispatchEx("Excel.Application")
    excel.Visible = 0

    wb = excel.Workbooks.Open(doc)
    # ws = wb.Worksheets[1]

    try:
        doc = sys.argv[1][:-4] + 'pdf'
        doc = os.path.abspath(doc)
        wb.SaveAs(doc, FileFormat=57)
    except Exception as e:
        print("Failed to convert")
        print(str(e))
    finally:
        wb.Close()
        excel.Quit()


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        input('no arguments')
        sys.exit('No Arguments')
    checkType(sys.argv[1])
