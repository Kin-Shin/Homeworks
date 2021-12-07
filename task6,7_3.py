def int_func(words):
    words = words[0].upper() + words[1:].lower()
    return words


my_word = input("Enter a word ")
print(int_func(my_word))

my_string = input('Enter a string ')
for every_word in my_string.split():
    print(int_func(every_word), end=" ")
