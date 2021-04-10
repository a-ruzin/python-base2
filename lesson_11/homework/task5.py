"""
5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают
за приём оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также
других данных, можно использовать любую подходящую структуру (например, словарь).
"""

class StoreError(Exception):
    pass


class Store:
    def __init__(self):
        self.store = {}

    def add(self, entity, department):
        self.store.setdefault(department, [])
        self.store[department].append(entity)

    def remove(self, entity, department):
        try:
            self.store[department].remove(entity)
        except:
            raise StoreError(f'На складе в департаменте {department} нет техники {entity}')

    def move(self, entity, department_from, department_to):
        self.remove(entity, department_from)
        self.add(entity, department_to)


class Entity:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


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


store = Store()
copier = Copier('Xerox', 20000, True)
store.add(copier, 'Бухгалтерия')
print(store.store)
store.move(copier, 'Бухгалтерия', 'Продажи')
print(store.store)
