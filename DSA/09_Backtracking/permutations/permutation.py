

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
            if arr[i] in output:
                continue
            
            output.append(arr[i])
            find_permutation(output)
            output.pop()

    find_permutation([])
    return final




def permutation3(nums):
    sol,res = [],[]

    def backtrack():
        if len(sol) == len(nums):
            res.append(sol[:])
            return 
        
        for x in nums:
            if x not in sol:
                sol.append(x)
                backtrack()
                sol.pop()

    backtrack()
    return res




# nums = [1,2,3]
nums = ['a','b','c']
arr = [1,2,3]
print(permutation1(arr))
print(permutation2(arr))
print(permutation3(nums)) # Same as permutation 2