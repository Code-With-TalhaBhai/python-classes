
from collections import deque


arr = [-8, 2, 3, -6, 10]
k = 2

# arr = [-58,-999]
# k = 1

# sliding window technique
def First_NegativeInteger_In_Windows_Size_K1(arr,k):
    dq = deque()
    ans_arr = []
    N = len(arr)

    for i in range(k):
        if (arr[i]<0):
            dq.append(i)

    if len(dq)>0:
        ans_arr.append(arr[dq[0]])
    else:
        ans_arr.append(0)


    for j in range(k,N):
        if (len(dq)>0 and (j - dq[0]) == k):
            dq.popleft()

        if(arr[j]<0):
            dq.append(j)

        if len(dq) > 0:
            ans_arr.append(arr[dq[0]])
        else:
            ans_arr.append(0)
    
    return ans_arr


 # brute force
def First_NegativeInteger_In_Windows_Size_K2(arr,k):    
    ans_arr = []
    N = len(arr)
    i = 0
    while(i<N):
        z = i + k
        if z <= N:
            j = i
            while(j<z):
                if arr[j] < 0:
                    # print('working')
                    ans_arr.append(arr[j])
                    break;
                j += 1

            if j == i+k:
                ans_arr.append(0)
            i += 1
            # print(ans_arr)
        else:
            return ans_arr
    return ans_arr
        

print(First_NegativeInteger_In_Windows_Size_K1(arr,k)) # sliding window technique
print(First_NegativeInteger_In_Windows_Size_K2(arr,k)) # brute force
