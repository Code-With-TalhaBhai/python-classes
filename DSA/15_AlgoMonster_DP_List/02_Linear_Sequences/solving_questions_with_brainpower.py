


def solving_questions_with_brain_power1(questions):
    n = len(questions)
    memo = {}

    def solve(i):
        if i >= n:
            return 0
        if i in memo:
            return memo[i]
        
        memo[i] = max(questions[i][0]+solve(i+questions[i][1]+1),solve(i+1))
        return memo[i]
    return solve(0)



def solving_questions_with_brain_power2(questions):
    n = len(questions)

    dp = [0 for i in range(n)]
    dp[n-1] = questions[n-1][0]

    # for i in range(n-2,-1,-1):
    #     if i + questions[i][1] + 1 >= n:
    #         dp[i] = max(dp[i+1],questions[i][0])
    #     else:
    #         dp[i] = max(dp[i+1],questions[i][0]+dp[i+questions[i][1]+1])

    # More Descriptive
    for i in range(n-2,-1,-1):
        curr_points = questions[i][0]
        questions_to_skip = questions[i][1]

        if i + questions_to_skip + 1 >= n:
            dp[i] = max(dp[i+1],curr_points)
        else:
            dp[i] = max(dp[i+1],curr_points + dp[i+questions_to_skip+1])


    # 2nd way
    # dp = [0] * (n+1)
    # for i in range(n-1,-1,-1):
    #     questions_to_skip = i + questions[i][1] + 1 
    #     dp[i] = max(dp[i+1],dp[min(questions_to_skip,n)]+questions[i][0])
    # return dp[0]



questions1 = [[3,2],[4,3],[4,4],[2,5]]
questions2 = [[1,1],[2,2],[3,3],[4,4],[5,5]]
questions3 = [[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]]


print(solving_questions_with_brain_power1(questions1))
print(solving_questions_with_brain_power1(questions2))
print(solving_questions_with_brain_power1(questions3))
print()
print(solving_questions_with_brain_power2(questions1))
print(solving_questions_with_brain_power2(questions2))
print(solving_questions_with_brain_power2(questions3))