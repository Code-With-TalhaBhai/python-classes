



def lengthOfLongestSubstring1(s: str):
    
    max_len = 0
    my_dict = {}
    l,r = 0,0
    

    while r < len(s):
        while s[r] in my_dict:
            my_dict.pop(s[l])
            l += 1
        else:
            my_dict[s[r]] = True
            max_len = max(max_len,r-l+1)
            r += 1
    return max_len


def lengthOfLongestSubstring2(s: str):
    
    max_len = 0
    my_dict = {}
    l,r = 0,0

    while r < len(s):
        if s[r] in my_dict:
            idx = my_dict.pop(s[l])
            l = idx + 1
        else:
            my_dict[s[r]] = r
            max_len = max(max_len,r-l+1)
            r += 1
    return max_len




s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"


print(lengthOfLongestSubstring1(s1))
print(lengthOfLongestSubstring1(s2))
print(lengthOfLongestSubstring1(s3))
print('Optimal')
print(lengthOfLongestSubstring2(s1))
print(lengthOfLongestSubstring2(s2))
print(lengthOfLongestSubstring2(s3))