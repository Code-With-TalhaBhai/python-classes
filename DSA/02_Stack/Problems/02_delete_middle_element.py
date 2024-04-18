

stack = ['1','2','3','4','5']

def delete_middle_element(stack):
    length:int = int(len(stack)/2)
    mid = length
    if length%2==1:
        mid = mid + 1
    
    middle_item = stack[mid]
    stack.pop(mid)
    return stack


print(delete_middle_element(stack))

