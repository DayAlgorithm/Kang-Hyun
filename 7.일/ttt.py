def solution(s):
    if (len(s) % 2) == 1:
        return 0
    
    num_of_string = 0
    start_index = -1
    end_index = 0
    stack = []
    
    index = 0
    while(True):
        if s[index] == '(' or s[index] == '{' or s[index] =='[':
            start_index = index
            break
        index += 1
    
    index = -1
    while(True):
        if s[index] == ')' or s[index] == '}' or s[index] ==']':
            end_index = index
            break
        index -= 1
    
    if start_index == -1:
        return 0
    if end_index == 0:
        return 0
    
    fixed = ""
    if start_index != 0:
            fixed += s[start_index:]
            fixed += s[:start_index]
    else:
        if end_index == -1:
            fixed = s
        else:
            fixed += s[end_index + 1:]
            fixed += s[:end_index +1]
        
    s = fixed
    print(s)
    
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '{' or s[i] =='[':
            stack.append(s[i])
        elif s[i] == ')':
            if len(stack) == 0:
                return 0
            if stack.pop() != '(':
                return 0
        elif s[i] == '}':
            if len(stack) == 0:
                return 0
            if stack.pop() != '{':
                return 0
        elif s[i] == ']':
            if len(stack) == 0:
                return 0
            if stack.pop() != '[':
                return 0
        if len(stack) == 0:
            num_of_string += 1
    
    return num_of_string

string = ")))(([]("
""
a = solution(string)
print(a)