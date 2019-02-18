from collections import defaultdict
import os
import sys


def put_files_to_storage(folder_path, storage):
    for directory, subdirectories, files in os.walk(folder_path):
        for filename in files:
            full_path = os.path.join(directory, filename)
            file_size = os.path.getsize(full_path)
            storage[filename, file_size].append(full_path)


def get_dublicates(storage):
    keys_with_dublicates = filter(lambda x: len(storage[x]) > 1, storage.keys())
    dublicates_info = list(map(lambda x: (x, storage[x]), keys_with_dublicates))
    return dublicates_info

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage: {0} + folder path'.format(sys.argv[0]))
        sys.exit()
    folder_path = sys.argv[1]
    if not os.path.isdir(folder_path):
        sys.exit('Please pass correct directory name')
    storage = defaultdict(list)
    put_files_to_storage(folder_path, storage)
    dublicates_info = get_dublicates(storage)
    if not dublicates_info:
        sys.exit('No dublicates founded')
    for file_info, file_path in dublicates_info:
        print('Dublicates {0} founded at {1}'.format(file_info[0], file_path))