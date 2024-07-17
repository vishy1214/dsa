# sequences?
# Strings, list and tuples are sequences in python

' Sequences are iteratable BUT bounded'

'''
TUPLE - ordered and Immutable 
'''
100, 200, 300   # Tuple with three items
(3.14,)         # Tuple with one item
()              # empty tuple

x = tuple('wow',)
print(x)    # prints ('w','o', 'w')


'''
LIST - mutable and ordered 
'''
[42, 3.14, 'hello']     # List with three items
[100]                   # list with one item
[]                      # Empty list

y = list('wow')
print(y)

'''
SET - unordered and follows hashtable
# two types: set & frozenset
set - mutable
frozenset - immutable
'''

i = {42, 3.14,'hello'}
{100}
set()
{}

'''
dictionaries - keys & values
- mutable & unordered and follows hashtable
'''
{1:2, 3:4,5:6}
{'key1':123,'key2':234,'key3':456}
z = dict(x=42, y=33, z=7)
print(z)

z1 = {**z,'k5':333}
print(z1)


'''
Unpacking Assignment
'''
a,b,c = i

print(a)
print(b)
print(c)

s = 0

while (s==0 or s<10):
    s+=1
    #print(s)
    if(s==0):
        print("awesome")
    elif(s%2 == 0 ):
        print("even")
    else:
        print("odd")


for item in i:
    print(item)




