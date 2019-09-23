# Remove files with certain extension from given folder

import os
import sys


def main(folder, extension, switch):
    found = False
    # print(f'Debug: {folder} | {extension} | {switch} {type(switch)}')
    if '.' not in extension:
        extension = '.' + extension
    for root, subs, files in os.walk(folder):
        for file in files:
            if file.endswith(extension):
                print(f'Found {root} {file}')
                found = True
                if switch:
                    try:
                        print(f'Removing: {os.path.join(root, file)}')
                        os.remove(os.path.join(root, file))
                    except IOError as E:
                        print(E)
                        continue
    if not switch and found:
        print('\nFiles found, Use program with [True] to remove found files')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        info = '''
  PurgeExtension.py
  -----------------
  Remove file with given extension.

  Usage:
  rmFext.py [folder] [extension] [True / False] :: True for deletion
'''
        input(info)
        # sys.exit('Expected; Folder, extension, T/F[dry-run]\n')
    if len(sys.argv) == 3:
        os.system('cls')
        main(sys.argv[1], sys.argv[2], False)
    else:
        os.system('cls')
        main(sys.argv[1], sys.argv[2], sys.argv[3])
