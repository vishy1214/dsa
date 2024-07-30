str = "the quick brown box jumps over a lazy dog"
str1 = "the quick brown box jumps over a lazy person"
str2 = ""


def find_missing_letter(inputstr):
    letters = ["a", "b", "c", "d", "e", "f",   "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",]
    missing_letters = []
    source_string_dict = {}

    for i in range(len(inputstr)):
        source_string_dict[inputstr[i]] = i

    for x in range(len(letters)):
        if(letters[x] not in source_string_dict):
            missing_letters.append(letters[x])

    return missing_letters

print(find_missing_letter(str))
print(find_missing_letter(str1))
print(find_missing_letter(str2))



