
# arr = [-8, 2, 3, -6, 10]
# k = 2

arr = [-58,-999]
k = 1
ans_arr = []
N = len(arr)

def First_NegativeInteger_In_Windows_Size_K():    

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
        

print(First_NegativeInteger_In_Windows_Size_K())
