import builtins

_abs = builtins.abs

def abs(str_or_num):
    if isinstance(str_or_num, str):
        return "".join(sorted(set(str_or_num)))
    return _abs(str_or_num)

builtins.abs = abs


print(abs("hello"))
print(abs(" world"))
print(3.123)