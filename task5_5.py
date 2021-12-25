with open("task5_5.txt", "w") as my_file:
    my_file.write(input('Enter numbers '))

with open("task5_5.txt", "r") as my_file:
    numbers = my_file.read().split()
    total = 0
    for el in numbers:
        total += int(el)

print(total)
