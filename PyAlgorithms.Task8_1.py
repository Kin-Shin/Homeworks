# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)

a, b, c = input("Введите три разных числа через пробел: ").split()
mean = 0
if a < b < c or a > b > c:
    mean = b
else:
    if b < a < c or c > a > b:
        mean = a
    else:
        mean = c
print(f'mean = {mean}')

