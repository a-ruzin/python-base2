from lesson_11.car import Car
from towncar import TownCar
from sportcar import SportCar
from workcar import WorkCar

# print(Car.derived_car_classes)

cars = []
with open('cars.txt', 'r', encoding='utf8') as f:
    for line in f:
        cartype, name, color = line.strip().split()
        cars.append(Car.create_car(cartype, name, color))


for car in cars:
    print(f'{car.__class__.__name__}: {car}')


#
# cars = []
# with open('broken_cars.txt', 'r', encoding='utf8') as f:
#     for line in f:
#         cartype, name, color = line.strip().split()
#         cars.append(create_car(cartype, name, color))
#
