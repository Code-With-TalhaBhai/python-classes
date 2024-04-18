

def reverse_str(str):
    new_str = ""
    stack = []
    for ch in str:
        # new_str += ch
        stack.append(ch)

    print(stack)

    while stack:
        new_str += stack[-1]
        stack.pop()
        # new_str += stack.pop()
     
    return new_str

str = "rocky"


print(reverse_str(str))