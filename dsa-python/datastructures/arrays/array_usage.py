import array

myarray = array.Array(10)

myarray.insert(1234)
print(myarray.get(0))
print(myarray.delete(123))
print(myarray.search(1234))
print(myarray.search(123))
print('~~~')
myarray.traverse()
