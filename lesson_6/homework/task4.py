"""
4. * (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах
превышает объём ОЗУ (разумеется, не нужно реально создавать такие большие файлы,
это просто задел на будущее проекта). Также реализовать парсинг данных из файлов
- получить отдельно фамилию, имя и отчество для пользователей и название каждого
 хобби: преобразовать в какой-нибудь контейнерный тип
 (список, кортеж, множество, словарь). Обосновать выбор типа.
 Подумать, какие могут возникнуть проблемы при парсинге.
 В словаре должны храниться данные, полученные в результате парсинга.
"""

with open('users.csv', 'r', encoding='utf-8') as users_f, open('hobby.csv', 'r', encoding='utf-8') as hobby_f:
    while True:
        user = users_f.readline()
        hobby = hobby_f.readline()
        if user:
            user_name = ' '.join(user.strip().split(','))
            hobbies = hobby.strip().split(',') if hobby else None
            print(user_name, hobbies)  # сложная обработка
        elif hobby:
            exit(1)
        else:
            break