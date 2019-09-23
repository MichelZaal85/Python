#!/usr/bin/python
try:
    import time
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except Exception as e:
    input(e)


class MyHandler(FileSystemEventHandler):

    def on_deleted(self,event):
        f = open('H:/Mijn Documenten/TXT/Logboeken/Log J.txt', 'a')
        f.write('Deleted:\t' + str(event.src_path) + '\n')
        f.close()
        print('file was deleted:\t', event)

    def on_created(self, event):
        f = open('H:/Mijn Documenten/TXT/Logboeken/Log J.txt', 'a')
        f.write('Created:\t' + str(event.src_path) + '\n')
        f.close()
        print('something got created\t', event)

    def on_moved(self, event):
        f = open('H:/Mijn Documenten/TXT/Logboeken/Log J.txt', 'a')
        f.write('Moved\t' + str(event.src_path) + ' --> ' + str(event.dest_path) + '\n')
        f.close()
        print('Something got moved:\t', event)


if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='c:/', recursive=True)
    observer.start()
    print('...WatchDog is Monitoring your folders...\n\n')

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('Program Stop!')
        observer.stop()
    observer.join()


'''
# simple example
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
'''
