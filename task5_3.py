def sum_func(seq):
    numbers = seq.split()
    result = 0
    for i in numbers:
        if i == "C":
            break
        result += int(i)
    return result


buffer = 0
cancel = False

while not cancel:
    my_numbers = (input('Введите числовую последовательность '))
    cancel = "C" in my_numbers
    buffer += sum_func(my_numbers)
    print(buffer)

