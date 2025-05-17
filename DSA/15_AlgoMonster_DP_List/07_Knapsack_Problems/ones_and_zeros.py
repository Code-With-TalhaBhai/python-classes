



from collections import Counter

def findMaxForm(strs, m: int, n: int) -> int:
    memo = {}
    def findMax(i,m,n):
        if i == len(strs):
            return 0
        
        if (i,m,n) in memo:
            return memo[(i,m,n)]

        cnt = Counter(strs[i])
        rem_zeros = m - cnt['0']
        rem_ones = n - cnt['1']

        take = 0
        if rem_zeros >= 0 and rem_ones >= 0:
            take = 1 + findMax(i+1,rem_zeros,rem_ones)
        noTake = findMax(i+1,m,n)
        memo[(i,m,n)] = max(take,noTake)
        return memo[(i,m,n)]
    return findMax(0,m,n)




strs1 = ["10","0001","111001","1","0"]
m1 = 5
n1 = 3

strs2 = ["10","0","1"]
m2 = 1
n2 = 1


print(findMaxForm(strs1,m1,n1))
print(findMaxForm(strs1,m2,n2))