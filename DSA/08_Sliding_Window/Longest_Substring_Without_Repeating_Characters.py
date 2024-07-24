


def lengthOfLongestSubstring(s: str) -> int:
    l = 0
    max_window = 0
    char_dict = {}

    # 1st way
    # r = 0
    # for char in s:  
    #     while char in char_dict:
    #         char_dict.pop(s[l])
    #         l += 1

    #     max_window = max(max_window,(r-l)+1)
    #     char_dict[char] = True
    #     r += 1


    # 2nd way
    for r in range(len(s)):
        while s[r] in char_dict:
            char_dict.pop(s[l])
            l += 1

        max_window = max(max_window,(r-l)+1)
        char_dict[s[r]] = True
    return max_window


    

s = "abcabcbb"
# s = "pwwkew"
print(lengthOfLongestSubstring(s))