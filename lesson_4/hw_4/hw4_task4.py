'''Задача 4. Функция максимума
Юра пишет различные полезные функции для Python, чтобы остальным
программистам стало проще работать. Он захотел написать функцию, которая
будет находить максимум из перечисленных чисел. Функция для нахождения
максимума из двух чисел у него уже есть. Юра задумался: может быть, её
можно как-то использовать для нахождения максимума уже от трёх чисел?
Помогите Юре написать программу, которая находит максимум из трёх чисел.
Для этого используйте только функцию нахождения максимума из двух чисел.
По итогу в программе должны быть реализованы две функции:
1. maximum_of_two — функция принимает два числа и возвращает одно
(наибольшее из двух);
2. maximum_of_three — функция принимает три числа и возвращает одно
(наибольшее из трёх); при этом она должна использовать для сравнений
первую функцию maximum_of_two.'''


def max_of_two(lst):
    '''функция принимает два числа и возвращает одно (наибольшее из двух)'''
    max_digit = lst[0]  #Можно реализовать через фенкция max(), max_digit = max(lst)
    if lst[1] > max_digit:
        max_digit = lst[1]
    return max_digit


def max_of_three(lst):
    '''функция принимает три числа и возвращает одно (наибольшее из трёх)'''
    max_digit = max_of_two((lst[0], max_of_two(lst[1:])))
    return max_digit


def main_menu():
    '''Function main menu'''
    while True:
        option = input('Выберите действие:\n 1 - сравнить 2 числа\n 2 - сравнить 3 числа\n 3 - Exit\n >>> ')
        match option:
            case '1':
                text = input('Введите 2 числa через пробел: ')
                if text.replace(' ', '').isdigit() and len(list(map(int, text.split()))) == 2:
                    digit = list(map(int, text.split()))
                    print(f'Max number = {max_of_two(digit)}\n')
                else:
                    print('Error. Enter two numbers.\n')
            case '2':
                text = input('Введите 3 числa через пробел: ')
                if text.replace(' ', '').isdigit() and len(list(map(int, text.split()))) == 3:
                    digit = list(map(int, text.split()))
                    print(f'Max number = {max_of_three(digit)}\n')
                else:
                    print('Error. Enter two numbers.\n')
            case '3':
                print('Goodbye', 'We are waiting for you again :(', sep='\n')
                exit()
            case _:
                print('Введите число от 1 до 3: \n')


main_menu()
