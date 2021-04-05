# from lesson_11.car import Car
# from towncar import TownCar
# from sportcar import SportCar
# from workcar import WorkCar
#
# # print(Car.derived_car_classes)
#
# cars = []
# with open('cars.txt', 'r', encoding='utf8') as f:
#     for line in f:
#         cartype, name, color = line.strip().split()
#         cars.append(Car.create_car(cartype, name, color))
#
#
# for car in cars:
#     print(f'{car.__class__.__name__}: {car}')
#
#
# #
# # cars = []
# # with open('broken_cars.txt', 'r', encoding='utf8') as f:
# #     for line in f:
# #         cartype, name, color = line.strip().split()
# #         cars.append(create_car(cartype, name, color))
# #


# class CarError(Exception):
#     pass
#
#
# class SpeedLimitError(CarError):
#     pass
#
#
# class BrokeError(CarError):
#     pass
#
#
#
# try:
#     pass
# except BrokeError:
#     pass
# except CarError:
#     pass
# except ValueError:
#     pass



# None
# True
# False
#
# from
# import
#
# if
# elif
# else
# and
# not
# or
# in
# is
#
# for
# while
#
# break
# continue
#
# class
#
# def
# return
# yield
# global
# nonlocal
# lambda
#
# del
#
# try
# except
# else
# finally
# as
# raise
#
# pass
# with
#
# async
# await
# assert

# def do_something(car):
#     return Car(car.name)
#
#
# class Car:
#     def __init__(self, name):
#         self.name = name
#
#
# a = Car('a')
# b = do_something(a)
#
# print(a is b)
#
# print(a is None)
#
# a = 0
#
# if a is None:
#     print('a is None')


#
# print(a is b, id(a), id(b))
#
# a = 'aaabbb'
# b = 'aaa'
# b += 'bbb'
# c = 'aaabbb'
# print(a, c, a == c, a is c)

# a = 1
# def f():
#     b = 3
#     def g():
#         global a
#         nonlocal b
#         c = 14
#         print(a, b, c)
#         a = 4
#         b = 15
#         print(a, b, c)
#
#     g()
#     print(b)
#
# f()
# print(a)
