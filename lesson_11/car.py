class Car:

    derived_car_classes = {}

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f'{self.name} {self.color}'

    @classmethod
    def register_car_class(cls, klass):
        cls.derived_car_classes[klass.__name__] = klass
        return klass

    @classmethod
    def create_car(cls, cartype, name, color):
        try:
            return cls.derived_car_classes[cartype](name, color)
        except KeyError:
            raise ValueError(f'Неизвестный тип машины {cartype}')

    @staticmethod
    def calc_time(speed, distance):
        return distance / speed


def register_car(klass):
    Car.derived_car_classes[klass.__name__] = klass
    print(Car.derived_car_classes, id(Car.derived_car_classes))
    # return klass
