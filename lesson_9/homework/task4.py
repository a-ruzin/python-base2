"""
4. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw() (отрисовка).
Метод выводит сообщение «Запуск отрисовки»;
создать три производных класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе переопределить метод draw(). Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры каждого класса и положить их в список.
Проитерироваться по этому списку и вызвать метод draw() для каждого элемента.
"""


class Stationary:
    def draw(self):
        print('Запуск отрисовки')


class Pen:
    def draw(self):
        print('Я ручка, я ручка')


class Pencil:
    def draw(self):
        print('Я карандаш, я карандаш')


class Handle:
    def draw(self):
        print('Я маркер, я маркер')


stationaries = [Stationary(), Pen(), Pencil(), Handle()]
for stationary in stationaries:
    stationary.draw()
