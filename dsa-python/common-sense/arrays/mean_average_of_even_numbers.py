array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def mean_average_even_numbers():
    sum = 0
    even_counter = 0

    for i in range(len(array)):
        if(array[i] % 2 == 0):
            sum += array[i]
            even_counter += 1

    print(f' sum: {sum} - even_counter:{even_counter} -- average : {sum/even_counter}')

mean_average_even_numbers()