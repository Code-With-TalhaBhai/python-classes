from collections import deque


def first_non_repeating(input):
    output_str = ""
    q = deque()

    for index,char in enumerate(input):

        if bool(q) is True:
            if q[0] == char:
                output_str += "#"
                q.pop()
            else:
                output_str += q[0]

        else:
            output_str += char
            q.append(char)

    return output_str
           






input1 = "aabc"
input2 = "zz"

print(first_non_repeating(input1))
print(first_non_repeating(input2))