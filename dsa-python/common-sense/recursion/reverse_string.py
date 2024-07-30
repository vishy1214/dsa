str = "abcde"

def reverse(input_str):
    if len(input_str) == 0:
        return ""
    return input_str[len(input_str)-1] + reverse(input_str[:len(input_str)-1])

print(reverse(str))