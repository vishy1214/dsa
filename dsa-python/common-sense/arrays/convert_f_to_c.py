temps_in_f = []
temps_in_f1 = [2]
temps_in_f2 = [45,65,72,32,0,98,78]
temps_in_f3 = [0]

def get_average_celsius_reading(temps):
    sumof = 0
    if(len(temps) == 0):
        print("list is empty")
        return

    for i in range(len(temps)):
        tempinC = (temps[i] - 32) * (5/9)
        sumof += tempinC

    print(f'average: {sumof / len(temps):0.4f}')

get_average_celsius_reading(temps_in_f)
get_average_celsius_reading(temps_in_f1)
get_average_celsius_reading(temps_in_f2)
get_average_celsius_reading(temps_in_f3)
