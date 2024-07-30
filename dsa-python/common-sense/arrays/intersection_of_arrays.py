first = [3,1,4,2]
second = [5,3,7,4]

def find_intersection():
    intersection = []
    for i in range(len(first)):
        for j in range(len(second)):
            if(first[i] == second[j]):
                intersection.append(first[i])
                break

    print(intersection)

find_intersection()