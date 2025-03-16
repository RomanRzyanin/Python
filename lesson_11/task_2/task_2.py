'''Задание №2
Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списков архивов
list-архивы также являются свойствами экземпляра
'''


class Archive:
    """text"""
    last_num = None
    last_str = None
    str_archive = []
    nums_archive = []

    def __init__(self, number, text):
        self.number = number
        self.text = text
        # self.str_archive = []
        # self.nums_archive = []

        if Archive.last_num is not None:
            Archive.nums_archive.append(Archive.last_num)
        if Archive.last_str is not None:
            Archive.str_archive.append(Archive.last_str)
        Archive.last_num = number
        Archive.last_str = text


obj_1 = Archive(1, '1')
print(obj_1.number, obj_1.text, obj_1.nums_archive, obj_1.str_archive)
obj_2 = Archive(2, '2')
print(obj_2.number, obj_2.text, obj_2.nums_archive, obj_2.str_archive)
obj_3 = Archive(3, '3')
print(obj_3.number, obj_3.text, obj_3.nums_archive, obj_3.str_archive)
print(obj_1.nums_archive)
