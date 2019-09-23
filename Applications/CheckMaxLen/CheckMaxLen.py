import os
import sys
import time


def checkFileLen(folder):
    max_len = 250
    file_found = False
    LF = '\n'
    log = open('c:/TEMP/Max_Len_Log.txt', 'w')
    for root, subs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            if len(file_path) > max_len:
                print(file)
                log.write(f'{root}{LF}{file} :: {len(file_path) - max_len}{LF}{LF}')
                file_found = True
    if not file_found:
        log.close()
        print('Everything is OK')
    else:
        print('....File(s) found....')
        log.close()
        os.startfile('c:/TEMP/Max_Len_Log.txt')
    log.close()


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        sys.exit('Expected input [folder]')
    checkFileLen(sys.argv[1])
    time.sleep(1)
