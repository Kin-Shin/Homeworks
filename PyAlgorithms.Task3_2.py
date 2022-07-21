# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.


def reverse(num):
    while int(num) > 0:
        el = int(num) % 10
        return print(el, end=''), reverse(int(num) // 10),


a = input('Number: ')
reverse(a)
