import os
import get_size

__all__ = ['scan_dir']


#
# def get_size(path):
#     if os.path.isfile(path):
#         return os.path.getsize(path)
#     elif os.path.isdir(path):
#         total_size = 0
#         for dirpath, _, filenames in os.walk(path):
#             for filename in filenames:
#                 file_path = os.path.join(dirpath, filename)
#                 total_size += os.path.getsize(file_path)
#         return total_size


def scan_dir(my_dir):
    result = []
    for root, dirs, files in os.walk(my_dir):
        for name in dirs + files:
            path = os.path.join(root, name)
            is_dir = os.path.isdir(path)
            size = get_size.get_size(path)
            parent = os.path.basename(root)
            result.append({
                'name': name,
                'path': path,
                'type': 'directory' if is_dir else 'file',
                'size': size,
                'parent': parent
            })
    return result

#print(scan_dir('D:/GeekBrains/2nd_year/Python/lesson_8'))

# if __name__ == '__main__':
#     scan_dir()
