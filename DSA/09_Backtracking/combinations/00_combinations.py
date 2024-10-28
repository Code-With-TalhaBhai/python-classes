


def combinations(n,k):
    res,sol = [],[]

    def backtrack(x):
        if len(sol) == k:
            # res.append(sol[:])
            res.append(sol.copy())
            return
        
        for i in range(x,n+1):
            sol.append(i)
            backtrack(i+1)
            sol.pop()

    backtrack(1)
    return res


n = 5
k = 2
print(combinations(n,k))