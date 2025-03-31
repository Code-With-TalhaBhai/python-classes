# Minimum characters delete to make strings equal


def minimum_characters_delete1(s1,s2):
    m = len(s1)
    n = len(s2)

    memo = {}
    def min_delete(i,j):
        if (i,j) in memo:
            return memo[(i,j)]
        
        if i == m:
            return n - j
        if j == n:
            return m - i
        
        if s1[i] == s2[j]:
            memo[(i,j)] = min_delete(i+1,j+1)
            return memo[(i,j)]
        
        first = 1 + min_delete(i+1,j)
        second = 1 + min_delete(i,j+1)
        memo[(i,j)] = min(first,second)
        return memo[(i,j)]
    return min_delete(0,0)



def minimum_characters_delete2(s1,s2):
    m = len(s1)
    n = len(s2)

    ...



print(minimum_characters_delete1('sea','eat'))
print(minimum_characters_delete1('delete','leet'))
print()
print(minimum_characters_delete2('sea','eat'))
print(minimum_characters_delete2('delete','leet'))