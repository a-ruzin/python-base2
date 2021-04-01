"""
4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные
значения функции и выбрасывать исключение ValueError, если что-то не так, например:
def val_checker...
    ...


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5
"""


def val_checker(validator_func):

    def decorator(func):

        def validated_func(*args, **kwargs):
            if validator_func(*args, **kwargs):
                return func(*args, **kwargs)
            else:
                raise ValueError(f'{validator_func}.__name__ failed')

        return validated_func

    return decorator


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(5))
print(calc_cube(-5))
