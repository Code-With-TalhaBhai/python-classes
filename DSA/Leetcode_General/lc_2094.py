


def findEvenNumbers1(digits):
    n = len(digits)
    final = set()

    for i in range(n):
        if digits[i] == 0:
            continue
        for j in range(n):
            if i == j:
                continue
            for k in range(n):
                if i == k or j == k:
                    continue

                num = digits[i] * 100 + digits[j] * 10 + digits[k]
                if num % 2 == 0:
                    final.add(num)
    final = sorted(final)
    return final



def findEvenNumbers2(digits):
    import collections
    final = []
    counter = collections.Counter(digits)

    for i in range(1,10):
        if counter[i] == 0:
            continue
        counter[i] -= 1
        for j in range(0,10):
            if counter[j] == 0:
                continue
            counter[j] -= 1
            for k in range(0,10,2):
                if counter[k] == 0:
                    continue
                num = i * 100 + j * 10 + k
                final.append(num)
            counter[j] += 1
        counter[i] += 1
    return final



digits1 = [2,1,3,0]
digits2 = [2,2,8,8,2]
digits3 = [3,7,5]


print('brute-force')
print(findEvenNumbers1(digits1))
print(findEvenNumbers1(digits2))
print(findEvenNumbers1(digits3))
print('Optimal')
print(findEvenNumbers2(digits1))
print(findEvenNumbers2(digits2))
print(findEvenNumbers2(digits3))