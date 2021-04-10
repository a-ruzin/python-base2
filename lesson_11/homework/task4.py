"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий
склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
"""


class Store:
    def __init__(self):
        self.store = []


class Entity:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Printer(Entity):
    def __init__(self, name, price, print_size):
        super().__init__(name, price)
        self.print_size = print_size


class Scanner(Entity):
    def __init__(self, name, price, is_color):
        super().__init__(name, price)
        self.is_color = is_color


class Copier(Entity):
    def __init__(self, name, price, is_multipage):
        super().__init__(name, price)
        self.is_multipage = is_multipage
