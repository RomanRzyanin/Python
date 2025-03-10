from bird import Bird
from fish import Fish
from mammal import Mammal


class AnimalFactory:

    @staticmethod
    def create_animal(animal_type, *args):

        '''
          Создает экземпляр животного на основе переданного типа и
          параметров.
          :param animal_type: Название типа животного (например, 'Dog'
          или 'Cat')
          :param args: Параметры для конструктора животного
          :return: Экземпляр соответствующего класса животного
          '''

        animal_classes = {
            'bird': Bird,
            'fish': Fish,
            'mammal': Mammal
        }
        if animal_type.lower() in animal_classes:
            return animal_classes[animal_type.lower()](*args)
        else:
            raise ValueError(f'Неизвестный тип животного: {animal_type}')
