profit = int(input("Введите значение выручки: "))
expense = int(input("Введите значение издержек: "))
if profit > expense:
     efficiency = profit / expense
     print(f"Прибыльное дельце! Рентабельность выручки: {efficiency:.2f}")
     staff = int(input("Введите численность сотрудников фирмы "))
     money = (profit - expense) / staff
     print(f"Прибыль на каждого сотрудника: {money:.2f}")
if profit < expense:
     print("мы терпим убытки!")
