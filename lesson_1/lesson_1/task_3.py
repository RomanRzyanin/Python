# task_3

def func(year):
    return 'yes' if year % 400 == 0 or year % 4 == 0 and year % 100 != 0 else 'no'


print(func(2024))
