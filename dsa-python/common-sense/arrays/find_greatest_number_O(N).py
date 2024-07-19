source = [120,56,15,8,99,101,111,1]
source1 = [1,56,15,8,99,101,111,121]
source2 = []
source3 = [1]
source4 = [120,56,15,8,99,101,111,1,2,4,55,33,44,77,66,99,11,22,999,22,5,7,9,13,19]
def find_greatest_number(list):
    greatest_num = 0

    for i in range(len(list)):
        if list[i] > greatest_num:
            greatest_num = list[i]

    print(greatest_num)


find_greatest_number(source3)
find_greatest_number(source)
find_greatest_number(source1)
find_greatest_number(source4)