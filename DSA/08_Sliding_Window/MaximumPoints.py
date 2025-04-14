

def maxScore(cardPoints, k: int) -> int:
    n = len(cardPoints)
    max_sum = 0
    
    for i in range(k):
        max_sum += cardPoints[i]
    
    if n == k:
        return max_sum
    
    sum = max_sum
    # for i in range(k):
    for i in range(1,k+1):
        # sum -= cardPoints[k-i-1]
        # sum += cardPoints[n-i-1]
        sum -= cardPoints[k-i]
        sum += cardPoints[n-i]
        max_sum = max(max_sum,sum)
    return max_sum



cardPoints1 = [1,2,3,4,5,6,1]
cardPoints2 = [9,7,7,9,7,7,9]


print(maxScore(cardPoints1,3))
print(maxScore(cardPoints2,7))