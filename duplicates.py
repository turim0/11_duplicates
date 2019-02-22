from collections import defaultdict
import os
import sys
import argparse


def put_files_to_storage(folder_path):
    storage = defaultdict(list)
    for directory, subdirectories, files in os.walk(folder_path):
        for filename in files:
            full_path = os.path.join(directory, filename)
            file_size = os.path.getsize(full_path)
            storage[filename, file_size].append(full_path)
    return storage


def get_duplicates(storage):
    duplicates_info = {file_info: file_paths
                       for file_info, file_paths in storage.items() if len(file_paths)>1
                       }
    return duplicates_info


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('folder_path', help='input folder path')
    arg = parser.parse_args()
    folder_path = arg.folder_path
    if not os.path.isdir(folder_path):
        sys.exit('Please pass correct directory name')
    storage = put_files_to_storage(folder_path)
    duplicates_info = get_duplicates(storage)
    if not duplicates_info:
        print("No dublicates founded")
        sys.exit()
    for file_info, file_paths in duplicates_info.items():
        print('Founded dublicates {0}: {1} bytes'.format(*file_info))
        print("\n".join(file_paths))
