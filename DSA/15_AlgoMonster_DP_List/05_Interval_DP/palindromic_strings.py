


def countSubstrings1(s):
    n = len(s)
    count = 0

    for i in range(n):
        l,r = i,i
        while l >= 0 and r < n and s[l] == s[r]:
            l -=1 
            r += 1
            count += 1

        l = i
        r = i+1
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
            count +=1
    return count 




def countSubstrings2(s):
    ...


# Simple
print(countSubstrings1('abc'))
print(countSubstrings1('aaa'))


# By Manacher's Algorithm
print(countSubstrings2('abc'))
print(countSubstrings2('aaa'))


