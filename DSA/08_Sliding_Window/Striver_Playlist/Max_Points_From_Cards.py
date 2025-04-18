


def maxScore(cardPoints, k: int) -> int:
    profit = 0
    n = len(cardPoints)
    for i in range(k):
        profit += cardPoints[i]

    if k == n:
        return profit

    max_profit = profit
    for i in range(1,k+1):
        profit -= cardPoints[k-i]
        profit += cardPoints[n-i]
        max_profit = max(max_profit,profit)

    return max_profit



cardPoints1 = [1,2,3,4,5,6,1]
k1 = 3

cardPoints2 = [9,7,7,9,7,7,9]
k2 = 7


print(maxScore(cardPoints1,k1))
print(maxScore(cardPoints2,k2))