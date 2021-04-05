"""
5. Реализуйте базовый класс Car.
при создании класса должны быть переданы атрибуты: color (str), name (str).
реализовать в классе методы: go(speed), stop(), turn(direction), которые должны
изменять состояние машины - для хранения этих свойств вам понадобятся
дополнительные атрибуты - придумайте какие.
добавьте метод is_police() - который возвращает True/False, в зависимости от
того является ли этот автомобиль полицейским (см.дальше)
Сделайте несколько производных классов: TownCar, SportCar, WorkCar, PoliceCar;
Добавьте в базовый класс метод get_status(), который должен возвращать в виде строки
название, цвет, текущую скорость автомобиля и направление движения (в случае если автомобиль едет),
для полицейских автомобилей перед названием автомобиля должно идти слово POLICE;
Для классов TownCar и WorkCar в методе get_status() рядом со значением скорости
должна выводиться фраза "ПРЕВЫШЕНИЕ!", если скорость превышает 60 (TownCar) и 40 (WorkCar).
Создайте по одному экземпляру каждого производного класса. В цикле из 10 итераций,
для каждого автомобиля сделайте одно из случайных действий: go, stop, turn со случайными
параметрами. После каждого действия показывайте статус автомобиля.
"""
import random


class Car:
    speed_limit = None

    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.speed = 0
        self.direction = 'Север'

    def go(self, speed):
        self.speed = speed

    def stop(self):
        self.speed = 0

    def turn(self, direction):
        self.direction = direction

    def is_police(self):
        return False

    def get_status(self):
        police_text = 'POLICE ' if self.is_police() else ''

        overlimit_text = ' ПРЕВЫШЕНИЕ!' if self.speed_limit and self.speed > self.speed_limit else ''
        if self.speed > 0:
            return f'{police_text}{self.color} {self.name} двигается со скоростью {self.speed}{overlimit_text} на {self.direction}'
        else:
            return f'{police_text}{self.color} {self.name} стоит'


class TownCar(Car):
    speed_limit = 60


class SportCar(Car):
    pass


class WorkCar(Car):
    speed_limit = 40


class PoliceCar(Car):
    def is_police(self):
        return True


cars = [
    TownCar('черный', 'Линкольн'),
    SportCar('красный', 'Феррари'),
    WorkCar('синий', 'Газ'),
    PoliceCar('белая', 'Лада'),
]

for iteration in range(10):
    for car in cars:
        action = random.randint(1, 3)
        if action == 1:
            car.go(random.randint(10, 100))
        elif action == 2:
            car.turn(random.choice(['Север', 'Юг', 'Запад', 'Восток']))
        elif action == 3:
            car.stop()
        print(car.get_status())
