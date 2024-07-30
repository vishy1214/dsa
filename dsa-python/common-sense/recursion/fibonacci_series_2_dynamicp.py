hash={}
def fib(n,hash):
    print(f' {n} - {hash}')
    if(n == 0 or n == 1):
        print(f' returning {n}')
        return n

    if(n not in hash):
        hash[n] = fib(n-2,hash) + fib(n-1,hash)

    return hash[n]

print(f'fib : {fib(6,hash)}')