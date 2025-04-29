

def valid_paranthesis(s):
    
    stack = []
    for char in s:
        if char == '(' or char == '{' or char == '[':
            stack.append(char)
        else:
            opening = stack.pop()
            if char == ')' and opening != '(':
                return False
            elif char == '}' and opening != '{':
                return False
            elif char == ']' and opening != '[':
                return False        
    return True


s1 = "()"
s2 = "()[]{}"
s3 = "(]"
s4 = "([])"


print(valid_paranthesis(s1))
print(valid_paranthesis(s2))
print(valid_paranthesis(s3))
print(valid_paranthesis(s4))