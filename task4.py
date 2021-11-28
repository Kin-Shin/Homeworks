number = int(input('Введите целое число '))
compare = number % 10
while number > 0:
    if compare < number % 10:
        compare = number % 10
    number = number // 10
print(compare)
