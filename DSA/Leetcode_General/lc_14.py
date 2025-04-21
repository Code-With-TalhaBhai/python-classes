


def longestCommonPrefix(strs):

    prefix = ""

    for i in range(len(strs[0])):
        ch = strs[0][i]
        same = True
        
        for j in range(1,len(strs)):
            if i == len(strs[j]) or ch != strs[j][i]:
                same = False
                break

        if same == False:
            break
        else:
            prefix += ch
    return prefix








strs = ["flower","flow","flight"]
strs = ["dog","racecar","car"]
