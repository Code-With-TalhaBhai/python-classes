from collections import deque


# with list
def first_non_repeating1(stream):
    obj = {}
    final_str = ""
    q = []
    
    for char in stream:
        if char in obj:
            if bool(q) and obj[char] > 0:
                q.remove(char)
            obj[char] = obj[char]-1
        else:
            obj[char] = 1
            q.append(char)

        if not bool(q):
            final_str += "#"
        else:
            final_str += q[0]

    return final_str

# with queue
def first_non_repeating2(stream):
    obj = {}
    final_str = ""
    q = []
    
    for char in stream:
        if char in obj:
            # if bool(q) and char == q[0]:
            if bool(q):
                # q.pop(0)
                q.remove(char)
            # obj[char] = obj[char] + 1
        else:
            # obj[char] = 0
            obj[char] = True
            q.append(char)

        if not bool(q):
            final_str += "#"
        else:
            final_str += q[0]

    # print(q)
    return final_str









input1 = "aabc"
input2 = "zz"
input3 = "tcpmxaixsswjelbswxytyhbwjinuhxhvpwaybmdhndafszoghpyzdahiqsgluufqcekjk"
input4 = "geeksforgeeksandgeeksquizfor"


print(first_non_repeating1(input1))
print(first_non_repeating1(input2))
print(first_non_repeating1(input3))
print(first_non_repeating1(input4))