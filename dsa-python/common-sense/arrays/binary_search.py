import math

source = [12,56,75,88,99,101,102,103]
def perform_binary_search(source,element):
    lower_bound = 0
    upper_bound = len(source)-1

    while lower_bound <= upper_bound:
        mid_point = int((lower_bound + upper_bound)//2)
        mid_point_element = source[mid_point]

        if(element == mid_point_element):
            return mid_point
        elif(element < mid_point_element):
            upper_bound = mid_point - 1
        elif(element > mid_point_element):
            lower_bound = mid_point + 1

    return None


print(perform_binary_search(source,75))
print(perform_binary_search(source,72))