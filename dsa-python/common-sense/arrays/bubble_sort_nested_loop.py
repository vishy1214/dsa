import time

source = [120,56,15,8,99,101,111,1]
source1 = [120]
source2 = []
source3 = [120,56,15,8,99,101,111,1,2,4,55,33,44,77,66,99,11,22,53,22,5,7,9,13,19]

def bubble_sort(list):
    start = time.perf_counter()
    unsorted_until_index = len(list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                sorted = False
                unsorted_until_index -= 1

    print(list)
    stop = time.perf_counter()
    print(f"processing time: {stop - start:0.8f} seconds when array len:{len(list)}")


print(source)
bubble_sort(source)
print(" - ")
print(source1)
bubble_sort(source1)
print(" - ")
print(source2)
bubble_sort(source2)
print(" - ")
print(source3)
bubble_sort(source3)