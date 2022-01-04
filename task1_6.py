from time import sleep


class TrafficLight:
    # атрибут класса
    colors = ("green", "yellow", "red")
    time = (7, 2, 7)

    # конструктор
    def __init__(self):
        self.__color = 'red'

    # метод
    def running(self):
        while True:
            for col in self.colors:
                self.__color = col
                print(self.__color)
                sleep(self.time[self.colors.index(self.__color)])


traffic_light = TrafficLight()
traffic_light.running()
