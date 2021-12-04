random_list = input("Введите элементы списка: ")
split_list = random_list.split()
split_list[:-1:2], split_list[1::2] = split_list[1::2], split_list[:-1:2]
print(split_list)

