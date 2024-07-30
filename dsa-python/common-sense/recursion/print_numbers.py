arr = [  1,2,3,[4, 5, 6],7,[8,[9, 10, 11,[12, 13, 14]]],[15, 16, 17, 18, 19,[20, 21, 22,[23, 24, 25,[26, 27, 29]], 30, 31], 32], 3]

def print_numbers(myarray):
    #todo: when to exit ?
    #todo: recursive condition
    # print & check for array and recurse if its an array
    if (isinstance(myarray,list)):
        for i in range(len(myarray)):
            print_numbers(myarray[i])
    else:
        print(myarray)

print_numbers(arr)



