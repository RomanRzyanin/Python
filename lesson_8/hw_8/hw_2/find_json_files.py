import os

__all__ = ['find_json_files']


def find_json_files(path):
    json_files = []
    for _, _, files in os.walk(path):
        for file in files:
            if os.path.isfile(path + '\\' + file) and file.endswith('.json'):
                json_files.append(file)
            else:
                print('Not JSON files')

    return json_files
