


# No duplicate permutation
def permutation_ii(arr):
    final = []

    def find_permutation(idx):
        if idx == len(arr) and arr not in final:
            final.append(arr.copy())

        for i in range(idx,len(arr)):
            if i != idx and arr[i] == arr[idx]:
                continue
            arr[i],arr[idx] = arr[idx],arr[i]
            find_permutation(idx+1)
            arr[i],arr[idx] = arr[idx],arr[i]


    find_permutation(0)
    return final 


arr = [1,1,2]
print(permutation_ii(arr))