


def brute_force(s):
    n = len(s)
    for i in range(n-1):
        k = 0
        j = i + 1
        # cnt = 0
        final_str = ''
        while j < n:
            if s[k] != s[j]:
                break
            final_str += s[k]
            # cnt += 1 
            k += 1
            j += 1 
        if j == n:
            # return cnt          
            return final_str
    return ''



# Uses Prefix-Suffix Array
def KMP1(s):
    n = len(s)
    lp = [0] * n
    p = 0
    
    for i in range(1,n):
        if s[p] == s[i]:
            p += 1
            lp[i] = p
        else:
            while p != 0 and s[p] != s[i]:
                p = lp[p-1]

            if s[p] == s[i]:
                lp[i] = p + 1
                p += 1
    # print(lp)
    # return lp[n-1]
    return s[:lp[n-1]]



def KMP2(s):
    n = len(s)
    lps = [0] * n
    p = 0
    i = p + 1

    while i < n:
        if s[i] == s[p]:
            p += 1
            lps[i] = p
            i += 1
        else:
            if p != 0:
                p = lps[p-1]
            else:
                lps[i] = 0
                i += 1
    # return lps[n-1]
    return s[:lps[n-1]]




s = "abcabdabcabdabdab"
print(brute_force(s)) # Time-Complexity -> O(N.M)
print(brute_force('bbb'))
print(brute_force('babbb'))
print()
print(KMP1(s)) # Time-Complexity -> O(N+M)
print(KMP1('bbb'))
print(KMP1('babbb'))
print()
print(KMP2(s)) # Time-Complexity -> O(N+M)
print(KMP2('bbb'))
print(KMP2('babbb'))