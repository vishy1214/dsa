def bubble_up(arr):
    sorted =False
    unsorted_until_index = len(arr) - 1

    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            if(arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = False
        unsorted_until_index -=1

    return arr 


if __name__ == '__main__':
    arr = [4,2,7,1,3]
    print(bubble_up(arr))