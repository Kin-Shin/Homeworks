# 4. Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

let1 = input('Введите первый символ диапазона: ')
let2 = input('Введите второй символ диапазона: ')

ascii_start = 96
serial_num1 = ord(let1) - ascii_start
serial_num2 = ord(let2) - ascii_start
distance = serial_num2 - serial_num1 - 1
print(f'{let1} - порядковый номер в алфавите {serial_num1}'
      f'\n{let2} - порядковый номер в алфавите {serial_num2}'
      f'\nмежду {let1} и {let2} {distance} букв'
      )


