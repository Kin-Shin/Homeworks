first_day = float(input("Количество км в первый день "))
aim = float(input("Цель в км "))
counter = 1
while first_day < aim:
    first_day = first_day + first_day / 10
    counter = counter + 1

print(f"Цель будет достигнута через {counter} дней")
