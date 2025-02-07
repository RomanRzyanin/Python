'''Задание №7
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки'''

import os

my_file_path = 'D:/GeekBrains/2nd_year/Python/lesson_7/task_7/files/'

f_video = ['.mp4', '.mkv', '.avi']
f_audio = ['.mp3', '.flac', '.aac']
f_pic = ['.jpeg', '.jpg', '.png']


def sort_files(file_path):
    os.chdir(file_path)
    if not os.path.isdir('my_video'):
        os.mkdir('my_video')
    if not os.path.isdir('my_audio'):
        os.mkdir('my_audio')
    if not os.path.isdir('my_pictures'):
        os.mkdir('my_pictures')
    list_files = []
    for dir_path, dir_name, file_name in os.walk(my_file_path):
        for name in file_name:
            list_files.append(name)
    for file in list_files:
        if any(p in file.lower() for p in f_video):
            os.replace(file, f'my_video/{file}')
        elif any(p in file.lower() for p in f_audio):
            os.replace(file, f'my_audio/{file}')
        else: #if any(p in file.lower() for p in f_pic):
            os.replace(file, f'my_pictures/{file}')


sort_files(my_file_path)
