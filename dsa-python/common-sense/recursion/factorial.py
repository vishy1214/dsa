def print_factorial(number):
    return  1 if (number == 1)else number * print_factorial(number - 1)

print(print_factorial(9))