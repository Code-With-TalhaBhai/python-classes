

def countSubstrings(s: str) -> int:
    total = 0
    n = len(s)

    for i in range(n):
        l,r = i,i
        while l >= 0 and r < n and s[l] == s[r]:
            total += 1 
            l -= 1
            r += 1

        l,r = i,i+1
        while l >= 0 and r < n and s[l] == s[r]:
            total += 1
            l -= 1
            r += 1

    return total
        


s1 = "aaa"
s2 = "abc"



print(countSubstrings(s1))
print(countSubstrings(s2))