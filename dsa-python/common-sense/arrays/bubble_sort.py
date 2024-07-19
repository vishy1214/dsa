import time

source = [120,56,15,8,99,101,111,1]
source1 = [120]
source2 = []
source3 = [120,56,15,8,99,101,111,1,2,4,55,33,44,77,66,99,11,22,53,22,5,7,9,13,19]

def perform_bubble_sort(list):
    start = time.perf_counter()
    leftp = 0
    rightp = leftp + 1
    swapped = False
    debug_print(f"array len:{len(list)}")
    if(len(list) == 0):
        always_print("source is empty")
        return
    elif(len(list) == 1):
        always_print("array has just one element. nothing to sort")
        return


    while(leftp <= rightp ):
        leftval = list[leftp]
        rightpval = list[rightp]
        local_swap = False # just for printing
        if(list[leftp] > list[rightp]):
            #swap
            list[rightp] = list[leftp]
            list[leftp] = rightpval
            swapped = True
            local_swap = swapped

        leftp += 1
        rightp += 1
        debug_print(f"leftp : {leftp} - rightp: {rightp} - swapped: {local_swap}  - comparision : {leftval} >  {rightpval}")
        if(rightp == len(list) and swapped == True):
            leftp = 0
            rightp = leftp + 1
            swapped = False
            debug_print(f"RESET : leftp : {leftp} - rightp: {rightp}")
        elif(rightp == len(list) and swapped == False):
            debug_print("exit loop")
            break
    always_print(f"sorted: { list}")
    stop = time.perf_counter()
    always_print(f"processing time: {stop - start:0.4f} seconds when array len:{len(list)}")


def always_print(message):
    print(message)

def debug_print(message):
    val = 0
    #print(message)

print(source)
perform_bubble_sort(source)
print(" - ")
print(source1)
perform_bubble_sort(source1)
print(" - ")
print(source2)
perform_bubble_sort(source2)
print(" - ")
print(source3)
perform_bubble_sort(source3)
