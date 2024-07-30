str1 = "racecar"
str2 = "kayak"
str3 = "deified"
str4 = ""
str5 = "a"
str6 = "aa"
str7 = "ab"
str8 = "abc"
str9 = "aaa"
str10 = "aaba"
str11 = "deifie"


def palindrome_checker(str):
    counter = 0
    reverse_counter = len(str)-1
    is_palindrome = True
    mid_point = len(str) // 2
    #print(f'counter: {counter} - reverse_counter: {reverse_counter} - midpoint: {mid_point}')
    while(counter < mid_point):
        if(str[counter] != str[reverse_counter]):
            is_palindrome = False
            break
        counter += 1
        reverse_counter -= 1

    print(f'{str} -- is it Palindrome: {is_palindrome}')
    return is_palindrome


palindrome_checker(str1)
palindrome_checker(str2)
palindrome_checker(str3)
palindrome_checker(str4)
palindrome_checker(str5)
palindrome_checker(str6)
palindrome_checker(str7)
palindrome_checker(str8)
palindrome_checker(str9)
palindrome_checker(str10)
palindrome_checker(str11)
