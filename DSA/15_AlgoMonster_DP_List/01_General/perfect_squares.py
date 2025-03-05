

def perfect_squares(n):
    if n <= 2:
        return n
    
    memo = {}

    def perfect(i,curr_sum):
        if (i,curr_sum) in memo:
            return memo[(i,curr_sum)]

        curr_sq = i * i

        if curr_sq > n or curr_sum > n:
            return float("inf")
        
        if curr_sum == n:
            return 0

        memo[(i,curr_sum)] = min(1+perfect(i,curr_sum+curr_sq),perfect(i+1,curr_sum))
        return memo[(i,curr_sum)]
    return perfect(1,0)


print(perfect_squares(12))
print(perfect_squares(13))
