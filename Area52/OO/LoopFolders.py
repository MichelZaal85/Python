import os
import sys


class main():
    '''
    class LoopFolders

    Loop Folders in given folder.
    print Root folder, sub folders, and files.
    Write output to currentdir/FileList.txt

    *Folders and file exceptions are skipped*
    '''

    def __init__(self, targetFolder):
        self.targetFolder = targetFolder
        print('Target Folder:', targetFolder)

    def loop(self):
        with open('testfileList.txt', 'w') as self.logFile:
            for root, dirs, files in os.walk(self.targetFolder):
                level = root.replace(self.targetFolder, '').count(os.sep)
                indent = ' ' * 4 * (level)
                print(f'{indent}{os.path.basename(root)}')
                subindent = ' ' * 4 * (level + 1)
                for f in files:
                    print(f'{subindent}{f}')


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        sys.exit('Expected folder input')
    looper = main(sys.argv[1])
    choice = input('Are you sure you want to do this?\n').lower()
    if choice == 'y' or 'yes':
        looper.loop()
