''''''


class Decorator:
    def __init__(self, num):
        self.num = num

    def __call__(self, func):
        def wrapper():
            return func()

        return wrapper


@Decorator(5)
def my_func():
    return 'Hello world!'


print(my_func())
