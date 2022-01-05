class Cell:
    def __init__(self, amount):
        self.amount = int(amount)

    def __add__(self, other):
        return f'Размер клетки равен: {self.amount + other.amount}'

    def __sub__(self, other):
        sub = self.amount - other.amount
        return f'Размер клетки равен: {sub}' if sub > 0 else 'Ошибка вычитания'

    def __truediv__(self, other):
        return self.amount // other.amount

    def __mul__(self, other):
        return self.amount * other.amount

    def make_order(self, row):
        result = ''
        for el in range(int(self.amount / row)):
            result += '*' * row + '\n'
        result += '*' * (self.amount % row) + '\n'
        return result


cell = Cell(38)
cell_2 = Cell(13)
print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
print(cell.make_order(5))
