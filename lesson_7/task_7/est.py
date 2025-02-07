import os
dir = 'D:/GeekBrains/2nd_year/Python/lesson_7/'

for root, dirs, files in os.walk(dir):
    print(dirs)

