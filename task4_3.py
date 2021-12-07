def my_func(x, y):
    return x ** y


def my_func_2(x, y):
    y = abs(y)
    while y > 0:
        z = x * x
        y = y - 1
    return 1 / z


num_1 = int(input("Введите действительное положительное число "))
num_2 = int(input("Введите целое отрицательное число "))

print(my_func(num_1, num_2))
print(my_func_2(num_1, num_2))
