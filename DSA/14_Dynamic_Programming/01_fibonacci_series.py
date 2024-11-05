
# 1. Without DP -> Recurrsive Backtracking
def fibonacci_series1(n):
    if n == 0 or n == 1:
        return n

    return fibonacci_series1(n-1) + fibonacci_series1(n-2)


# 2. Top-Down Approach(memoization)
# Time-Complexity(O(n))
# Space-Complexity(O(2*n))->1n for recurrsive calls + 1n for extra-memory(dictionary)
def fibonacci_series2(n):
    memoize_dict = {}

    def fibonacci(n):
        if n == 0 or n == 1:
            return n
        
        if n in memoize_dict:
            return memoize_dict[n]
    
        memoize_dict[n] = fibonacci(n-1) + fibonacci(n-2)
        return memoize_dict[n]


    return fibonacci(n)



# 3. Bottom-up Approach(Tabulation)
# Time-Complexity(O(n))
# Space-Complexity(O(n))->for dp->array
def fibonacci_series3(n):
    dp = [0,1]

    for i in range(2,n+1):
        new = dp[i-1] + dp[i-2]       
        dp.append(new)

    return dp[n]


# 4. Bottom-up No-memory DP
# Time-Complexity(O(n))
# Space-Complexity(O(1))-> No additional space
def fibonacci_series4(n):
    prev1 = 1
    prev2 = 0
    curr = n

    for i in range(2,n+1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return curr

print(fibonacci_series1(7))
print(fibonacci_series2(7))
print(fibonacci_series3(7))
print(fibonacci_series4(7))