array = [1,2,3,4]

def max(list):
    print(list)
    if(len(list) == 1):
        return list[0]

    maximum_val = max(list[1:len(list)])

    if(list[0] > maximum_val):
        return list[0]
    else:
        return maximum_val


print(f'Max number: {max(array)}')

