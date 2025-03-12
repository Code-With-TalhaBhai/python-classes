

def mincostTickets1(days,costs):
    n = len(days)
    memo = {n:0}

    def mincost(i,rem_days):
        if i == n:
            return 0
        
        if rem_days > days[i]:
            return mincost(i+1,rem_days)
        elif i in memo:
            return memo[i]
        else:
            memo[i] = min(
                costs[0] + mincost(i+1,days[i]+1),
                costs[1] + mincost(i+1,days[i]+7),
                costs[2] + mincost(i+1,days[i]+30)
            )
            return memo[i]
        
    return mincost(0,days[0])



def mincostTickets2(days,cost):
    n = len(days)
    maxi = max(days)
    dp = [0 for i in range(maxi+1)]
    j = 0

    # for i in range(maxi+1):
    for day in range(days[0],maxi+1): # space optimization
        if day != days[j]:
            dp[day] = dp[day-1]
        elif day == days[j]:
            dp[day] = dp[day-1] + cost[0]
            
            if days[j] - 7 <= 0:
                dp[day] = min(dp[day],cost[1])
            else:
                dp[day] = min(dp[day],dp[days[j]-7]+cost[1])
            
            if days[j] - 30 <= 0:
                dp[day] = min(dp[day],cost[2])
            else:
                dp[day] = min(dp[day],dp[days[j]-30]+cost[2])
            j += 1

    # print(dp)
    return dp[maxi]






days1 = [1,4,6,7,8,20]
days2 = [1,2,3,4,5,6,7,8,9,10,30,31]
days3 = [6,8,9,18,20,21,23,25]
costs = [2,7,15]

print(mincostTickets1(days1,costs))
print(mincostTickets1(days2,costs))
print(mincostTickets1(days3,[2,10,41]))
print()
print(mincostTickets2(days1,costs))
print(mincostTickets2(days2,costs))
print(mincostTickets2(days3,[2,10,41]))