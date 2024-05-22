from collections import deque


arr = [2, 3, 7, 9, 5, 1, 6, 4, 3];
k = 4
dq = deque()
ans = []

for i in range(k):
    if dq and arr[i] >= arr[dq[-1]]:
        dq.pop()

    dq.append(i)

for i in range(k,len(arr)):
    # Remove elements that are outside of current window
    while dq and i - dq[0] >= k:
        dq.popleft()

    print('dq before pop',dq)
    # Remove elements that are less than current element
    while dq and arr[i] >= arr[dq[-1]]:
        dq.pop()

    print('dq after pop',dq)
    # print(ans)
    dq.append(i)
    ans.append(arr[dq[0]])


print(ans)
