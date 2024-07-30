clothing = ["Purple Shirt","Green Shirt"]
clothing1 = []
clothing2 = ["yellow shirt"]


def generate_labels(list):
    if(len(list) == 0):
        print("list is empty")
    labels = []

    for i in range(len(list)):
        for j in range(len(list)):
            print(f'{list[i]} Size: {j+1}')
            labels.append(f'{list[i]} Size: {j+1}')
            
    return labels


generate_labels(clothing)
generate_labels(clothing1)
generate_labels(clothing2)