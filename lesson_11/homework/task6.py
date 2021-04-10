"""
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных
на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум
возможностей, изученных на уроках по ООП.
"""


class StoreError(Exception):
    pass


class Store:
    STORE_NAME = 'store'

    def __init__(self):
        self.store = {}

    def __str__(self):
        result = []
        if self.store:
            for department, entities in self.store.items():
                result.append(f'{department}: {len(entities)}')
                for entity, quantity in entities.items():
                    result.append(f'    {entity}: {quantity}')
        else:
            result.append('Склад пустой')
        result.append('--------')
        return "\n".join(result)

    def get(self, department, entity):
        return self.store.get(department, {}).get(entity, 0)

    def set(self, department, entity, quantity):
        if quantity > 0:
            self.store.setdefault(department, {})
            self.store[department].setdefault(entity, 0)
            self.store[department][entity] = quantity
        elif quantity == 0:
            if department in self.store:
                if entity in self.store[department]:
                    del self.store[department][entity]
        else:
            raise StoreError('Количество техники должно быть больше нуля')

    def change(self, department, entity, quantity):
        current_quantity = self.get(department, entity)
        self.set(department, entity, current_quantity + quantity)

    def add(self, entity, quantity):
        self.change(self.STORE_NAME, entity, quantity)

    def move_to_department(self, department, entity, quantity):
        self.change(self.STORE_NAME, entity, -quantity)
        self.change(department, entity, quantity)

    def return_to_store(self, department, entity, quantity):
        self.change(department, entity, -quantity)
        self.change(self.STORE_NAME, entity, quantity)


class Entity:
    def __init__(self, model_name, price):
        self.model_name = model_name
        self.price = price

    def __str__(self):
        return f'{self.__class__.__name__} {self.model_name}'

    def __repr__(self):
        return self.model_name


class Printer(Entity):
    def __init__(self, model_name, price, print_size):
        super().__init__(model_name, price)
        self.print_size = print_size


class Scanner(Entity):
    def __init__(self, model_name, price, is_color):
        super().__init__(model_name, price)
        self.is_color = is_color


class Copier(Entity):
    def __init__(self, model_name, price, is_multipage):
        super().__init__(model_name, price)
        self.is_multipage = is_multipage


store = Store()
print(store)

copier = Copier('Xerox 3320', 20000, True)
printer = Printer('Epson FW650', 5000, 'A4')

store.add(copier, 5)
store.add(printer, 15)
print(store)

store.move_to_department('Продажи', copier, 3)
store.move_to_department('Продажи', printer, 7)
print(store)

store.move_to_department('Бухгалтерия', copier, 1)
store.move_to_department('Продажи', printer, 3)
print(store)

try:
    store.return_to_store('Продажи', copier, 10)
    print(store)
except:
    print('10 штук не удалось')

store.return_to_store('Продажи', copier, 1)
print(store)
