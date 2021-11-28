time = int(input('Введите количество секунд: '))
hours = time // 3600
minutes = time % 3600 // 60
sec = time % 60
print(f"{hours:02}:{minutes:02}:{sec:02}")
