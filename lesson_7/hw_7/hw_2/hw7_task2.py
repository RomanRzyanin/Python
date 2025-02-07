'''Задача 2. Создание архива каталога
Напишите скрипт, который создает архив каталога в формате .zip. Скрипт
должен принимать путь к исходному каталогу и путь к целевому архиву. Архив
должен включать все файлы и подпапки исходного каталога.'''

import os
import zipfile


def zip_directory(source_dir, output_zip):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, source_dir))


zip_directory('D:/GeekBrains/nd_year/Python/lesson_7', 'D:/GeekBrains/nd_year/Python/lesson_7/output.zip')
