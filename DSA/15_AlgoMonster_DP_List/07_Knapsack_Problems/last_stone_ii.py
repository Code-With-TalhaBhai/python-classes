


def last_stone_ii_1(stones):
    n = len(stones)
    memo = {}

    # def last_stone1(i,sum1,sum2):
    #     if i == n:
    #         return abs(sum1-sum2)

    #     if (i,sum1,sum2) in memo:
    #         return memo[(i,sum1,sum2)]

    #     memo[(i,sum1,sum2)] = min(last_stone(i+1,sum1+stones[i],sum2),last_stone(i+1,sum1,sum2+stones[i]))
    #     return memo[(i,sum1,sum2)]
    # return last_stone1(0,0,0)



    total_sum = sum(stones)
    target = stones // 2
    def last_stone2(i,curr_sum):
        if curr_sum >= target or i == n:
            return abs(curr_sum - (total_sum - curr_sum))
        if (i,curr_sum) in memo:
            return memo[(i,curr_sum)]

        memo[(i,curr_sum)] = min(
            last_stone2(i+1,curr_sum+stones[i]),
            last_stone2(i+1,curr_sum)
        )
        return memo[(i,curr_sum)]
    return last_stone2(0,0)


stones1 = [2,7,4,1,8,1]
stones2 = [31,26,33,21,40]


print(last_stone_ii_1(stones1))
print(last_stone_ii_1(stones2))