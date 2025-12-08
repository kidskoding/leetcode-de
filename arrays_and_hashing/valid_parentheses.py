def valid_parentheses(str):
    stack = []
    parentheses_pair = {')': '(', ']': '[', '}': '{'}
    
    for x in str:
        if x in parentheses_pair:
            if stack and parentheses_pair[x] == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            stack.append(x)
                    
    return len(stack) == 0