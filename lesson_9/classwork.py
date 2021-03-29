# from functools import wraps
# from time import sleep as slp
#
#
# registered_functions = {}
#
#
# # def decorator(func):
# #     cache = {}
# #     @wraps(func)
# #     def new_func(*args, **kwargs):
# #         if tuple(args) not in cache:
# #             result = func(*args, **kwargs)
# #             cache[tuple(args)] = result
# #         return cache[tuple(args)]
# #
# #     return new_func
#
# def register_func(func):
#     registered_functions[func.__name__] = func
#     return func
#
#
# registered_functions[slp.__name__] = slp
#
#
# @register_func
# def sleep():
#     slp(1)
#
# print(registered_functions)
#
# #
# # @register_func
# # def sum_two_numbers(a, b):
# #     """
# #     функция складывает два числа
# #     :param a:
# #     :param b:
# #     :return:
# #     """
# #     print('Оргинальная sum_two_numbers вызвана')
# #     sleep(1)
# #     return a + b
# #
# #
# # # print(help(sum_two_numbers))
# #
# # # for x in range(10):
# # #     print(sum_two_numbers(x % 2, 3))
# #
# # print(registered_functions)

class Car:
    # color = 'black'
    # doors = 4
    # name = None
    engine = '4 cylynder'

    def __init__(self, name, color='black', doors=4):
        self.name = name
        self.color = color
        self.doors = doors
        self.speed = 0

    def __str__(self):
        return f'Car {self.color} {self.name} - {self.doors} дверей, {self.engine}'

    # def describe(self):
    #     return f'{self.color} {self.name} - {self.doors} дверей'

    def accelerate(self, delta):
        speed_limit = self.speed_limit()
        if speed_limit is None or self.speed + delta <= speed_limit:
            self.speed += delta
        else:
            self.speed = speed_limit

    def speed_limit(self):
        return None

    def decelerate(self, delta):
        self.speed -= delta
        if self.speed < 0:
            self.speed = 0


class Truck(Car):

    def __init__(self, name, color='black', doors=4, load_limit=1000):
        super().__init__(name, color, doors)
        self.load_limit = load_limit
        self.load = 0

    def __str__(self):
        return f'Truck {self.color} {self.name} is moving {self.speed} km/h - {self.doors} дверей, {self.engine}, load: {self.load} из {self.load_limit}'

    def take_load(self, weight):
        if weight <= self.load_limit:
            self.load = weight
        else:
            raise ValueError('Нагрузка слишком велика')

    def speed_limit(self):
        return 60


class Sport:
    color = 'Yellow'

    def is_sport(self):
        return True


class SportCar(Car, Sport):

    def __init__(self, name, color='black', doors=2):
        super().__init__(name, color, doors)

    def __str__(self):
        return f'Truck {self.color} {self.name} is moving {self.speed} km/h - {self.doors} дверей, {self.engine}'

    def speed_limit(self):
        return 360


# print(Car.engine)

car = SportCar('Volvo', 'red', 5)
print(car)
car.accelerate(40)
print(car)
car.accelerate(40)
print(car)

print(car.color)


# print(car)
# car.take_load(500)
# print(car)
# car.take_load(1500)
# print(car)


car2 = Car('BMW', 'black', 2)
car3 = Car('Mercedes')
car4 = Car('Mercedes', doors=5)
car4.engine = '8 cylynder'
#
# print(car, type(car))
# print(car2, type(car2))
# print(car3)
# print(car4)
#
# Car.engine = '6 cylynder'
#
# print(car)
# print(car2)
# print(car3)
# print(car4)


# print(Car.describe(car))

# ЭТО ПЛОХО!!!
# class Bat:
#     pass
#
# class Man:
#     pass
#
# class BatMan(Bat, Man):
#     pass
#

import datetime
from time import sleep


class Parking:
    def __init__(self, limit=10):
        self._cars = []
        self.limit = limit

    def park_car(self, car):
        if car in self._cars:
            raise ValueError('Эта машина уже здесь запаркована')

        if not self.is_full():
            self._cars.append(car)
        else:
            raise ValueError('Стоянка полная')

    def is_full(self):
        return len(self._cars) >= self.limit

    def list_cars(self):
        for car in self._cars:
            print(car)


parking = Parking(10)
parking.park_car(car)
parking.park_car(car2)
parking.park_car(car3)
parking.park_car(car4)

parking.list_cars()
