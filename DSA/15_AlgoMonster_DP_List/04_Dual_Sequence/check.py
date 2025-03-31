


def min_deletions_to_make_equal(s1: str, s2: str) -> int:
    def min_delete(i,j):

        # If s1 is empty, delete all characters from s2
        if i == len(s1):  
            return len(s2) - j
        # If s2 is empty, delete all characters from s1
        if j == len(s2):  
            return len(s1) - i
        
        # If characters match, move to the next character in both strings
        if s1[i] == s2[j]:
            return min_delete(i + 1, j + 1)
        
        # If characters do not match, delete either character and count the deletion
        delete_s1 = 1 + min_delete(i + 1, j)
        delete_s2 = 1 + min_delete(i, j + 1)
        # Return the minimum deletions required
        return min(delete_s1, delete_s2)
    return min_delete(0,0)



# Example usage
s1 = "sea"
s2 = "eat"
print(min_deletions_to_make_equal(s1, s2))  # Output: 2
print(min_deletions_to_make_equal('delete', 'leet'))  # Output: 2
print(min_deletions_to_make_equal('deete', 'leet'))  # Output: 2
# deete, leet