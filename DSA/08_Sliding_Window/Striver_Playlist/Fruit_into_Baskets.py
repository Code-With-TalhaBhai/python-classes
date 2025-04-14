

from collections import defaultdict


def totalFruit1(fruits,k) -> int:
    n = len(fruits)
    basket = set()
    max_len = 0

    for i in range(n):
        for j in range(i,n):
            basket.add(fruits[j])
            if len(basket) <= k:
                # print(i,j)
                max_len = max(max_len,j-i+1)
            else:
                basket.clear()
                break
    return max_len


def totalFruit2(fruits,k) -> int:
    n = len(fruits)
    basket = {}
    max_len = 0
    l = 0


    for r in range(n):
        if fruits[r] not in basket:
            basket[fruits[r]] = 0
        basket[fruits[r]] += 1

        while len(basket) > k:
            basket[fruits[l]] -= 1
            if basket[fruits[l]] == 0:
                basket.pop(fruits[l])
            l += 1
        max_len = max(max_len,r-l+1)
    return max_len


def totalFruit3(fruits,k) -> int:
    n = len(fruits)
    basket = {}
    max_len = 0
    l = 0

    for r in range(n):
        if fruits[r] not in basket:
            basket[fruits[r]] = 0
        basket[fruits[r]] += 1

        if len(basket) > k:
            basket[fruits[l]] -= 1
            if basket[fruits[l]] == 0:
                basket.pop(fruits[l])
            l += 1
        max_len = max(max_len,r-l+1)
    return max_len


fruits1 = [1,2,1]
fruits2 = [0,1,2,2]
fruits3 = [1,2,3,2,2]
fruits4 = [1,0,1,4,1,4,1,2,3]

print('brute-force')
print(totalFruit1(fruits1,2))
print(totalFruit1(fruits2,2))
print(totalFruit1(fruits3,2))
print(totalFruit1(fruits4,2))
print('Optimal -> O(n^2)')
print(totalFruit2(fruits1,2))
print(totalFruit2(fruits2,2))
print(totalFruit2(fruits3,2))
print(totalFruit2(fruits4,2))
print('Optimized -> O(n)')
print(totalFruit3(fruits1,2))
print(totalFruit3(fruits2,2))
print(totalFruit3(fruits3,2))
print(totalFruit3(fruits4,2))
