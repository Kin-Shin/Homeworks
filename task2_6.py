class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self, mass, thick):
        return self._length * self._width * mass * thick


road = Road(5000, 20)
print(road.asphalt_mass(25, 5))
