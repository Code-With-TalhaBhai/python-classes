





def Longest_Prefix_Suffix_KMP(s):
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



print(Longest_Prefix_Suffix_KMP('abcabdabcabdabdab')) # Time-Complexity -> O(N+M)
print(Longest_Prefix_Suffix_KMP('bbb'))
print(Longest_Prefix_Suffix_KMP('babbb'))


