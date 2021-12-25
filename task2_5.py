with open("task2_5.txt", "r") as my_file:
    lines = str(my_file).split("\n")
    total_lines = 0
    for num, sentence in enumerate(my_file, 1):
        print(f'{num}, {sentence} (number of words - {(len(str(sentence).split()))})')
        total_lines += 1
    print(f"Total lines {total_lines}")
