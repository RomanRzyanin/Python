import json

__all__ = ['read_json_files']

def read_json_files(files, path):
    result = []
    for file in files:
        with open(path + file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            result.extend(data)
    return result

