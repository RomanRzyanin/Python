import json
import os


def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        data = {
            'function_name': func.__name__,
            'args': args,
            'kwargs': kwargs,
            'result': result
        }

        # if os.path.exists(file):
        #     with open(file, 'r') as f_read:
        #         js_data = json.load(f_read)
        #
        #     js_data.append(data)
        #
        #     with open(file, 'w') as f_write:
        #         json.dump(js_data, f_write, indent=2)
        #
        # else:
        #     with open(file, 'w') as f_write:
        #         json.dump(data, f_write, indent=2)

        return data

    return wrapper


@decorator
def my_func(a, b, c=3, d=5):
    return a + b + c + d


print(my_func(1, 2, c=3, d=56))
print(my_func(4, 5, c=6, d=34))


with open('test.json', 'a')as f:
    json.dump(my_func(1, 2, c=3, d=56), f, indent=2)
with open('test.json', 'a') as f:
    json.dump(my_func(4, 5, c=6, d=34), f, indent=2)