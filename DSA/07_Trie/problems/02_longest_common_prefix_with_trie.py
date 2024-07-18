

from operator import le


class Trie:

    def __init__(self):
        self.root = {}

    def insert(self,word):
        curr = self.root
        for letter in word:
            if letter not in curr:
                curr[letter] = {}
            curr = curr[letter]
        curr["."] = "."




def longest_common_prefix(strs):
    trie = Trie()
    prefix = ""

    for string in strs:
        trie.insert(string)


    curr = trie.root
    for letter in strs[0]:
        if len(curr) == 1:
            prefix += letter
        else:
            break
        curr = curr[letter]

    return prefix
    



strs1 = ["flower","flow","flight"]
strs2= ["dog","racecar","car"]
strs3 = ["ab", "a"]

print(longest_common_prefix(strs1))
print(longest_common_prefix(strs2))
print(longest_common_prefix(strs3))