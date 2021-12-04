var_words = input("Введите набор слов ").split()
for num, elem in enumerate(var_words, 1):
    print(num, elem[:10])
