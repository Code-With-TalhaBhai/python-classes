


def lengthAfterTransformations1(s: str, t: int) -> int:
    res = s
    for i in range(t):
        final = ''
        for char in res:
            if char == 'z':
                final += 'ab'
            else:
                final += chr(ord(char)+1)
        res = final
    return len(final) % (10**9+7)



def lengthAfterTransformations2(s: str, t: int) -> int:
    MOD = (10 ** 9 + 7)
    res = [0] * 26
    for char in s:
        res[ord(char)-ord('a')] += 1


    for _ in range(t):
        newRes = [0] * 26

        for i in range(25):
            newRes[i+1] = res[i]
        newRes[0] = res[25]
        newRes[1] = (newRes[1]+res[25]) % MOD
        res = newRes
    return sum(res) % MOD


s1 = "abcyy"
t1 = 2
s2 = "azbk"
t2 = 1


print('brute-force')
print(lengthAfterTransformations1(s1,t1))
print(lengthAfterTransformations1(s2,t2))
print('optimal')
print(lengthAfterTransformations2(s1,t1))
print(lengthAfterTransformations2(s2,t2))