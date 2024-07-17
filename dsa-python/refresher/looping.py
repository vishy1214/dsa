##### different ways to Loop
arr = [1,2,3,4,5,6,8,10,23]

for value in arr:
    print(value)

for index in range(len(arr)):
    print(index)

for index, value in enumerate(arr):
    print(f'index: {index} and value: {value}')