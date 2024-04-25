
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

    # print(stack[-1],"is celebrity")

    # verify celebrity
    candidate = stack[-1]
    no_of_zeros = 0


    for items in M[candidate]:
        if items == 0:
            no_of_zeros = no_of_zeros + 1

    if no_of_zeros != len(M):
        print("it is happening")
        return -1
    

    # Ones count
    no_of_ones = 0
    for items in M:
        if(items[candidate])==1:
            no_of_ones = no_of_ones + 1

    if no_of_ones != len(M)-1:
        return -1
    
    return candidate



M = [
    [0,1,0],
    [0,0,0],
    [0,1,0]
]

O = [
        [0,1],
        [1,0]
    ];


print("Celebrity is: ",find_celebrity(M))
print("Celebrity is: ",find_celebrity(O))
