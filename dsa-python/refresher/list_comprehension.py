'''
Applying a calculation or function
 on each element of a list to produce a new list
 is such a useful concept that Python has a special syntax for it.
 The concept is called a list comprehension
'''

#approach 1 - usual way
values = [1,2,50,12,20]
squares = []
for v in values:
    squares.append(v * v)

print(squares)

#approach 2 -- list comprehension
squares2 = [ v * v for v in values] # returns a sequence
print(squares2)

cubes = [ x ** 3 for x in values]
print(cubes)

wordarray = ['ape','ape-man','hand-me-down']
new_wordarray = [ w.split("-") for w in wordarray]
print(new_wordarray) # [['ape'], ['ape', 'man'], ['hand', 'me', 'down']]

#with filters
cubing_multiples_of_3 = [x ** 3 for x in values if x % 3 ==0 ]
print(cubing_multiples_of_3)
print(12*12*12)
print(cubing_multiples_of_3[0] == 12*12*12)