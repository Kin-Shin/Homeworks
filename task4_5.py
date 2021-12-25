translation = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("task4_5.txt", "r") as not_translated, open("task4_5(2).txt", 'w') as translated:
    content = not_translated.readlines()
    for el in content:
        eng = el.split()
        rus = translation.get(eng[0])
        translated.write(f'{el.replace(eng[0], rus)}')

    
