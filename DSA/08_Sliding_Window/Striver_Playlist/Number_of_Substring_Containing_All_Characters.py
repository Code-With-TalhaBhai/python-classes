

def numberOfSubstrings1(s: str):
    n = len(s)
    cnt = 0
    characters = {}

    # 1st way
    # for i in range(n):
        # for j in range(i,n):
            # characters[s[j]] = True
            # if 'a' in characters and 'b' in characters and 'c' in characters:
            #     cnt += 1
        # characters.clear()

    # 2nd way
    # for i in range(n):
    #     # characters = {0:0,1:0,2:0}
    #     characters = [0,0,0]
    #     for j in range(i,n):
    #         characters[ord(s[j])-ord('a')] = 1
    #         if characters[0] + characters[1] + characters[2] == 3:
    #             cnt += 1
    # return cnt


    # 3rd way - More Optimized
    for i in range(n):
        characters = [0,0,0]
        for j in range(i,n):
            characters[ord(s[j])-ord('a')] = 1
            if characters[0] + characters[1] + characters[2] == 3:
                cnt += n - j
                break
    return cnt
    

def numberOfSubstrings2(s: str):
    n = len(s)
    cnt = 0
    # char_idx = {
    #     'a': -1,
    #     'b': -1,
    #     'c': -1
    # }
    char_idx = [-1,-1,-1]

    for i in range(n):
        char_idx[ord(s[i])- ord('a')] = i
        min_val = min(char_idx)
        if min_val > -1:
            cnt += min_val + 1
    return cnt









s1 = "abcabc"
s2 = "aaacb"

print(numberOfSubstrings1(s1))
print(numberOfSubstrings1(s2))
print('Optimal')
print(numberOfSubstrings2(s1))
print(numberOfSubstrings2(s2))
