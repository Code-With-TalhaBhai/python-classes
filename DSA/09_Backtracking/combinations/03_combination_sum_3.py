

def combinationSum3(k: int, n: int):
    arr = list(range(1,10))
    # print(arr)
    final = []  
    combinations = []

    def find_combinations(sum,i):
        if sum == n and len(combinations) == k:
            final.append(combinations.copy())

        if sum >= n or i >= len(arr):
            return

        val = arr[i]        
        combinations.append(val)
        find_combinations(sum+val,i+1)

        combinations.pop()
        while i+1 < len(arr) and arr[i+1] == arr[i]:
            i += 1

        find_combinations(sum,i+1) 


    find_combinations(0,0)
    return final





print(combinationSum3(3,7))
