"""
3. Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...


@type_logger
def calc_cube(x):
   return x ** 3

# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую;
можете ли вы вывести тип значения функции?
Сможете ли решить задачу для именованных аргументов?
Сможете ли вы замаскировать работу декоратора?
Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)
"""
from functools import wraps


def type_logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        arg_types = ", ".join(map(lambda x: f'{x}: {type(x).__name__}', args))
        kwarg_types = ", ".join(map(lambda pair: f'{pair[0]}={pair[1]}: {type(pair[1]).__name__}', kwargs.items()))
        if arg_types and kwarg_types:
            kwarg_types = ', ' + kwarg_types
        print(f'Is called {func.__name__}({arg_types}{kwarg_types}) -> {type(result).__name__}')
        return result

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(3)
print(a)
