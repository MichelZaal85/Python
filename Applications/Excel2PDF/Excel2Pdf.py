import sys
import os
from win32com import client
# import win32api


def exceltopdf(doc):
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


# input_file = sys.argv[1]
exceltopdf(sys.argv[1])
