def my_func(arg_1, arg_2, arg_3):
    return (arg_1 + arg_2 + arg_3) - min(num_list)


num_1 = int(input('Input first number '))
num_2 = int(input('Input second number '))
num_3 = int(input('Input third number '))

num_list = (num_1, num_2, num_3)

print("The sum of maximum digits:", my_func(num_1, num_2, num_3))
