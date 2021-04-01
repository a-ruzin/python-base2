"""
1. Написать функцию email_parse(<email_address>), которая при помощи регулярного
выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает
их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.

# Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru

Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в
регулярном выражении; имеет ли смысл в данном случае использовать функцию re.compile()?
"""


# user_name@domain.ru
# name342.343-asdf@depa-rtment.domain.ru


import re

re_email = re.compile('^([a-zA-Z0-9_.-]+)@((([a-zA-Z0-9-]+)\.)+[a-zA-Z]+)$')


def email_parse(email):
    match = re_email.match(email)
    if match:
        return {'username': match.group(1), 'domain': match.group(2)}
    else:
        raise ValueError('некорректный email-адрес')


print(email_parse('someone@geekbrains.ru'))
print(email_parse('someone@geekbrainsru'))
