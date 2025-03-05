

def perfect_squares(n):
    if n <= 1:
        return n
    
    def perfect(i,curr_sum):
        curr_sq = i * i

        if curr_sq > n or curr_sum > n:
            return float("inf")
        
        if curr_sum == n:
            return 0

        return min(1+perfect(i,curr_sum+curr_sq),perfect(i+1,curr_sum))


    return perfect(1,0)


print(perfect_squares(12))
print(perfect_squares(13))
