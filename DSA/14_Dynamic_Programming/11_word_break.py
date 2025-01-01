


def word_break1(s,wordDict):
    n = len(s)

    # index as argument
    # def word_b_1(i):
    #     if s[i:] in wordDict:
    #         return True
    #     for j in range(i,n):
    #         s_word = s[i:j]
    #         if s_word in wordDict:
    #             if word_b_1(j):
    #                 return True
    #     return False
    # return word_b_1(0)

    # substring as argument
    def word_b_2(s):
        if s in wordDict:
            return True
        for j in range(1,n):
            s_word = s[:j]
            if s_word in wordDict:
                if word_b_2(s[j:]):
                    return True
        return False
    return word_b_2(s)



def word_break2(s,wordDict):
    n = len(s)
    memo = {0 : True}

    def word_b(i):
        if s[i:] in wordDict:
            return True

        if i in memo and memo[i] == False:
            return False

        
        for j in range(i,n):
            s_word = s[i:j]
            if s_word in wordDict:
                if word_b(j):
                    return True

        memo[i] = False
        return memo[i]

    word_b(0)
    return memo[0]


def word_break3(s,wordDict):
    n = len(s)
    dp = [False] * (n+1)

    # 1st way
    dp[n] = True
    for i in range(n-1,-1,-1):
        for word in wordDict:
            s_len_to_match = i + len(word)
            if s_len_to_match <= n and s[i: s_len_to_match] == word:
                dp[i] = dp[s_len_to_match]
            if dp[i]:
                break
    return dp[0]
        



s1 = "leetcode"
wordDict1 = ["leet","code"]

s2 = "applepenapple"
wordDict2 = ["apple","pen"]

s3 = "catsandog"
wordDict3 = ["cats","dog","sand","and","cat"]

s4 = "aaaaaaa"
wordDict4 = ["aaaa","aa"]


print('With Recurrsion')
print(word_break1(s1,wordDict1))
print(word_break1(s2,wordDict2))
print(word_break1(s3,wordDict3))
print(word_break1(s4,wordDict4))
print()

print('With Memoization')
print(word_break2(s1,wordDict1))
print(word_break2(s2,wordDict2))
print(word_break2(s3,wordDict3))
print(word_break2(s4,wordDict4))
print()

print('with Tabulation')
print(word_break3(s1,wordDict1))
print(word_break3(s2,wordDict2))
print(word_break3(s3,wordDict3))
print(word_break3(s4,wordDict4))