from itertools import count, cycle


my_counter = count(int(input("Введите первое целое число ")))
for i in range(20):
    print(next(my_counter))

my_list = [1, 'test', (1, 2, 3), True, [6, 'a', False]]
my_cycle = cycle(my_list)
for i in range(22):
    print(next(my_cycle))
