def quicksort(list):
    pivot = list(len(list)/2);
    sorted = []
    left = []
    mid = []
    right = []

    for i in range(len(list)):
        value = list[i]
        if(value < pivot): left[i]
        if(value > pivot): right[i]
        if(value == pivot):mid[i]

    sorted[quicksort(left)]
    sorted[mid]
    sorted[quicksort(right)]

    return sorted

list = [3,5,1,6,2,9,4,7,10]
print(quicksort(list))