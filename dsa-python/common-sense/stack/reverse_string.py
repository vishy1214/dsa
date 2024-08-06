string = "vishwanath"

def reverse_string(input_string):
    reversed = []
    reversed_string = ""

    for i in range(len(input_string)):
        reversed.append(input_string[i])


    for j in range(len(reversed)):
        reversed_string += reversed.pop()

    print(f'{input_string} --> {reversed_string}')


reverse_string(string)




