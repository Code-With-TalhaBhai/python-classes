
# n ---> number of dices
# k ---> number of faces

def numRollsToTarget1(n: int, k: int, target: int) -> int:
    MOD = 10**9+7

    memo = {}
    def numRolls(curr_sum,dice_left):
        if curr_sum == target and dice_left == 0:
            return 1
        
        if curr_sum > target or dice_left == 0:
            return 0
        
        if (curr_sum,dice_left) in memo:
            return memo[(curr_sum,dice_left)] 

        total = 0
        for r in range(1,k+1):
            total += numRolls(curr_sum+r,dice_left-1)
        memo[(curr_sum,dice_left)] = total % MOD
        return memo[(curr_sum,dice_left)]   
    return numRolls(0,n)

    

# def numRollsToTarget2(n: int, k: int, target: int) -> int:
#     MOD = (10**9)+7
#     if n == 1:
#         if target < k:
#             return 1
#         else:
#             return 0
    
    # dp = [[0 for i in range()] for i in range()]
    # ...
    





print('Recurrsion')
print(numRollsToTarget1(1,6,3))
print(numRollsToTarget1(2,6,7))
print(numRollsToTarget1(30,30,500)) # only work with memoization, because time-complexity is too high
print(numRollsToTarget1(10,10,100)) # only work with memoization, because time-complexity is too high
print('DP')
# print(numRollsToTarget2(1,6,3))
# print(numRollsToTarget2(2,6,7))
# print(numRollsToTarget2(30,30,600))
# print(numRollsToTarget2(10,10,100))
