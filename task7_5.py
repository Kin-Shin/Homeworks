import json

firm = {}
comp, comp_sum = 0, 0
with open("task7_5.txt", "r") as my_file:
    content = my_file.readlines()
    for el in content:
        data = el.split()
        income = int(data[2]) - int(data[3])
        firm.update({data[0]: income})
        if income > 0:
            comp += 1
            comp_sum += income

ave = comp_sum / comp
outcome = [firm, {"average_profit": ave}]

with open("task7_5(2).json", "w") as my_file:
    json.dump(outcome, my_file)
