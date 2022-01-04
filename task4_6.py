class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("The car is on the move")

    def stop(self):
        print("The car is stopped")

    def turn(self, direction):
        print(f'The car turned to {direction}')

    def show_speed(self):
        print(f'Speed of the car {self.speed} km/h')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Town car speed exceeded!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Work car speed exceeded!')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


police = PoliceCar(140, 'white-blue', 'NYPD')
town = TownCar(80, 'black', 'Toyota')
sport = SportCar(200, 'yellow', 'Lamborghini')
work = WorkCar(40, 'white', "Kamaz")

print(town.name)
town.show_speed()
# town.speed = 59

print(police.name, '\n', police.color)
police.show_speed()
police.turn('Right')


print(sport.name, '\n', sport.color)
sport.show_speed()

print(work.name)
work.show_speed()
work.turn('Left')
