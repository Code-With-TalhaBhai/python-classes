

# With extra-node
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

    def search(self,word)->bool:
        res = False
        curr = self.root

        for letter in word:
            if letter not in curr:
                return False
            curr = curr[letter]
        
        if "." in curr:
            res = True

        return res
    
    def startsWith(self,prefix)->bool:
        curr = self.root

        for letter in prefix:
            if letter not in curr:
                return False
            curr = curr[letter]
        return True



trie = Trie()

trie.insert('car')
trie.insert('case')
trie.insert('care')
trie.insert('ballon')


print("The following word in trie: ",trie.search('car'))
print("The following word in trie: ",trie.search('case'))
print("The following word in trie: ",trie.search('cared'))
print("The following word in trie: ",trie.search('ballon'))
print("The following word in trie: ",trie.search('kamal'))

print()

print("The following startsWith in trie: ",trie.startsWith('ca'))
print("The following startsWith in trie: ",trie.startsWith('bal'))
print("The following startsWith in trie: ",trie.startsWith('zal'))