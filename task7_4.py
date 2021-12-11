def fact(n):
    val_fact = 1
    for i in range(1, n + 1):
        val_fact *= i
        yield val_fact


n = int(input("Факториал "))

for el in fact(n):
    print(el)
