str = "minimum"
str1 = ""
str2 = "minimumnu"

def find_non_dupe_letter(inputstr):
    dict = {}

    for i in range(len(inputstr)):
        if(inputstr[i] in dict):
            value = dict[inputstr[i]]
            dict[inputstr[i]] = value + 1
        else:
            dict[inputstr[i]] = 1

    for k,v in dict.items():
        if(v == 1):
            return k

    return None

print(find_non_dupe_letter(str))
print(find_non_dupe_letter(str1))
print(find_non_dupe_letter(str2))