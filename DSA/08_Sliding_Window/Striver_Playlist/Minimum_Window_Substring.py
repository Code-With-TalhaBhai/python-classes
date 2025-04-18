

from collections import defaultdict


def minWindow1(s: str, t: str) -> str:
    if len(t) > len(s):
        return ''

    char_freq = defaultdict(int)
    for t_char in t:
        char_freq[t_char] += 1
    # print(char_freq)

    final_str = ''
    min_len = float('inf')
    for l in range(len(s)):
        temp_freq = char_freq.copy()
        for r in range(l,len(s)):
            if s[r] in temp_freq:
                temp_freq[s[r]] -= 1
                if temp_freq[s[r]] == 0:
                    temp_freq.pop(s[r])
                if len(temp_freq) == 0:
                    window_size = r - l + 1
                    if min_len > window_size:
                        min_len = window_size
                        final_str = s[l:r+1]
                    break
    return final_str



def minWindow2(s: str, t: str) -> str:
    if len(t) > len(s):
        return ''
    
    if s == t:
        return s
    
    char_freq = defaultdict(int)
    for t_char in t:
        char_freq[t_char] += 1

    l = 0
    min_len = float('inf')
    start_idx = -1
    cnt = 0

    for r in range(len(s)):
        char_freq[s[r]] -= 1
        if char_freq[s[r]] >= 0:
            cnt += 1


        while l < len(s) and cnt > len(t) - 1:
            if min_len > r - l + 1:
                start_idx = l
                min_len = r - l + 1

            char_freq[s[l]] += 1
            if char_freq[s[l]] > 0:
                cnt -= 1
            l += 1

    if start_idx == -1:
        return ''
    
    final_str = s[start_idx:start_idx+min_len+1]
    return final_str
       


s1 = "ADOBECODEBANC" 
t1 = "ABC"
s2 = "a"
t2 = "a"
s3 = "a"
t3 = "aa"


print('brute-force')
print(minWindow1(s1,t1))
print(minWindow1(s2,t2))
print(minWindow1(s3,t3))
print(minWindow1('a','b'))
print('Sliding-Window')
print(minWindow2(s1,t1))
print(minWindow2(s2,t2))
print(minWindow2(s3,t3))
print(minWindow2('a','b'))