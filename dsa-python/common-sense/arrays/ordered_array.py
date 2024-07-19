
source = [12,56,75,88,99,101,102,103]
def linear_search(array,element):

    for x in range(len(array)):
        current_val = array[x]
        if(current_val == element):
            return x
        elif(current_val > element):
            return None



print(linear_search(source,56))
print(linear_search(source,75))


