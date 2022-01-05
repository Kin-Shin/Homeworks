class DivisionToZero:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def divide_by_zero(numerator, denominator):
        try:
            return (numerator / denominator)
        except:
            return ("Деление на ноль невозможно")


div = DivisionToZero(50, 25)
print(DivisionToZero.divide_by_zero(50, 0))
print(DivisionToZero.divide_by_zero(46, 0.31))
print(div.divide_by_zero(50, 0))