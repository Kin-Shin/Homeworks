with open("task1_5.txt", "w") as my_file:
    while True:
        data = input("Enter your data ")
        if len(data) == 0:
            break
        data = data + "\n"
        my_file.writelines(data)



