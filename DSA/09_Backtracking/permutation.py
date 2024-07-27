


def permutations(nums):
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
print(permutations(nums))