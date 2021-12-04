all_goods = []
session = ''
while session != 'N':
    good = input('Наименование  ')
    price = input('Цена  ')
    quantity = input("Количество  ")
    meter = input("Ед. изм ")
    session = input('Нажмите любую клавишу, чтобы продолжить ввод товара; (N) - чтобы прекратить ')
    resume = {"Наименование": good, "Цена": price, "Количество": quantity, "Ед. изм": meter}
    all_goods.append(resume)
for num, el in enumerate(all_goods, 1):
    print(num, el)

analitics = {}

for data in all_goods:
    for key, value in data.items():
        analitics[key] = [value]
        if key != None:
            analitics[key].append(value)



print(analitics)