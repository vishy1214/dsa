import math
f = 1
"""while f != 0:
    print(f)
    f -= 0.2"""

print(f'f: {f}')  # 1

f1 = f - 0.2 # 0.8
print(f'f1: {f1}')
f2 = f1 - 0.2 # 0.6000000000000001
print(f'f2: {f2}')
print(f'f1: {f1}')

print(f'math.ceil(f1): {math.ceil(f1)}') # prints 1 instead of 0.8
print(f'math.floor(f1): {math.floor(f1)}') # prints 0 instead of 0.8
print(f'math.fabs(f1): {math.fabs(f1)}')
print(f'abs(f1): {abs(f1)}')

f10 = 10
print(f' 1/10: {1/10}')
print(f' f/f10: {(float(f)/float(f10))}')



