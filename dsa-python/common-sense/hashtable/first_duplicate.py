array =  ["a", "b", "c", "d", "c", "e", "f"]
array1 =  ["a", "b", "c", "d", "e", "f"]
array2 =  []

def find_first_dupe(list):
    dict = {}
    
    for i in range(len(list)):
        if(list[i] not in dict):
            dict[list[i]] = i
        else:
            return list[i]

    return None

print(find_first_dupe(array))
print(find_first_dupe(array1))
print(find_first_dupe(array2))
