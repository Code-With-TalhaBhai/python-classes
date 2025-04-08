


def minBitFlips(start: int, goal: int) -> int:
    
    res = start ^ goal # checking how many bits are change, which then set to 1.
    
    cnt = 0
    while res != 0:
        res = res & (res - 1)
        cnt += 1
    return cnt
    


start1 = 10
goal1 = 7

start2 = 3
goal2 = 4

print(minBitFlips(start1,goal1))
print(minBitFlips(start2,goal2))
print(minBitFlips(3,2))


