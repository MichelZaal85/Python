#!/usr/bin/python
try:
    import time, PyPDF2, re
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except Exception as e:
    input('Something went horribly wrong:', e)


class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path[-4:] == '.pdf':
            print('Got a PDF file!')
            self.searchPDF(event.src_path)

    def searchPDF(self, File):
        file = open(File, 'rb')
        for i in range(PyPDF2.PdfFileReader(file).numPages):
            print(PyPDF2.PdfFileReader(file).getPage(i).extractText())
            text = PyPDF2.PdfFileReader(file).getPage(i).extractText()
            # match = re.search(r'onderhoud|inspectie|rapport', text, flags=re.M)
            dateMatch = re.search(r'(\d{2}-\d{2}-\d{4})|(\d{4}-\d{2}-\d{2})', text, flags=re.M)
            if dateMatch:
                print('Some date thingy found:', dateMatch)
                break
            # if match:
            #     print('\n\n\tFound!', match)
            #     break
        file.close()
        print('Going somewhere?')
        self.PDFfileHandler()

    def PDFfileHandler(self):
        print('somethingsomething file something')


if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='D:/Downloads', recursive=True)
    observer.start()
    print('...WatchDog is Monitoring your folders...\n\n')

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('Program Stop!')
        observer.stop()
    observer.join()

# MatchString = r'versie'
#     for i in range(PyPDF2.PdfFileReader(file).numPages):
#         print(PyPDF2.PdfFileReader(file).getPage(i).extractText())
#         PDFtext = PyPDF2.PdfFileReader(file).getPage(i).extractText()

#         if re.search(MatchString, PDFtext, flags=re.M):
#             match = re.search(MatchString, PDFtext, flags=re.M)
#             print('\n\n\tFound!', match)
#             input('continue?...')
#         else:
#             print('\t\t\tNo match')
#         choice = input('continue?: ')
#         if choice.lower() == 'no' or choice.lower() == 'n':
#             break
