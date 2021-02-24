"""
1. Человеко-ориентированное представление интервала времени
Спросить у пользователя размер интервала (в секундах).
Вывести на экран строку в зависимости от размера интервала:

1) до минуты: <s> сек;
2) до часа: <m> мин <s> сек;
3) до суток: <h> час <m> мин <s> сек;
4) сутки или больше: <d> дн <h> час <m> мин <s> сек

Например, если пользователь введет 4567 секунд, вывести:
1 час 16 мин 7 сек

"""

duration = int(input('Введите интервал в секундах:'))

minutes, seconds = divmod(duration, 60)
hours, minutes = divmod(minutes, 60)
days, hours = divmod(hours, 24)

if days > 0:
    print(f"{days} дн {hours} час {minutes} мин {seconds} сек")
elif hours > 0:
    print(f"{hours} час {minutes} мин {seconds} сек")
elif minutes > 0:
    print(f"{minutes} мин {seconds} сек")
else:
    print(f"{seconds} сек")
