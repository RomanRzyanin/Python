'''Задание №3
✔ Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более короткого файла,
возвращайтесь в его начало.'''

__all__ = ['w_newfile', 'read_f_name', 'read_f_digit']


def read_f_digit():
    with open('../task_1/tst.txt', 'r', encoding='utf-8') as f_d:
        dig = f_d.readlines()
    return dig


def read_f_name():
    with open('names.txt', 'r', encoding='utf-8') as f_n:
        name = f_n.readlines()
    return name


def w_newfile(fd, fn):
    with open('new_file.txt', 'a', encoding='utf-8') as f:
        if len(fd) < len(fn):
            for i in range(len(fn)):
                if i < len(fd):
                    res = int(fd[i].rstrip('\n').split('|')[0].strip()) * float(
                        fd[i].rstrip('\n').split('|')[1].strip())
                    if res <= 0:
                        print(f'{fn[i].rstrip('\n').lower():<8}: {round(abs(res), 3)}', file=f)
                    else:
                        print(f'{fn[i].rstrip('\n').upper():<8}: {round(res)}', file=f)
                else:
                    res = int(fd[i - len(fd)].rstrip('\n').split('|')[0].strip()) * float(
                        fd[i - len(fd)].rstrip('\n').split('|')[1].strip())
                    if res <= 0:
                        print(f'{fn[i].rstrip('\n').lower():<8}: {round(abs(res), 3)}', file=f)
                    else:
                        print(f'{fn[i].rstrip('\n').upper():<8}: {round(res)}', file=f)
        else:
            for i in range(len(fd)):
                if i < len(fn):
                    res = int(fd[i].rstrip('\n').split('|')[0].strip()) * float(
                        fd[i].rstrip('\n').split('|')[1].strip())
                    if res <= 0:
                        print(f'{fn[i].rstrip('\n').lower():<8}: {round(abs(res), 3)}', file=f)
                    else:
                        print(f'{fn[i].rstrip('\n').upper():<8}: {round(res)}', file=f)
                else:
                    res = int(fd[i].rstrip('\n').split('|')[0].strip()) * float(
                        fd[i].rstrip('\n').split('|')[1].strip())
                    if res <= 0:
                        print(f'{fn[i - len(fn)].rstrip('\n').lower():<8}: {round(abs(res), 3)}', file=f)
                    else:
                        print(f'{fn[i - len(fn)].rstrip('\n').upper():<8}: {round(res)}', file=f)



