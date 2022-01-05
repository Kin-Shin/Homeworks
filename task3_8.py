class Exclusion:
    def __init__(self, my_list):
        self.my_list = []

    def data(self):
        while True:
            try:
                my_data = int(input('Введите данные '))
                self.my_list.append(my_data)
                print(f'Принятые данные - {self.my_list} \n ')
            except:
                print(f"Неверные данные")
                check = input(f'Ввести новые данные? Y/N ')

                if check == 'Y' or check == 'y':
                    print(err.data())
                else:
                    print(f'Сбор данных окончен. \n Принятые данные - {self.my_list}')
                    break

err = Exclusion(1)
print(err.data())
