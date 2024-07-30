first = ["a","b","c","d","e","f","g"]
second = ["b","c","z"]

def is_array_subset(first_array,second_array):
    hash_first_array = {}
    for i in range(len(first_array)):
        hash_first_array[first_array[i]] = i

    for j in range(len(second_array)):
        if(second_array[j] not in hash_first_array):
            return False

    return True

print(f'is it a subset: {is_array_subset(first,second)}')