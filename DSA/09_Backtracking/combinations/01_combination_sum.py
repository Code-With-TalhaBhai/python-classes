import collections


def combination_sum1(candidates,target):
    sol,res = [],[]
    sum = [0]

    def backtrack(i):
        if sum[0] >= target or i == len(candidates):
            if sum[0] == target:
                res.append(sol.copy())
            return
        
        num = candidates[i]
        sum[0] += num
        sol.append(num)
        backtrack(i)

        sum[0] -= num
        sol.pop()
        backtrack(i+1)

    backtrack(0)
    return res


def combination_sum2(candidates,target):
    sol,res = [],[]

    def backtrack(i,sum):
        if sum == target:
            res.append(sol.copy())

        if sum >= target or i == len(candidates):
            return
        
        num = candidates[i]
        sol.append(num)
        backtrack(i,sum+num)
        sol.pop()
        backtrack(i+1,sum)

    backtrack(0,0)
    return res



candidates1 = [2,3,6,7]
candidates2 = [2,3,5]

print(combination_sum1(candidates1,7))
print(combination_sum1(candidates2,8))


# Optimized
print("Optimized way")
print(combination_sum2(candidates1,7))
print(combination_sum2(candidates2,8))