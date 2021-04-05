# class Parking:
#     def __init__(self):
#         self.list_cars = []
#         self.name = 'No name'
#
#     def __str__(self):
#         return ", ".join(self.list_cars)
#
#     def add(self, car):
#         self.list_cars.append(car)
#
#     def remove(self, car):
#         self.list_cars.remove(car)
#
#     def __add__(self, other):
#         # Неплохая идея:
#         parking = Parking()
#         parking.list_cars = self.list_cars + other.list_cars
#         return parking
#         # Плохая идея:
#         # self.list_cars += other.list_cars
#         # return self
#
#     def __iadd__(self, other):
#         return self.__add__(other)
#
#     def __getitem__(self, idx):
#         return self.list_cars[idx]
#
#     def __len__(self):
#         return len(self.list_cars)
#
#     def __setattr__(self, attrname, value):
#         if attrname == 'name':
#             value = str(value)
#         #     if type(value) != str:
#         #         print('фигушки')
#         #     else:
#         #         super().__setattr__(attrname, value)
#         # else:
#         #     super().__setattr__(attrname, value)
#         super().__setattr__(attrname, value)
#         # self.__dict__[attrname] = value

# a = Parking()
# a.add('Volvo')
# a.add('Bmw')
# a.add('Mercedes')
#
# b = Parking()
# b.add('Lada')
# b.add('Hyunday')
#
# print(a, len(a))
# print(b, len(b))
# print('----------')
# c = a + b
# print(a)
# print(b)
# print(c)
#
# print(len(c))
# for i in range(len(c)):
#     print(c[i])

# a = Parking()
# a.name = 3.3
# a.xxx = 'asdf'
#
# print(a.name, type(a.name))
# print(a.__dict__)

# class DataBase:
#     def __init__(self):
#         print('init A')
#         self.file = open('database.txt', 'r+', encoding='utf-8')
#
#     def get_size(self):
#         return 'Маленькая'
#
#     def __del__(self):
#         self.file.close()
#         print('del A')
#
# db = DataBase()
# print(db.get_size())
# db = 3


# class DataBase:
#     def __init__(self):
#         print('init A')
#
#     def __del__(self):
#         print('del A')
#
#     def __call__(self, *args, **kwargs):
#         print(args, kwargs)
#
# db1 = DataBase()
# db2 = DataBase()
#
# db1.xxx = db2
# db2.xxx = db1
#
# db1 = 'asdf'
# db2 = 3
#
# from time import sleep
# sleep(10)

# db = DataBase()
# db()
# db(1)
# db(3, args=234)

 # a > b   # __gt__
 # a >= b   # __gte__

# a = Parking()
# a.add('a')
# c = a
# b = Parking()
# b.add('b')
#
# print(a)
# print(b)
# print(c)
# print('---')
# a += b
#
# print(a)
# print(b)
# print(c)


# class A:
#     def method(self):
#         pass
#
#
# class B(A):
#     def method(self):
#         pass
#         A.method(self)
#
#     def m2(self):
#         print('hoho')
#
#
# class C(B, A, FFFF):
#     def method(self):
#         FFFF.method(self)
#
#
# class D(B):
#     def method(self):
#         super().method()
#
#
# class E(A):
#     def method(self):
#         A.method(self)


# # Интерфейс
# class A:
#     def __len__(self):
#         return 3
#
#
# a = A()
#
# print(len(a))
# r = range(10)
# print(type(r))

# class IterParking:
#     def __init__(self, objects):
#         self.objects = objects
#         self.index = 0
#
#     def __next__(self):
#         if self.index < len(self.objects):
#             obj = self.objects[self.index]
#             self.index += 1
#             return obj
#         raise StopIteration
#
#
# class Parking:
#     def __init__(self):
#         self._list_cars = []
#         self.name = 'No name'
#         # self._total_space = self.get_total_space()
#         self._total_space = None # self.get_total_space()
#
#     def __str__(self):
#         return ", ".join(self._list_cars)
#
#     def add(self, car):
#         self._list_cars.append(car)
#
#     def remove(self, car):
#         self._list_cars.remove(car)
#
#     # def __getitem__(self, idx):
#     #     return self.list_cars[idx]
#     #
#     # def __len__(self):
#     #     return len(self.list_cars)
#
#     def __iter__(self):
#         return IterParking(self._list_cars)
#         # return iter(self._list_cars)
#
#     @property
#     def occupied_space(self):
#         return len(self._list_cars) * 20
#
#     @property
#     def total_space(self):
#         if self._total_space is None:
#             self._total_space = self.get_total_space()
#         return self._total_space
#
#     def get_total_space(self):
#         from time import sleep
#         sleep(2)
#         return 300
#
#
# parking = Parking()
# parking.add('Volvo')
# parking.add('Bmw')
# parking.add('Lada')
#
# # for car in parking:
# #     print(car)
#
#
# print(parking.occupied_space)
# print(parking.total_space)
# print(parking.total_space)
# print(parking.total_space)
# print(parking.total_space)


# # Композиция
# class A:
#     def __init__(self, name):
#         self.name = name
#
#
# class B:
#     def __init__(self, a):
#         self.a = a
#
#
# a = A('hoho')
# b = B(a)
#
# print(b.a.name)


from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def get_size(self):
        pass

    @abstractmethod
    def get_size2(self):
        pass


class B(A):
    def get_size(self):
        return 3


class C(B):
    def get_size2(self):
        return 3


c = C()
print(c.get_size())
