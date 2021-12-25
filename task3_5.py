with open("task3_5.txt", "r") as my_file:
    money = int()
    count = int()
    while True:
        data = str(my_file.readline()).split()
        if len(data) == 0:
            break
        money += int(data[1])
        count += 1
        if int(data[1]) < 20000:
            print(f'{data[0]} {data[1]}')

    print(money / count)
