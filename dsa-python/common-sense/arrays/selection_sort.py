# selection sort finds the lowest value and moves it to the front of the array. the swap is just one per
# iteration whereas the bubble sort for almost every comparision the swap happens, so in one iterations
# there's N-1 swaps as worst case. here in selection sort, the worst case is just 1
import time

source = [120,56,15,8,99,101,111,1]
source3 = [120,120,120,56,15,8,99,101,111,1,2,4,55,33,44,77,66,99,11,22,53,22,5,7,9,13,19]

def perform_selection_sort(list):
    start = time.perf_counter()
    lowest_val_idx = 0
    print(f'source list : {list}')

    for i in range(len(list)):
        lowest_val = list[i]
        lowest_val_idx = i
        for j in range(i+1,len(list)):
            #print(f'idx: i: {i} - j: {j} --condition: {list[j]} < {list[i]} ')
            if(list[j] < lowest_val):
                lowest_val_idx = j
                lowest_val = list[lowest_val_idx]
                #print(f' i: {i} - j: {j} - lowest_val_idx: {lowest_val_idx} - lowest_val:{lowest_val} - comparision: {list[j]} < {list[i]}')

        #print(f' i: {i} - j: {j} - lowest_val_idx: {lowest_val_idx}')
        if(lowest_val_idx != i):
            #swap
            i_val = list[i]
            list[i] = list[lowest_val_idx]
            list[lowest_val_idx] = i_val
            #print(f'lowest val swap - {i_val} with {lowest_val} --- updated list:  {list}')

    print(f"sorted list : {list}")
    stop = time.perf_counter()
    print(f'processing time : {stop - start:0.6f} seconds')

perform_selection_sort(source3)




