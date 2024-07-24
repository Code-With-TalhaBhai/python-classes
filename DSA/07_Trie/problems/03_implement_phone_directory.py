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




def display_prefixes(curr,prefix,all_seraches):
    if "." in curr:
        all_seraches.append(prefix[0])
        return 

    for letter in curr:
        prefix[0] += letter
        display_prefixes(curr[letter],prefix,all_seraches)  
        prefix[0] = prefix[0][:-1] # deleting element


def displayContacts(trie_contact, s):

    for letter in s:
        if letter not in trie_contact:
            return []
        trie_contact = trie_contact[letter]

    all_searches = []
    display_prefixes(trie_contact,[s],all_searches)
    return all_searches


def input_output_function(contact,s):
    trie_contact = Trie()
    for word in contact:
        trie_contact.insert(word)
    trie_contact = trie_contact.root

    prefix = ""
    for char in s:
        prefix += char
        print(displayContacts(trie_contact,prefix))
    print()
    # print(displayContacts(trie_contact,"g"))

contacts1 = ["geeikistest", "geeksforgeeks", "geeksfortest"]
s1 = "geeips"

contacts2 = ["cod","coding","codding","code","coly"]
s2 = "coding"


input_output_function(contacts1,s1)
input_output_function(contacts2,s2)



