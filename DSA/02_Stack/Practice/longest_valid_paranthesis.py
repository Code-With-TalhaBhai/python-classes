


def longest_valid_paranthesis(s):
    stack = []
    cnt = 0
    
    for char in s:
        if char == "(" or char == '{' or char == '[':
            stack.append(char)
        else:
            if not stack:
                continue
            opening = stack.pop()
            if char == ')' and opening == '(':
                cnt += 2
            elif char == '}' and opening == '{':
                cnt += 2
            elif char == ']' and opening == '[':
                cnt += 2      
    return cnt





s1 = '(()'
s2 = ')()())'
s3 = ''


print(longest_valid_paranthesis(s1))
print(longest_valid_paranthesis(s2))
print(longest_valid_paranthesis(s3))