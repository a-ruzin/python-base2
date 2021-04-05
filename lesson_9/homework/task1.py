"""
1. Создать класс TrafficLight (светофор).
определить у него один приватный атрибут color (цвет) и
метод get_current_signal() (получить текущий цвет);
после создания экземпляра светофора, он запускает режим смены сигналов
с разной длительностью: красный (3 сек), жёлтый (1 сек), зелёный (3 сек);
переключение идет циклично в порядке красный-жетлый-зеленый-красный-жетлый-зеленый-красный-...
проверить переключение режимов работы светофора, опрашивая в цикле текущее
состояние светофора с интервалом 0.5 секунды, используя метод get_current_signal().
"""
from datetime import datetime
from time import sleep


class TrafficLight:
    __color = None
    __order = [
        (3, 'red'),
        (1, 'yellow'),
        (3, 'green'),
    ]

    def __init__(self):
        self.__color = 'red'
        self.start_time = datetime.now()
        self.cycle_total_seconds = sum(x[0] for x in self.__order)

    def get_current_signal(self):
        diff = (datetime.now() - self.start_time).total_seconds()
        shift = diff % self.cycle_total_seconds
        index = 0
        while shift > self.__order[index][0]:
            shift -= self.__order[index][0]
            index += 1

        self.__color = self.__order[index][1]
        return self.__color


light = TrafficLight()
for i in range(30):
    current_time = datetime.now()
    print(current_time, light.get_current_signal())
    sleep(0.5)
