first_array = [1,2,3,4,5]
second_array = [0,2,4,6,8]

first_array1 = []
second_array1 = []

first_array2 = [1]
second_array2 = [1,2]

first_array3 = [1]
second_array3 = []

def get_intersection(first,second):
    intersection = []
    base_dict = {}

    for i in range(len(first)):
        base_dict[first[i]] = i

    for j in range(len(second)):
        if(second[j] in base_dict):
            intersection.append(second[j])

    print(intersection)
    return intersection

get_intersection(first_array,second_array)
get_intersection(first_array1,second_array1)
get_intersection(first_array2,second_array2)
get_intersection(first_array3,second_array3)


