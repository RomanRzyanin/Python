from random import choices, randint
from string import ascii_lowercase
from os import getcwd, makedirs, chdir

def func_1(ext, files=42, min_len=6, max_len=30, min_bytes=256, max_bytes=4096):
    for _ in range(files):
        name = ''.join(choices(ascii_lowercase, k=randint(min_len, max_len))) + ext
        with open(name, 'wb') as f:
            pass


def func_2(files=10, **kwargs):
    # values = []
    # for value in kwargs.values():
    #     values.append(value)
    for _ in range(files):
        ext = str(*choices(list(kwargs.values())))
        func_1(ext, 5)


def func_3(dir):
    my_path = getcwd() + '\\' +  dir
    try:
        makedirs(my_path)
        chdir(my_path)
    except FileExistsError:
        chdir(my_path)
    func_2(5, a='.avi', b='.flac', c='.mp3', d='.jpg', e='.mp4', f='.JPEG')
    chdir('..')


#func_1('.txt')
# func_2(5, a='.txt', b='.doc', c='.bin')
func_3('test_dir')