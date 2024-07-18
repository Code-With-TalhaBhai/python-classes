

def longest_common_prefix_without_trie(strs):
    prefix = ""

    for i in range(len(strs[0])):
        ch = strs[0][i]
        same = True
        

        for j in range(1,len(strs)):
            if (i == len(strs[j])) or (ch != strs[j][i]):
                same = False
                break

        if same == False:
            break
        else:
            prefix += ch

    return prefix





strs1 = ["flower","flow","flight"]
strs2= ["dog","racecar","car"]
strs3 = ["ab", "a"]

print(longest_common_prefix_without_trie(strs1))
print(longest_common_prefix_without_trie(strs2))
print(longest_common_prefix_without_trie(strs3))