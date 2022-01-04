class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def profit(self):
        return self._income['wage'] + self._income['bonus']


employee1 = Position('Ivan', 'Petrov', 'surgeon', 167000, 22345)
employee2 = Position('Nikolay', 'Semibratov', 'rentgenologist', 195000, 12885)


print(employee1.get_full_name())
print(employee1.position)
print(employee1.wage)
print(employee1.profit())

print(employee2.get_full_name())
print(employee2.position)
print(employee2.wage)
print(employee2.profit())
