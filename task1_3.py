def degree(arg_1, arg_2):
    return arg_1 // arg_2


num = int(input('Enter numerator '))
den = int(input('Enter denominator '))
if den == 0:
    print("unsupported operation")
else:
    print(degree(num, den))
