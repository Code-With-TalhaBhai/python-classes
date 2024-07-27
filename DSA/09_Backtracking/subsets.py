from typing import List 


def subsets1(nums: List[int]) -> List[List[int]]:
    ans = []
    subset = []
    
    def dfs(n):
        if n == len(nums):
            # ans.append(subset[:])
            ans.append(subset.copy())
            # return ans
            return ans

        dfs(n+1)
        subset.append(nums[n])

        dfs(n+1)
        subset.pop()
        return ans

    # dfs(0)
    # return ans
    return dfs(0)
    

def subsets2(nums:List[int]) -> List[List[int]]:
    all_subsets = []
    subset = []

    def dfs(i):
        if i == len(nums):
            all_subsets.append(subset[:])
            return
        
        subset.append(nums[i])
        dfs(i+1)

        subset.pop()
        dfs(i+1)

    dfs(0)
    return all_subsets



# nums = [0]
# nums = [1,2]
nums = [1,2,3]
print(subsets1(nums))
print(subsets2(nums))

