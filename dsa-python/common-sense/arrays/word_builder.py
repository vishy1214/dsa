array = ["a","b","c","d"]

def word_builder():
    word_combo =  []

    for i in range(len(array)):
        for j in range(len(array)):
            if(i != j):
                word_combo.append(f'{array[i]}{array[j]}')


    print(word_combo)


word_builder()
