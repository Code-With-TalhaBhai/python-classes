from collections import deque


def first_non_repeating(stream):
    q = deque()
    obj = {}
    final_str = ""

    for char in stream:
        if char in obj:
            while bool(q) and q[0] in obj:
                q.popleft()
        else:
            obj[char] = True
            q.append(char)
        if not bool(q):
            final_str += "#"
        else:
            final_str += q[0]
    return final_str
            


input1 = "aabc"
input2 = "zz"
input3 = "tcpmxaixsswjelbswxytyhbwjinuhxhvpwaybmdhndafszoghpyzdahiqsgluufqcekjk"
input4 = "geeksforgeeksandgeeksquizfor"


print(first_non_repeating(input1))
print(first_non_repeating(input2))
print(first_non_repeating(input3))
print(first_non_repeating(input4))