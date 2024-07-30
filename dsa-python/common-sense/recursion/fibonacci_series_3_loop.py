
def fib(n):
    a = 0
    b = 1
    sum = 0

    for x in range(n-1):
       sum = a + b
       a = b
       b = sum

    print(sum)

fib(19)