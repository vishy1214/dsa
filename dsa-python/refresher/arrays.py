#array definition
arr = [1,2,3,4,5,6,8,10,23]
arr2 = '1234566'   #typically a string
arr3 = ['a','b','c']
arr4 = ['a','b','c']
arr5 = '1234566'

charArray = ['a' for j in range(1000)]
boolArray = [False] * 32786

print(arr[1])
print(arr[1])

arr4 = arr + arr3
print(arr4)

print(arr2 * 7) # 1234566123456612345661234566123456612345661234566
print(arr2 * 0) #  "" empty

if 3 in arr:
    print(True)  # true
else:
    print(False)

if arr3 == arr4:
    print(True)
else:
    print(False)  # false

if arr2 == arr5:
    print(True)  #true
else:
    print(False)




#### Multivalued Assignments
