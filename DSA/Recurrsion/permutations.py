

def permutation1(arr):
    final = []
    # output = []

    def find_permutation(idx):
        if idx >= len(arr):
            final.append(arr.copy())

        for i in range(idx,len(arr)):
            arr[i],arr[idx] = arr[idx],arr[i]
            find_permutation(idx+1)
            arr[i],arr[idx] = arr[idx],arr[i]

    find_permutation(0)
    return final


def permutation2(arr):
    final = []
    
    def find_permutation(output):
        if len(output) >= len(arr):
            final.append(output.copy())

        for i in range(len(arr)):
            # 1st way
            # if arr[i] not in output:
            #     output.append(arr[i])
            
            #     find_permutation(output)
            #     output.pop()

            if arr[i] in output:
                continue
            
            output.append(arr[i])
            find_permutation(output)
            output.pop()

    find_permutation([])
    return final





arr = [1,2,3]
print(permutation1(arr))
print(permutation2(arr))
