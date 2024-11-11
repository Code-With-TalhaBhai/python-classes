

# recurrsion
def count_number_hop1(i,n):
    if i == n:
        return 1
    if i > n:
        return 0
    
    return count_number_hop1(i+1,n) + count_number_hop1(i+2,n) + count_number_hop1(i+3,n)


def count_number_hop2(n):
    if n == 0:
        return 1
    
    if n < 0:
        return 0
    
    return count_number_hop2(n-1)+count_number_hop2(n-2)+count_number_hop2(n-3)


# Memoization(Top-Down)
def count_number_hop3(n):
    memo = {n:1}

    def count_num(i):
        if i > n:
            return 0

        if i not in memo:
            memo[i] = count_num(i+1) + count_num(i+2) + count_num(i+3)

        return memo[i]

    
    count_num(0)
    return memo[0]


# Bottom-Up(Tabulation)
def count_number_hop4(n):
    tabulation = []
    for i in range(n+1):
        tabulation.append(i)

    tabulation[3] = 4

    for i in range(4,n+1):
        tabulation[i] = tabulation[i-1] + tabulation[i-2] + tabulation[i-3]

    return tabulation[n]



# space-optimized
def count_number_hop5(n):
    if n < 3:
        return n

    curr = 4
    prev1 = 4
    prev2 = 2
    prev3 = 1    

    for i in range(4,n+1):
        curr = prev1 + prev2 + prev3
        prev3 = prev2
        prev2 = prev1
        prev1 = curr



    return curr



n = 5
print(count_number_hop1(0,n))
print(count_number_hop2(n))
# DP
print(count_number_hop3(n))
print(count_number_hop4(n))
print(count_number_hop5(n))

