"""
2. Реализовать класс Road (дорога).
определить защищенные атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
определить внутри класса приватную константу масса квадратного метра асфальта толщиной 1 см.
определить метод расчёта массы асфальта get_asphalt_mass(height), необходимого
для покрытия всей дороги толщиной height см;
использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см * число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""


class Road:

    MASS_PER_ONE_SQUARE_METRE = 25

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_asphalt_mass(self, height):
        return self.length * self.width * self.MASS_PER_ONE_SQUARE_METRE * height


road = Road(5000, 20)
print(road.get_asphalt_mass(10)/1000)
