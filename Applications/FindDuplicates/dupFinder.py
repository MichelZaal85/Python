# dupFinder.py
import os
import sys
import hashlib


ROOT = 'C:/Users/ZaaJM/Dropbox/Python/Applications/FindDuplicates/'
FILE = 'Duplicates.txt'
doubles = []
LF = '\n\r'
LB = '___________________'


def main():
    dups = {}
    folders = sys.argv[1:]
    for i in folders:
        # Iterate the folders given
        if os.path.exists(i):
            # Find the duplicated files and append them to the dups
            joinDicts(dups, findDup(i))
        else:
            print(f'{i} is not avalid path, please verify')
            sys.exit()
    printResults(dups)
    return


def findDup(parentFolder):
    # Dups in format {hash:[names]}
    dups = {}
    for dirName, subdirs, fileList in os.walk(parentFolder):
        print(f'Scanning {dirName}...')
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(dirName, filename)
            # Calculate hash
            file_hash = hashfile(path)
            # Add or append the file path
            if file_hash in dups:
                dups[file_hash].append(path)
            else:
                dups[file_hash] = [path]
    return dups


# Joins two dictionaries
def joinDicts(dict1, dict2):
    for key in dict2.keys():
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key]
        else:
            dict1[key] = dict2[key]


def hashfile(path, blocksize=65536):
    try:
        afile = open(path, 'rb')
        hasher = hashlib.md5()
        buf = afile.read(blocksize)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(blocksize)
        afile.close()
        return hasher.hexdigest()
    except IOError as IOerr:
        print(IOerr)
        pass


def printResults(dict1):
    dupFiles = open(ROOT + FILE, 'w', buffering=1)
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:
        print('Duplicates Found:')
        print('The following content is identical')
        print(LB)
        for result in results:
            for subresult in result[1::]:
                print(f'\t\t{subresult}')
                try:
                    dupFiles.write(f'{subresult}{LF}')
                    doubles.append(subresult)
                except Exception:
                    continue
            print(LB)
            dupFiles.write(f'{LB}{LF}')
        dupFiles.close()
    else:
        input('\nNo duplicate files found.')
        sys.exit('Clean Exit')


def duplicateRemover(doubles):
    err_log = open(ROOT + 'ErrLog.txt', 'w')
    print(f'Duplicates: {len(doubles)}')
    answer = input('\nRemove duplicates? [Y/n]').lower()
    if answer.lower() == 'n':
        sys.exit('Program terminated')

    for double in doubles:
        try:
            os.remove(double)
            print(f'Removing {double}')
        except Exception as E:
            print(E)
            err_log.write(f'{E}{LF}')
    err_log.close()
    input('Program finished with no errors')
    sys.exit('Clean Exit')


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        sys.exit('DupFinder.py :: folder | folder1 folder2 folder3')
    main()
    duplicateRemover(doubles)
