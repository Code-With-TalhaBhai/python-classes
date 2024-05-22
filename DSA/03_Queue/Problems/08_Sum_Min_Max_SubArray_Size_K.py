from collections import deque
from collections import deque


def Sum_Min_Max_K(arr,k):
    N = len(arr)
    min_q = deque()
    max_q = deque()

    for i in range(k):

        while (len(min_q) > 0 and arr[min_q[-1]] >= arr[i]):
            min_q.pop()

        while (len(max_q) > 0 and arr[max_q[-1]] <= arr[i]):
            max_q.pop()

        min_q.append(i)
        max_q.append(i)

    print(arr[min_q[0]])
    print(arr[max_q[0]])
    print(min_q)
    print(max_q)


arr=[2, 5, -1, 7, -3, -1, -2]
# k = 3


# print(Sum_Min_Max_K(arr,2))
print(Sum_Min_Max_K(arr,3))
# print(Sum_Min_Max_K(arr,4))
# print(Sum_Min_Max_K(arr,5))
