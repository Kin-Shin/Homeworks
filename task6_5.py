total = {}
with open("task6_5.txt", "r") as my_file:
    content = my_file.readlines()
    for el in content:
        lessons = el.split()
        time = 0
        for elem in lessons[1:]:
            if elem != "-":
                num = '0'
                for element in elem:
                    if element.isdigit():
                        num += element
                    else:
                        break
                time += int(num)
        total.update({lessons[0].strip(':'): time})
print(total)
