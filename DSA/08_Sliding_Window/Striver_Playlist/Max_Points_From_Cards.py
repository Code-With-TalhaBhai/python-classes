


def maxScore(cardPoints, k: int) -> int:
    profit = 0
    for i in range(k+1):
        profit += cardPoints[i]

    for i in range(k+1,len(cardPoints)):
        profit_to_add = cardPoints[i]
        j = 1
        while j <= k:
            profit -= cardPoints[i-j]
            profit += profit_to_add
            j += 1

    return profit



cardPoints1 = [1,2,3,4,5,6,1]
k1 = 3

cardPoints2 = [9,7,7,9,7,7,9]
k2 = 7


print(maxScore(cardPoints1,k1))
print(maxScore(cardPoints2,k2))