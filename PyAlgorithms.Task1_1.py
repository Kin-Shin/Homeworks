# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

a = 5
b = 6
print(f'операнды: {a} ({bin(a)}), {b} ({bin(b)})')
print(f'побитовое И: {a & b} ({bin(a & b)}) \nпобитовое ИЛИ: {a | b} ({bin(a | b)}) '
      f'\nпобитовое ИСКЛ.ИЛИ: {a ^ b} ({bin(a ^ b)})'
      )
print(f'побитовый сдвиг числа 5 влево: {5<<2} ({bin(5<<2)}) '
      f'\nпобитовый сдвиг числа 5 вправо: {5>>2} ({bin(5>>2)})'
      )

