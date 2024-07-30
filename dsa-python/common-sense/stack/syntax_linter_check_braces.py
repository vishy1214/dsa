import stack_implementation
def is_syntax_valid(code_str):
    stack = stack_implementation.Stack()
    #print(stack.size())
    if(len(code_str) == 0):
        return False

    for i in range(len(code_str)):
        current_char = code_str[i]
        if(current_char in {"[","{","("}):
            #print(f'push block: {current_char}')
            stack.push(current_char)
        elif(current_char in {"]","}",")"}):
            stack_head = stack.head()
            if((current_char == "]" and stack_head == "[") or
                    (current_char == "}" and stack_head == "{") or
                         (current_char == ")" and stack_head == "(")):
                    stack.pop()
                    #print(f'pop block: {current_char}')
                    continue
            else:
                print(f'not a match block: {current_char}')
                stack.clear_stack()
                return False
        else:
           # print(f'ignore block: {current_char}')
            continue #ignore all other characters

    stack.clear_stack()
    return True

print(is_syntax_valid("[]"))
print(is_syntax_valid("[}"))
print(is_syntax_valid("[()]"))
print(is_syntax_valid("[({})]"))
print(is_syntax_valid("[({(})]"))
print(is_syntax_valid("[({var x = })]"))
print(is_syntax_valid("(var x = [1, 2, 3]);"))
print(is_syntax_valid("(var x = [1, 2, 3});"))
print(is_syntax_valid("{var x = [1, 2, 3});"))
print(is_syntax_valid("{var x = [1, 2, 3)};"))
print(is_syntax_valid("(var x = [1, 2, 3]);"))
print(is_syntax_valid(""))