class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'{self.a + other.a + self.b + other.b}*i'

    def __mul__(self, other):
        return f'{(self.a * other.a - self.b * other.b) + (self.a * other.b + other.a * self.b)}*i'




d1 = ComplexNumber(5, -8)
d2 = ComplexNumber(7, 15)
print(d1 + d2)
print(d1 * d2)
