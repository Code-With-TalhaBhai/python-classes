
def knows(M,A,B):
    if M[A][B]:
        return True
    else:
        return False

def find_celebrity(M):
    stack = []
    no_of_rows = len(M)
    # print(no_of_rows)

    for i in range(len(M)):
        stack.append(i)

    while len(stack) > 1:
        A = stack[-1]
        stack.pop()
        B = stack[-1]
        stack.pop()

        if knows(M,A,B):
            stack.append(B)
        else:
            stack.append(A)








M = [
    [0,1,0],
    [0,0,0],
    [0,1,0]
]


find_celebrity(M)