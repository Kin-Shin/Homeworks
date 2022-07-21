# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

let = input('Введите любую букву: ')

ascii_start = 96
serial_num = ord(let) - ascii_start

print(f'{let} - порядковый номер в алфавите {serial_num}')

