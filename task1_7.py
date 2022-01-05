from random import randint


class Matrix:
    def __init__(self, numbers):
        self.numbers = numbers

    def __str__(self):
        string = ''
        for el in range(len(self.numbers)):
            for elem in range(len(self.numbers[el])):
                string += f'{self.numbers[el][elem]:03} '
            string += '\n'
        return string

    def __add__(self, other):
        numbers = []
        for el in range(len(self.numbers)):
            line = []
            for elem in range(len(self.numbers[el])):
                temp = self.numbers[el][elem] + other.numbers[el][elem]
                line.append(temp)
            numbers.append(line)
        return Matrix(numbers)


matrix_1 = Matrix([[randint(0, 99) for i in range(10)] for i in range(10)])
matrix_2 = Matrix([[randint(0, 99) for i in range(10)] for i in range(10)])

print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
