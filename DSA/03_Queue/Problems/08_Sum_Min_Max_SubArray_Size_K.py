from collections import deque
from collections import deque


def Sum_Min_Max_K(arr,k):
    N = len(arr)
    min_q = deque()
    max_q = deque()

    min_q.append(0)
    max_q.append(0)

    for i in range(1,k):
        if arr[min_q[0]] > arr[i]:
            min_q[0] = i

        if arr[max_q[0]] < arr[i]:
            max_q[0] = i


    sum = arr[min_q[0]] + arr[max_q[0]]
    # print(min_q)
    # print(max_q)
    print('min',arr[min_q[0]],' max',arr[max_q[0]])
    print('sum',sum)

    for j in range(k,N):
        if (len(min_q) > 0 and j - min_q[0] == k):
            print("entering min double")
            min_q.pop()

        print('j',j)
        print('max_q',max_q[0])
        if (len(max_q) > 0 and j - max_q[0] == k):
            print("entering max double")
            max_q.pop()

        print(max_q)
        # print('max',arr[max_q[0]])


        if len(min_q) == 0:
            print("entering min")
            min_q.append(j)

        if len(max_q) == 0:
            print("entering max")
            max_q.append(j)


        if arr[min_q[0]] > arr[j]:
            min_q.appendleft(j)

        if arr[max_q[0]] < arr[j]:
            max_q.appendleft(j)


        sum += arr[min_q[0]] + arr[max_q[0]]
        print('min',arr[min_q[0]],' max',arr[max_q[0]])
        print('sum',sum)

    return sum


arr=[2, 5, -1, 7, -3, -1, -2]
# k = 3


# print(Sum_Min_Max_K(arr,2))
print(Sum_Min_Max_K(arr,3))
# print(Sum_Min_Max_K(arr,4))
# print(Sum_Min_Max_K(arr,5))
