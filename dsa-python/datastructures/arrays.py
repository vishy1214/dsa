import math
import time

arr = ["apples", "banana", "pear", "---nothing---"]

print(arr)

print("~~~~~~~~~~~~~~~")

for i in arr:
    print(i)

print("~~~~~~~~~~~~~~~")

arrNum = [3, 17, 75, 80, 202]



def divisible_by_5():
    for i in range(1,100):
        if(i % 5 == 0):
          print(i , "Divisible by 5")

## Linear Search ##
def search_array(sourceArr, searchItem):
    start =  time.perf_counter()
    return_val = None
    for idx in range(len(sourceArr)):
        currItem = sourceArr[idx]
        if(currItem == searchItem):
            return_val = idx
            break
        elif(currItem > searchItem):
            break
    stop = (time.perf_counter())
    print(stop - start)
   # print("{:.2f}".format(math.ceil(stop - start)), " Seconds")
    return return_val


def binary_search(arr, searchItem):
    start = time.perf_counter()
    lower_bound = 0
    upper_bound = len(arr) -1
    return_midpoint = 0
    while(lower_bound <= upper_bound ):
        midpoint = math.ceil((lower_bound + upper_bound) / 2)
        #print(lower_bound, " ", midpoint, " ", upper_bound)
        value_at_midpoint = arr[midpoint]
        #print("value_at_midpoint: ", value_at_midpoint)
        if(value_at_midpoint == searchItem):
            return_midpoint = midpoint
            break
        elif(searchItem > value_at_midpoint):
            lower_bound = midpoint + 1
        elif(searchItem < value_at_midpoint):
            upper_bound = midpoint - 1
    stop = time.perf_counter()
    print(stop - start)
    return return_midpoint
    #print(lower_bound, " ", midpoint, " ", upper_bound, " exited")

if __name__ == '__main__':
    arr = [3, 17, 75, 80, 202,210,234,250,275,290,310,323,342, 374,399,400,401, 403, 404, 407, 410,412, 413]  # ordered array
    searchItem = 202

    print(search_array(arr,searchItem))
    print("________________")
    print("________________")
    print(binary_search(arr,searchItem))





