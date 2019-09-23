import sys
import os
import comtypes.client


def main(arg):
    WDFORMATPDF = 17

    in_file = os.path.abspath(sys.argv[1])
    out_file = os.path.splitext(sys.argv[1])[0] + '.pdf'

    word = comtypes.client.CreateObject('Word.Application')
    doc = word.Documents.Open(in_file)
    doc.SaveAs(out_file, FileFormat=WDFORMATPDF)
    doc.Close()
    word.Quit()


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        sys.exit('No Arguments')
    main(sys.argv[1])
